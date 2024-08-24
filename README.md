# Ds-Donovan-Election-Narratives

This repository contains a series of analysis code to analyze election related emails. 

## Base/Extended Questions that Have Been Answered and The Results

### 1. Create a database of every active candidate and their party
We use the Google Gmail API to extract the required emails from election related email accounts as data. https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/api_call.py

### 2. What themes or narratives is each political party pushing? Does this change by state?
In U.S. politics, different political parties often focus on distinct themes and styles in their campaigning and policy priorities. Here's a general overview of how major parties typically differ:

- **Democratic Party**:
   - **Themes**: Democrats often focus on social justice, climate change, healthcare reform, and stronger federal government intervention in economic and social issues. They advocate for policies that increase government involvement in healthcare, provide greater protections for workers, and promote social equality.
   - **Style**: Democratic campaigns generally emphasize inclusivity and diversity. They tend to appeal to urban voters, younger demographics, and minority groups. Their rhetoric often stresses compassion, equity, and community-based solutions.

- **Republican Party**:
  - **Themes**: Republicans typically prioritize tax cuts, smaller government, deregulation, and conservative social policies. They advocate for a strong national defense, reduced government spending on social programs, and policies that favor business and economic growth.
  - **Style**: Republican campaigns often adopt a more traditionalist and nationalist tone. They appeal mainly to suburban and rural voters, emphasizing individual liberties, personal responsibility, and patriotism. Their messaging tends to focus on maintaining cultural and economic status quo and can be more direct and assertive.


For a broad overview, here are the focus issues in political campaigns for each of the 50 U.S. states:

1. Alabama: Economic development and healthcare access.
2. Alaska: Natural resource management and climate change impacts.
3. Arizona: Immigration policy and water resource management.
4. Arkansas: Economic growth and healthcare improvements.
5. California: Climate change, housing, and healthcare.
6. Colorado: Environmental policy and education funding.
7. Connecticut: Economic inequality and education.
8. Delaware: Job creation and environmental conservation.
9. Florida: Climate resilience and immigration.
10. Georgia: Voting rights and healthcare.
11. Hawaii: Tourism impact and environmental preservation.
12. Idaho: State rights and land use.
13. Illinois: Fiscal reform and crime rates.
14. Indiana: Manufacturing jobs and education reform.
15. Iowa: Agricultural policy and renewable energy.
16. Kansas: Agricultural subsidies and education.
17. Kentucky: Coal industry and healthcare services.
18. Louisiana: Coastal restoration and economic diversification.
19. Maine: Healthcare access and environmental issues.
20. Maryland: Transportation and healthcare.
21. Massachusetts: Education and healthcare innovation.
22. Michigan: Auto industry and infrastructure.
23. Minnesota: Education funding and healthcare.
24. Mississippi: Economic development and healthcare access.
25. Missouri: Job creation and public safety.
26. Montana: Land rights and environmental policies.
27. Nebraska: Agriculture and trade policies.
28. Nevada: Tourism economy and water rights.
29. New Hampshire: Tax policies and education.
30. New Jersey: Infrastructure and education.
31. New Mexico: Energy resources and education.
32. New York: Economic development and public health.
33. North Carolina: Economic growth and education.
34. North Dakota: Energy development and job creation.
35. Ohio: Manufacturing and healthcare.
36. Oklahoma: Energy policy and healthcare.
37. Oregon: Environmental conservation and homelessness.
38. Pennsylvania: Manufacturing and healthcare.
39. Rhode Island: Education reform and job creation.
40. South Carolina: Manufacturing jobs and education.
41. South Dakota: Native American rights and rural healthcare.
42. Tennessee: Economic development and education.
43. Texas: Immigration, energy, and healthcare.
44. Utah: Economic growth and environmental management.
45. Vermont: Rural development and healthcare.
46. Virginia: Government transparency and transportation.
47. Washington: Technology industry and environmental sustainability.
48. West Virginia: Coal industry and economic transition.
49. Wisconsin: Dairy industry and education.
50. Wyoming: Energy sector and land management.

Here are the relevant files:
![Top Keywords by State.png](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Top%20Keywords%20by%20State.png)
![Total Mentions for Each Candidate by Party.png](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Total%20Mentions%20for%20Each%20Candidate%20by%20Party.png)

