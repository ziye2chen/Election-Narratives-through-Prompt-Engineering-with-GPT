import os
import re
from collections import defaultdict
'''
    The output of the large model is: subject/validate name (attribute) [evaluation]<relevant region>.
    This code can extract and count the number of occurrences of each part separately by person name, 
    and save it to the corresponding person name file.
'''

# Path to the file containing email analysis results
file_path = 'email_analysis_results_Number of candidate mentions.txt'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()
data = text_data

# Split the data into fragments based on commas and slashes
fragments = re.split(r'[,/]', data)
names = []

# Extract names from fragments
for fragment in fragments:
    match = re.search(r'([^()]+)\s*\(', fragment)
    if match:
        name = match.group(1).strip()
        names.append(name)

# Function to merge lists and count occurrences
def merge_lists(lst):
    merged_dict = {}
    for item in lst:
        if item in merged_dict:
            merged_dict[item] += 1
        else:
            merged_dict[item] = 1

    merged_list = [(key, value) for key, value in merged_dict.items()]
    return merged_list

# Function to remove patterns from the list
def remove_patterns_from_list(lst):
    pattern = r"\[.*?\]|\(.*?\)|<.*?>"
    cleaned_list = [re.sub(pattern, "", item) for item in lst]
    return cleaned_list

# Clean and merge names list
names = remove_patterns_from_list(names)
names = merge_lists(names)

# Filter out names with count less than 20
names = [(name, count) for name, count in names if count > 20]

# Write names and counts to individual files
with open(rf"C:\Users\petrichor_fff\Desktop\CS506\data_mid\Joe Biden.txt", "w") as file:
    file.write(f"Joe Biden\n168\n\n")

for name, number in names:
    with open(rf"C:\Users\petrichor_fff\Desktop\CS506\data_mid\{name}.txt", "w") as file:
        file.write(f"{name}\n{number}\n\n")
        print(name,number)

# Word counts defaultdict
word_counts = defaultdict(lambda: defaultdict(int))

# Function to extract and count words
def extract_and_count_words(sentences_path, person_name):
    with open(sentences_path, 'r') as file:
        for line in file:
            if person_name in line:
                before_slash = line.split('/')[0]
                words = [word.strip() for word in before_slash.split(',')]
                for word in words:
                    if word:
                        word_counts[person_name][word] += 1

# File names in the directory
file_names = os.listdir('data_mid')

# People names extracted from file names
people_names = [file_name[:-4] for file_name in file_names if file_name.endswith('.txt')]

# Folder name
folder_name = 'data_mid'
# Path to sentences file
sentences_file_path = 'email_analysis_results_Number of candidate mentions.txt'

# Extract and count words for each person
for name in people_names:
    extract_and_count_words(sentences_file_path, name)

# Write word counts to individual files
for name, counts in word_counts.items():
    with open(os.path.join(folder_name, f'{name}.txt'), 'a') as file:
        for word, count in counts.items():
            if count >= 5:
                file.write(f'{word}: {count}\n')
        file.write(f'\n')

# Function to update word counts for comma-separated words
def update_word_counts_comma_separated(line, person_name, word_counts):
    words_in_brackets = re.findall(r'\((.*?)\)', line)
    for group in words_in_brackets:
        words = group.split(',')
        for word in words:
            word = word.strip()
            word_counts[person_name][word] += 1

# Folder path
folder_path = 'data_mid'
# Target file path
target_file_path = 'email_analysis_results_Number of candidate mentions.txt'

# Word counts defaultdict
word_counts = defaultdict(lambda: defaultdict(int))

try:
    with open(target_file_path, 'r', encoding='utf-8') as file:
        target_content = file.readlines()
except FileNotFoundError:
    exit()

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        person_name = filename[:-4]
        for line in target_content:
            if person_name in line:
                update_word_counts_comma_separated(line, person_name, word_counts)

# Write word counts to individual files
for person_name, counts in word_counts.items():
    output_file_path = os.path.join(folder_path, f'{person_name}.txt')
    with open(output_file_path, 'a', encoding='utf-8') as file:
        for word, count in counts.items():
            if count > 5:
                file.write(f'{word}: {count}\n')
        file.write(f'\n')

# Function to extract and count words for square bracket-separated words
def extract_and_count_words_2(target_content, person_name, word_counts):
    pattern = re.compile(rf"{re.escape(person_name)}\s*[^][]*\[([^]]+?)\]")
    for line in target_content:
        match = pattern.search(line)
        if match:
            group = match.group(1)
            words = group.split(',')
            for word in words:
                word = word.strip()
                if word:
                    word_counts[person_name][word] += 1

# Word counts defaultdict
word_counts = defaultdict(lambda: defaultdict(int))

# Folder path
folder_path = 'data_mid'
# Target file path
target_file_path = 'email_analysis_results_Number of candidate mentions.txt'

try:
    with open(target_file_path, 'r', encoding='utf-8') as file:
        target_content = file.readlines()
except FileNotFoundError:
    exit()

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        person_name = filename[:-4]
        extract_and_count_words_2(target_content, person_name, word_counts)

# Write word counts to individual files
for person_name, counts in word_counts.items():
    output_file_path = os.path.join(folder_path, f'{person_name}.txt')
    with open(output_file_path, 'a', encoding='utf-8') as file:
        for word, count in counts.items():
            if count >= 1:
                file.write(f'{word}: {count}\n')
        file.write(f'\n')

# Function to extract and count words for angle bracket-separated words
def extract_and_count_words_3(target_content, person_name, word_counts):
    pattern = re.compile(rf"{re.escape(person_name)}\s*[^<>]*\<([^>]+?)\>")
    for line in target_content:
        match = pattern.search(line)
        if match:
            group = match.group(1)
            words = group.split(',')
            for word in words:
                word = word.strip()
                if word:
                    word_counts[person_name][word] += 1

# Word counts defaultdict
word_counts = defaultdict(lambda: defaultdict(int))

# Folder path
folder_path = 'data_mid'
# Target file path
target_file_path = 'email_analysis_results_Number of candidate mentions.txt'

try:
    with open(target_file_path, 'r', encoding='utf-8') as file:
        target_content = file.readlines()
except FileNotFoundError:
    exit()

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        person_name = filename[:-4]
        extract_and_count_words_3(target_content, person_name, word_counts)

# Write word counts to individual files
for person_name, counts in word_counts.items():
    output_file_path = os.path.join(folder_path, f'{person_name}.txt')
    with open(output_file_path, 'a', encoding='utf-8') as file:
        for word, count in counts.items():
            if count >= 1:
                file.write(f'{word}: {count}\n')
