import matplotlib.pyplot as plt
from datetime import datetime

'''
This code is used to visualize data, which includes 
the most meaningful words that appear, 
the most politically related words that appear, 
the number of emails received per day, 
the number of emails received per day of a week, 
the number of emails received at each time of the day, 
and the number of times each candidate appears. 
Line charts, pie charts, and bar charts will be drawn for analysis
'''

def content_to_dict(content):
    content_dict = {}
    for line in content.split('\n'):
        if line:
            key_value = line.split(': ')
            if len(key_value) == 2:
                content_dict[key_value[0]] = float(key_value[1])
    return content_dict

# Assuming 'candidates_count.txt' is the file path
candidates_count_file_path = 'candidates_count.txt'  # Update this path as necessary
# Reading the file content
with open(candidates_count_file_path, 'r') as file:
    candidates_count_content = file.read()

candidates_count_dict = content_to_dict(candidates_count_content)
candidates_count_dict = content_to_dict(candidates_count_content)

selective_words_file_path = 'Meaningful_words.txt'  # Update this path as necessary
with open(selective_words_file_path, 'r') as file:
    selective_words_content = file.read()
selective_words_dict = content_to_dict(selective_words_content)
selective_words_dict = content_to_dict(selective_words_content)

political_words_file_path = 'Political_words.txt'  # Update this path as necessary
with open(political_words_file_path, 'r') as file:
    political_words_content = file.read()
print(political_words_content)
political_words_dict = content_to_dict(political_words_content)
print(political_words_dict)


# Draw bar and pie charts for candidate counting
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(candidates_count_dict.keys(), candidates_count_dict.values(), color='skyblue')
plt.title('Candidates Count')
plt.xticks(rotation=45, ha="right")
plt.ylabel('Counts')

candidates_count_dict = {
'Joe Biden': 67,
'Donald Trump': 98,
'Haley Nikki': 8,
'Dean Phillips': 1,
}
green_shades = [(12/255,163/255,127/255), (1/255,69/255,53/255), (16/255, 220/255,170/255), (12/255, 163/255,127/255)]
plt.subplot(1, 2, 2)
plt.pie(candidates_count_dict.values(), labels=candidates_count_dict.keys(), autopct='%1.1f%%', startangle=140, colors=green_shades)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Candidates Count Distribution')

plt.tight_layout()
plt.savefig('Candidates Count.png')
plt.show()


# Draw bar and pie charts for selective word counting
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(selective_words_dict.keys(), selective_words_dict.values(), color='lightgreen')
plt.title('Most Common Words Count')
plt.xticks(rotation=45, ha="right")
plt.ylabel('Counts')

green_shades = [(12/255,163/255,127/255), (1/255,69/255,53/255), (16/255, 220/255,170/255), (12/255, 163/255,127/255), (16/255, 230/255,177/255)]
plt.subplot(1, 2, 2)
plt.pie(selective_words_dict.values(), labels=selective_words_dict.keys(), autopct='%1.1f%%', startangle=140, colors=green_shades)
plt.axis('equal')
plt.title('Most Common Words Count Distribution')

plt.tight_layout()
plt.savefig('Most Common Words.png')
plt.show()



# Draw bar and pie charts for selective word counting
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(political_words_dict.keys(), political_words_dict.values(), color='lightpink')
plt.title('Most Common Political Words Count')
plt.xticks(rotation=45, ha="right")
plt.ylabel('Counts')

green_shades = [(12/255,163/255,127/255), (1/255,69/255,53/255), (16/255, 220/255,170/255), (12/255, 163/255,127/255), (16/255, 230/255,177/255)]
plt.subplot(1, 2, 2)
plt.pie(political_words_dict.values(), labels=political_words_dict.keys(), autopct='%1.1f%%', startangle=140, colors=green_shades)
plt.axis('equal')
plt.title('Most Common Political Words Count Distribution')
plt.tight_layout()
plt.savefig('Most Common Political Words.png')
plt.show()




file_path = 'emails_info.txt'

# Reading and displaying the first few lines of the file to understand its structure
with open(file_path, 'r') as file:
    lines = file.readlines()
# Processing the file content to extract date and day of week information
email_dates = [line.split(',')[0] for line in lines]
email_days = [line.strip().split(', ')[2] for line in lines]

# Counting emails per date
email_count_per_date = {}
for date in email_dates:
    email_count_per_date[date] = email_count_per_date.get(date, 0) + 1

# Counting emails per day of the week
email_count_per_day = {}
for day in email_days:
    email_count_per_day[day] = email_count_per_day.get(day, 0) + 1

# Sorting the email count per date for plotting
sorted_dates = sorted(email_count_per_date.keys())
sorted_counts = [email_count_per_date[date] for date in sorted_dates]

# Plotting the line chart for emails per date
plt.figure(figsize=(10, 6))
plt.plot(sorted_dates, sorted_counts, marker='o', color = 'lightcoral')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Number of Emails')
plt.title('Number of Emails Received Per Day')
plt.tight_layout()
plt.savefig('Number of Emails Received Per Day.png')
plt.show()


# Plotting the pie chart for emails per day of the week
green_shades = [(12/255,163/255,127/255), (1/255,69/255,53/255), (16/255, 220/255,170/255), (12/255, 163/255,127/255), (16/255, 230/255,177/255)]
days = list(email_count_per_day.keys())
counts = [email_count_per_day[day] for day in days]

plt.figure(figsize=(8, 8))
plt.pie(counts, labels=days, autopct='%1.1f%%', startangle=140, colors=green_shades)
plt.title('Distribution of Emails by Day of the Week')
plt.tight_layout()
plt.savefig('Distribution of Emails by Day of the Week.png')
plt.show()



# Extracting and counting emails per hour
email_hours = [datetime.strptime(line.split(',')[1].strip(), '%H:%M:%S').hour for line in lines]

email_count_per_hour = {}
for hour in email_hours:
    email_count_per_hour[hour] = email_count_per_hour.get(hour, 0) + 1

# Sorting the email count per hour for plotting
sorted_hours = sorted(email_count_per_hour.keys())
sorted_hour_counts = [email_count_per_hour[hour] for hour in sorted_hours]

# Plotting the line chart for emails per hour
plt.figure(figsize=(10, 6))
plt.plot(sorted_hours, sorted_hour_counts, marker='o', linestyle='-', color='lightsalmon')
plt.xticks(range(0, 24))
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Emails')
plt.title('Number of Emails Received Per Hour')
plt.grid(True)
plt.tight_layout()
plt.savefig('Number of Emails Received Per Hour.png')
plt.show()

