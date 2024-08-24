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
import os
from datetime import datetime, timedelta

'''
    This code will traverse all specified emails, use Google API to find their collection time, 
    then save the collection time to the email_info file, 
    change the email name to collection time, 
    and finally merge the emails received within the same week into one file
'''

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


def parse_filename_to_date(filename):
    """Extract the date from the filename."""
    date_part = filename.split('_')[0]  # Assuming the date is before the first underscore
    return datetime.strptime(date_part, '%Y-%m-%d')

def find_sunday(date):
    """Return the Sunday date for the given date, adjusted for weeks starting on Sunday."""
    return date - timedelta(days=date.weekday())

def group_files_by_week(files):
    """Group files by the week of their dates."""
    weeks = {}
    for file in files:
        date = parse_filename_to_date(file)
        sunday = find_sunday(date)
        if sunday in weeks:
            weeks[sunday].append(file)
        else:
            weeks[sunday] = [file]
    return weeks

def read_file_content(file_path):
    """Read the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_weekly_files(base_path, weeks):
    """Write files grouped by week."""
    for sunday, files in weeks.items():
        week_filename = os.path.join(base_path, f"{sunday.strftime('%Y-%m-%d')}.txt")
        with open(week_filename, 'w', encoding='utf-8') as week_file:
            for file in files:
                content = read_file_content(os.path.join(base_path, file))
                week_file.write(content + '\n')

service = get_gmail_service()

# get data of emails
for filename in os.listdir('data'):
    if filename.endswith('.json'):
        filepath = os.path.join('data', filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            mail_id = json.load(file)['id']

        # Fetch the email using the Gmail API
        message = service.users().messages().get(userId='me', id=mail_id).execute()
        internalDate = int(message['internalDate']) / 1000
        date_time = datetime.datetime.fromtimestamp(internalDate)

        # Format date and time for filenames (using a Windows-compatible format)
        formatted_date = date_time.strftime('%Y-%m-%d')
        formatted_time = date_time.strftime('%H-%M-%S')  # Replace colons with dashes
        week_day = date_time.strftime('%A')

        # Write to the log file
        with open('emails_info.txt', 'a') as output_file:
            output_file.write(f'{formatted_date}, {formatted_time}, {week_day}\n')

        # Rename the JSON file
        new_filename = f'{formatted_date}_{formatted_time}_{week_day}.json'  # Use underscores instead of commas
        new_filepath = os.path.join('data', new_filename)
        os.rename(filepath, new_filepath)


base_path = 'data'  # Update this to your directory containing the files
files = [f for f in os.listdir(base_path) if f.endswith('.json')]  # Assuming all files are .json
weeks = group_files_by_week(files)
write_weekly_files(base_path, weeks)
print("Files have been successfully grouped and saved by week.")
