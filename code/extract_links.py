import os
import re
import json
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import csv

'''
    This code is used to extract links from the mailbox
'''

# use regex to extract links from email body
def extract_links(email_body):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, email_body)
    return urls

# extract links from emails and count the frequency of each link
def extract_links_from_emails(emails):
    links = {}
    for email in emails:
        extracted_links = extract_links(email)
        for link in extracted_links:
            if link in links:
                links[link] += 1
            else:
                links[link] = 1
    return links

# extract hostnames from links and count the frequency of each hostname
def extract_hostname_from_links(links):
    hostnames = {}
    for link in links:
        try:
            parsed_uri = urlparse(link)
            hostname = parsed_uri.hostname
            if hostname in hostnames:
                hostnames[hostname] += 1
            else:
                hostnames[hostname] = 1
        except ValueError:
            print(f"Skipping malformed URL: {link}")
    return hostnames

# save links and their frequencies to a file
def save_links_to_file(links, output_file):
    with open(output_file, 'w') as f:
        for link, frequency in links:
            f.write(f'{link},{frequency}\n')

# save hostnames and their frequencies to a file
def save_hostnames_to_file(hostnames, output_file):
    with open(output_file, 'w') as f:
        for hostname, frequency in hostnames:
            f.write(f'{hostname},{frequency}\n')

# read emails from files
def read_emails_from_file():
    directory = '../data/email samples/'
    emails = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + filename, 'r') as f:
                email = json.load(f)
                emails.append(email['body'])
    return emails

def plot_top_hostnames(num_top_hostnames=10):
    # Read the hostnames and their frequencies from the file
    with open('../data/hostnames.txt', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Sort the data by frequency in descending order and select the top 10
    data.sort(key=lambda x: int(x[1]), reverse=True)
    top_10_data = data[:num_top_hostnames]

    # Separate the hostnames and frequencies into two lists
    hostnames, frequencies = zip(*top_10_data)
    frequencies = [int(freq) for freq in frequencies]

    # Create a bar chart
    plt.figure(figsize=(20, 10))
    bars = plt.barh(hostnames, frequencies, color='blue')
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', va='center')
    plt.xlabel('Frequency')
    plt.ylabel('Hostname')
    plt.title('Top 10 Frequent Hostnames')
    plt.gca().invert_yaxis()  # invert the y-axis to display the highest value at the top

    # Save the chart to a local file
    plt.savefig('../data/top_10_hostnames.png')

def plot_top_links(num_top_links=10):
    # Read the links and their frequencies from the file
    with open('../data/links.txt', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    top_10_data = data[:num_top_links]

    # Separate the links and frequencies into two lists
    links, frequencies = zip(*top_10_data)
    frequencies = [int(freq) for freq in frequencies]

    # Create a bar chart
    plt.figure(figsize=(30, 10))
    color_map = ["b","r","r","g","b","r","r","r","r","b"]

    bars = plt.barh(links, frequencies, color=color_map)
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', va='center')
    plt.xlabel('Frequency')
    plt.ylabel('Link')
    plt.title('Top 10 Frequent Links')
    plt.gca().invert_yaxis()  # invert the y-axis to display the highest value at the top

    # Save the chart to a local file
    plt.savefig('../data/top_10_links.png')

emails = read_emails_from_file()
links = extract_links_from_emails(emails)
hostnames = extract_hostname_from_links(links)
# sort links and hostnames by frequency in descending order
links = sorted(links.items(), key=lambda x: x[1], reverse=True)
hostnames = sorted(hostnames.items(), key=lambda x: x[1], reverse=True)
for link, frequency in links[:30]:
    print(f'{link}: {frequency}')
save_links_to_file(links, '../data/links.txt')
save_hostnames_to_file(hostnames, '../data/hostnames.txt')