In addition, a more detailed summary and analysis are provided in this document(Summarized by ChatGPT).(https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/data/final_data/summary_of_a_week.txt)
### Example: 
### 2024-01-22
### Republican Party
1. **Kari Lake (Arizona)**: Kari Lake is actively campaigning for the U.S. Senate seat in Arizona. Her emails emphasize a grassroots movement, criticizing the current state of government and media, advocating for change, and requesting financial support for her campaign.
   
2. **Hung Cao (Virginia)**: Hung Cao's campaign focuses on his background in Navy Special Operations and his stance on immigration and border security. His emails contain strong criticisms of current Democratic policies and stress the importance of securing the border and upholding American laws.

3. **Jonathan Reiss (California)**: Reiss is inviting supporters to a fireside dinner event to discuss his visions for California and the U.S. Senate, aiming to engage directly with potential voters and stakeholders.

4. **Other Republican Initiatives**: Several other emails from Republican candidates and initiatives focus on rallying support against Democratic opponents, emphasizing the need to secure financial contributions to compete effectively.

### Democratic Party
1. **Tammy Baldwin (Wisconsin)**: Baldwin’s campaign emails focus on the urgency of meeting fundraising goals to compete against wealthy Republican opponents and emphasize grassroots support.

2. **Chris Murphy**: Supports Joe Biden and urges contributions to both his own campaign and Biden's, emphasizing the critical stakes of the upcoming election and the dangers posed by Donald Trump’s potential return to power.

3. **Katie Porter (California)**: Porter’s emails highlight her reputation for accountability and her refusal to accept corporate PAC money. Her campaign messages focus on social issues and the need for a fair economy.

4. **Other Democratic Campaigns**: Similar themes of urgency in fundraising and combating Republican policies, with an emphasis on maintaining or gaining Democratic control in various legislative bodies.

### Neutral/Non-Partisan Political Content
- Some emails discuss general political engagement and voter outreach without clear affiliation to a specific party. These messages typically focus on the mechanics of campaigning, such as fundraising and event announcements, without ideological emphasis.

### Evaluation
- The emails present a clear dichotomy between Republican and Democratic campaigns, both emphasizing the urgency of fundraising and ideological battles. Republican emails tend to focus on security, law enforcement, and critiques of media and current government policies, portraying a narrative of rescue and defense against perceived mismanagement by Democrats. Democratic emails highlight threats to social justice, healthcare, and environmental policies, positioning their campaigns as essential to protecting democracy and progressive values. Neutral political content serves to engage potential voters and supporters in the political process, often through informational updates and calls to action that stress the importance of participation in upcoming elections.

- This overview reflects a highly polarized political landscape where each party positions itself as crucial to correcting or sustaining the nation’s trajectory, appealing to their respective bases with tailored messages that underscore deep ideological divides.

### 3. What misinformation or conspiracy theories are different political parties pushing? 
Due to the fact that the big language model cannot directly extract information from links, we extracted information from all emails and identified the most frequently appearing links, and analyzed them.

### Example: 
- pjnewsletter.com, being shared 18 times,  is a news source with a notable right-wing bias. An email sharing a link to such websites can possibly be using misinformation strategies.

![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Top%2010%20Frequent%20Hostnames.png)
![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/misinfo.png)
![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Campaign%20vs.%20Non-Campaign%20Websites.png)

### 4. What is the sentiment of different campaigns (positive, negative, etc)? 
The activities of certain specific political figures often tend to be positive or negative, which is related to their campaign style, support rate, and political party they belong to.

![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Sentiment%20Analysis%20for%20Each%20Candidate.png)

![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Sentiment%20Analysis%20by%20Political%20Party.png)

### 5. What links are these campaigns sharing?
The vast majority of links are fundraising and news links initiated by candidates, and the following files contain links from all the emails we extracted.

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/data/final_data/links.txt


### 6. What other people do these emails reference (Donald Trump, Joe Biden, Hillary Clinton, etc)?
We extracted all the names mentioned in the emails and filtered out data that appeared less frequently, by political party.

