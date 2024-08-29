# Author: Yeganeh Mohammad Salehi
# Enrolment No.: 01/1456323


import os
from your_module import (
    file_content_reveal,
    file_lines_count,
    count_words,
    word_term_frequency,
    type_token_ratio,
    generate_ngrams,
    generate_concordance,
    find_collocations,
    global_statistics,
    global_term_frequency,
    global_type_token_ratio,
    global_concordance,
    global_collocations,
    save_to_file
)

# Paths
file_path = 'C:/Users/yeganeh/Desktop/Yegane_MohammadSalehi/data/long_text_file.txt'
directory_path = 'C:/Users/yeganeh/Desktop/Yegane_MohammadSalehi/data/'
output_dir = 'C:/Users/yeganeh/Desktop/Yegane_MohammadSalehi/output/'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Local statistics
print("Local Statistics:")
content = file_content_reveal(file_path)
if isinstance(content, dict):
    print(f"Error reading file: {content['error_message']}")
else:
    num_lines = file_lines_count(file_path)
    print("Number of lines:", num_lines)
    total_words, unique_words = count_words(content)
    print("Number of words:", total_words)
    print("Number of unique words:", unique_words)
    term_freq = word_term_frequency('example', content)
    print("Term frequency for 'example':", term_freq)
    ttr = type_token_ratio('example', file_path)
    print("Type-Token Ratio for 'example':", ttr)
    bigrams = generate_ngrams(content, 2)
    print("Bigrams:", bigrams)
    concordance = generate_concordance(file_path, 'example')
    print("Concordance for 'example':", concordance)
    collocations = find_collocations(file_path)
    print("Collocations:", collocations)

    # Save outputs to files
    save_to_file(num_lines, os.path.join(output_dir, 'number_of_lines.txt'))
    save_to_file(total_words, os.path.join(output_dir, 'number_of_words.txt'))
    save_to_file(unique_words, os.path.join(output_dir, 'number_of_unique_words.txt'))
    save_to_file(term_freq, os.path.join(output_dir, 'term_frequency_example.txt'))
    save_to_file(ttr, os.path.join(output_dir, 'type_token_ratio_example.txt'))
    save_to_file(bigrams, os.path.join(output_dir, 'bigrams.txt'))
    save_to_file(concordance, os.path.join(output_dir, 'concordance_example.txt'))
    save_to_file(collocations, os.path.join(output_dir, 'collocations.txt'))

# Global statistics
print("\nGlobal Statistics:")
global_stats = global_statistics(directory_path)
print(global_stats)
global_term_freq = global_term_frequency(directory_path)
print("Global Term Frequency:", global_term_freq)
global_ttr = global_type_token_ratio(directory_path)
print("Global Type-Token Ratio:", global_ttr)
global_concordance_list = global_concordance(directory_path, 'example')
print("Global Concordance for 'example':", global_concordance_list)
global_collocations_list = global_collocations(directory_path)
print("Global Collocations:", global_collocations_list)

# Save global outputs to files
save_to_file(global_stats, os.path.join(output_dir, 'global_statistics.txt'))
save_to_file(global_term_freq, os.path.join(output_dir, 'global_term_frequency.txt'))
save_to_file(global_ttr, os.path.join(output_dir, 'global_type_token_ratio.txt'))
save_to_file(global_concordance_list, os.path.join(output_dir, 'global_concordance_example.txt'))
save_to_file(global_collocations_list, os.path.join(output_dir, 'global_collocations.txt'))
