# Author: Yeganeh Mohammad Salehi
# Enrolment No.: 01/1456323


import os
from collections import Counter
import re


def save_to_file(data, file_path):
    with open(file_path, 'w') as f:
        if isinstance(data, list):
            for item in data:
                f.write(str(item) + "\n")
        elif isinstance(data, dict):
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        else:
            f.write(str(data))


def read_file(file_path: str):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return {
            "status": "failed",
            "error_type": type(e).__name__,
            "error_message": str(e)
        }


def count_words(text: str) -> tuple:
    words_list = text.split()
    total_words_count = len(words_list)
    unique_words_count = len(set(words_list))
    return total_words_count, unique_words_count


def file_content_reveal(file_path: str):
    return read_file(file_path)


def file_lines_count(file_path: str):
    content = read_file(file_path)
    if isinstance(content, dict):
        return 0
    return len(content.splitlines())


def word_term_frequency(word: str, content: str):
    words_list = content.split()
    return words_list.count(word)


def unique_words(doc_path: str):
    content = read_file(doc_path)
    if isinstance(content, dict):
        return []
    words_list = content.split()
    return list(set(words_list))


def type_token_ratio(word: str, doc_path: str):
    content = read_file(doc_path)
    if isinstance(content, dict):
        return 0
    doc_total_words_count, _ = count_words(content)
    total_repeat_count = word_term_frequency(word, content)
    return total_repeat_count / doc_total_words_count if doc_total_words_count > 0 else 0


def generate_ngrams(content: str, n):
    if not 0 < n <= 3:
        return "invalid n"
    words = content.split()
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]


def generate_concordance(doc_path, target_word, context_window=3):
    content = read_file(doc_path)
    if isinstance(content, dict):
        return []
    words = content.split()
    concordance_list = []
    for index, word in enumerate(words):
        if word.lower() == target_word.lower():
            start = max(0, index - context_window)
            end = min(len(words), index + context_window + 1)
            context = ' '.join(words[start:end])
            concordance_list.append(context)
    return concordance_list


def generate_bigrams(words):

    return zip(words, words[1:])


def find_collocations(doc_path, num_collocations=10, min_freq=3):
    content = read_file(doc_path)
    if isinstance(content, dict):
        return []
    words = re.findall(r'\w+', content.lower())
    bigram_counter = Counter(generate_bigrams(words))
    filtered_bigrams = {bigram: count for bigram, count in bigram_counter.items() if count >= min_freq}
    sorted_bigrams = sorted(filtered_bigrams.items(), key=lambda item: item[1], reverse=True)
    return sorted_bigrams[:num_collocations]


def count_documents(directory_path: str) -> int:
    if not os.path.exists(directory_path):
        return 0
    return len([name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))])


def global_statistics(directory_path: str):
    num_documents = count_documents(directory_path)
    if num_documents == 0:
        return {
            "num_documents": 0,
            "total_lines": 0,
            "total_tokens": 0,
            "unique_tokens": 0
        }

    total_lines = 0
    total_tokens = 0
    unique_tokens_set = set()

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        content = read_file(file_path)
        if isinstance(content, dict):
            continue
        total_lines += len(content.splitlines())
        total_words, _ = count_words(content)
        total_tokens += total_words
        unique_tokens_set.update(set(content.split()))

    return {
        "num_documents": num_documents,
        "total_lines": total_lines,
        "total_tokens": total_tokens,
        "unique_tokens": len(unique_tokens_set)
    }


def global_term_frequency(directory_path: str):
    term_counter = Counter()
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        content = read_file(file_path)
        if isinstance(content, dict):
            continue
        words_list = content.split()
        term_counter.update(words_list)
    return dict(term_counter)


def global_type_token_ratio(directory_path: str):
    term_freq = global_term_frequency(directory_path)
    total_tokens = sum(term_freq.values())
    unique_tokens = len(term_freq.keys())
    return unique_tokens / total_tokens if total_tokens > 0 else 0


def global_concordance(directory_path: str, target_word, context_window=3):
    concordance_list = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        concordance_list.extend(generate_concordance(file_path, target_word, context_window))
    return concordance_list


def global_collocations(directory_path: str, num_collocations=10, min_freq=3):
    words = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        content = read_file(file_path)
        if isinstance(content, dict):
            continue
        words.extend(re.findall(r'\w+', content.lower()))

    bigram_counter = Counter(generate_bigrams(words))
    filtered_bigrams = {bigram: count for bigram, count in bigram_counter.items() if count >= min_freq}
    sorted_bigrams = sorted(filtered_bigrams.items(), key=lambda item: item[1], reverse=True)
    return sorted_bigrams[:num_collocations]
