import os
import json
from collections import Counter
from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle
import base64
import json

'''
    This code is used to preprocess emails, providing some basic information,
    including counting the average number of words per email,
     the number of words that appear the most,
     the number of times specified keywords appear, 
     and the collection time of each email
'''

# Use the credentials.json file from the Gmail API to authenticate
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

# get the content of emails
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
        text = content.get('body', '')
        words = text.split()
        return len(words)
        
# get the keywords in emails
def find_keywords_in_json_files(folder_path, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}
    # Traverse all files in a folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # Open and read JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    # Update keyword count
                    update_keyword_counts(data, keyword_counts)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file {filename}")

    return keyword_counts
    

# count the keywords
def update_keyword_counts(data, keyword_counts):
    if isinstance(data, dict):
        for k, v in data.items():
            for keyword in keyword_counts:
                if keyword in k or (isinstance(v, str) and keyword in v):
                    keyword_counts[keyword] += 1
            if isinstance(v, (dict, list)):
                update_keyword_counts(v, keyword_counts)
    elif isinstance(data, list):
        for item in data:
            update_keyword_counts(item, keyword_counts)
    elif isinstance(data, str):
        for keyword in keyword_counts:
            if keyword in data:
                keyword_counts[keyword] += 1


# save count of keywords to txt
def save_counts_to_file(keyword_counts, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for keyword, count in keyword_counts.items():
            file.write(f"{keyword}: {count}\n")


# extract words except the space and punctuation
def extract_words_from_data(data):
    words = []
    if isinstance(data, dict):
        for v in data.values():
            words.extend(extract_words_from_data(v))
    elif isinstance(data, list):
        for item in data:
            words.extend(extract_words_from_data(item))
    elif isinstance(data, str):
        # Simple segmentation logic, where words are segmented by spaces and punctuation is removed
        words.extend(data.translate(str.maketrans('', '', ',.!?;:"()[]{}')).lower().split())
    return words


# get the words with most occurrences
def find_most_common_words(folder_path, n):
    all_words = Counter()  # Use Counter to count word occurrences
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    words = extract_words_from_data(data)
                    all_words.update(words)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file {filename}")

    # Find the N words with the highest frequency of occurrence
    most_common_words = all_words.most_common(n)
    return most_common_words

# save the counted words to the txt
def save_most_common_words_to_file(most_common_words, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in most_common_words:
            file.write(f"{word}: {count}\n")

# Find the N words with the highest frequency of occurrence
folder_path = 'data'
n = 1000
most_common_words = find_most_common_words(folder_path, n)
print(f"Most common words: {most_common_words}")

output_file = 'most_common_words.txt'
save_most_common_words_to_file(most_common_words, output_file)
print(f"Most common words have been saved to {output_file}")

# Count the number of occurrences of each candidate
folder_path = 'data'
keywords = ['Biden', 'Joe', 'Joe Biden', 'Trump', 'Donald', 'Donald Trump', 'Haley', 'Nikki', 'Haley Nikki', 'Phillips', 'Dean', 'Dean Phillips']  # Change here to the list of keywords you want to search for
keyword_counts = find_keywords_in_json_files(folder_path, keywords)
print(f"Keyword counts: {keyword_counts}")

output_file = 'candidates_count.txt'
save_counts_to_file(keyword_counts, output_file)
print(f"Keyword counts have been saved to {output_file}")


# Calculate the average number of words in emails
folder_path = 'data'
file_paths = Path(folder_path).glob('*.json')

total_words = 0
file_count = 0

for file_path in file_paths:
    word_count = process_file(file_path)
    total_words += word_count
    file_count += 1

average_words_per_file = total_words / file_count if file_count else 0

print(f"Average words per JSON file: {average_words_per_file}")

output_file_path = 'Average_words.txt'

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(f"Average words per E-mail: {average_words_per_file}")

# get data of emails
service = get_gmail_service()

for filename in os.listdir('data'):
    if filename.endswith('.json'):
        with open(os.path.join('data', filename), 'r', encoding='utf-8') as file:
            mail_id = json.load(file)['id']
            message = service.users().messages().get(userId='me', id=mail_id).execute()
            internalDate = int(message['internalDate']) / 1000
            date_time = datetime.datetime.fromtimestamp(internalDate)
            formatted_date = date_time.strftime('%Y-%m-%d')
            formatted_time = date_time.strftime('%H:%M:%S')
            week_day = date_time.strftime('%A')
            with open('emails_info.txt', 'a') as output_file:
                output_file.write(f'{formatted_date}, {formatted_time}, {week_day}\n')