![](https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/blob/main/deliverables/Total%20Mentions%20for%20Each%20Candidate%20by%20Party.png)

### 7. Do any of these questions change depending on how competitive the seat is?
States with closer seats tend to speak more aggressively, while those with clear advantages tend to speak more calmly.

Here are the emails we extract on a weekly basis and real-time updates on seat changes.

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/data/final_data/data_per_week.zip
https://www.realclearpolling.com/elections/president/2024/battleground-states

## Data Cleaning Methods with Links to the Files for Data Cleaning
### 1. Email extraction: 
extracting emails from a mailbox.

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/Data_preprocessing.py

### 2. Keyword extraction: 
Counting the number of occurrences of specified keywords from emails.

### Word frequency statistics: 
Count the N words with the highest frequency of occurrence.

### Word count: 
Counts the average word count of an email.

### Time extraction:
Extracting the collection time of emails.

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/Data_preprocessing.py

### 3. Summarize each email
The specific output is **subject/candidate name(attitude)[evaluation]\<relevant region>** for each email.

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/LLM_mid.py

### 4. Organize the keywords in the summary
Extract and place the frequency of each candidate's appearance, the frequency of related keywords, and the frequency of related attitudes in a file named after the person's name

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/Data_processing_mid.py

### 5. Extract link
Extract links that appear in emails

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/extract_links.py

### 6. Classify by time
Change the email name to the time it was received and archive the email in weeks

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/Data_Processing_final.py

## Data Analysis Methods with Links to the Files for Data Analysis

### Line charts, pie charts, and bar charts for analysis

The most meaningful words that appear

The most politically related words that appear

The number of emails received per day

The number of emails received per day of a week

The number of emails received at each time of the day

The number of times each candidate appears

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/plot_emails_summary.py


Top Keywords by State

Sentiment Analysis by Political Party

Campaign vs. Non Campaign Websites

Number of Candidates by Political Party

Total Mentions for Each Candidate by Party

Sentiment Analysis by Political Party

https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/code/chartsGeneration.ipynb

## Links to datasets

### Emails: 
https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/data/final_data/data.zip

## How to Run
#### All executable files are located in the code directory

Above all,  Run api_call.py to download all JSON files for emails.

#### Data_preprocessing.py: 

1. JSON file for emails required.
2. After running, obtain Average_words.txt; candidates_count.txt;  most_common_words.txt; emails_info.txt.
3. Analyse most_common_words.txt with GPT to find the top N meaningful words and the top N politically related words, and save them to Meaningful_words.txt and Political_words.txt, respectively.

#### LLM_mid.py: 

1. JSON file for emails required.
2. After running, obtain email_analysis_results_Number of candidate mentions.txt, a summary of each email for each line, and for each candidate, the output format is **subject/validate name (title) [evaluation]\<relevant region>**.

#### Data_processing_mid.py: 

1. email_analysis_results_Number of candidate mentions.txt required.
2. After running, extract and count the number of occurrences of each part separately by person name, and save it to the corresponding person name file.

#### Data_Processing_final.py: 

1. JSON file for emails required.
2. After running, all emails will be named after the collection time and merged on a weekly basis

#### extract_links.py: 

1. JSON file for emails required.
2. After running, obtain links.txt.

#### plot_emails_summary.py: 
1. Meaningful_words.txt, Political_words.txt, emails_info.txt, candidates_count.txt requied.
2. After running, obtain some bar charts, pie charts, and line charts for basic email information

#### chartsGeneration.ipynb: 
1. Txt file named after a person's name required.
2. After running, obtain visualizations of themes related to different political parties, etc..

#### Prompt for ChatGPT: 
1. Use this prompt to analyze emails merged on a weekly basis.
https://github.com/ziye2chen/Election-Narratives-through-Prompt-Engineering-with-GPT/tree/main/data/final_data/prompt_final.txt


## References

1. Gmail API: https://developers.google.com/gmail/api/guides
2. Open AI API: https://openai.com
3. Llama 2: https://mindformers.readthedocs.io/zh-cn/latest/docs/model_cards/llama2.html
4. Seats changes over time: https://www.realclearpolling.com/elections/president/2024/battleground-states

