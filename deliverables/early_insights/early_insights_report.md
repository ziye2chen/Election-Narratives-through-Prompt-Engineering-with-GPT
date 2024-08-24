# Early Insights Report
### Data Collection and Pre-processing
* **Data Collection** We've retrieved all email messages by using Gmail API and the code has been pushed to the Github repo.  
* **Data Pre-processing** Since the raw data for our project is human language, there's not much work to do for data cleaning and pre-processing. We just removed the icons and special characters from the text.  

### Data Analysis
* **the Scale of Data** In our preliminary investigation, we analyzed a collection of 500 emails to gain an initial understanding relevant to our research objectives.
  
* **Analysis on the Length of Emails** This analysis revealed that the average email length within this batch is roughly 325.8 words. Such a finding is crucial for guiding our future choice of language processing tools, ensuring they are well-suited to manage the dataset's intricacy and size efficiently.  
* **Analysis on the Content of Emails** Additionally, we have carefully extracted the names of individuals mentioned and pinpointed the most frequently occurring terms, for example, names and words. This frequency analysis provided us with a deeper insight into the dominant topics and concerns prevalent during this election cycle. Not surprisingly, the most frequent names appealing in these emails are "Donald Trump" and "Joe Biden". However, there are still some other names showing up, such as "Dean Phillips" and "Haley Nikki".  
![Candidates Count](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/a68d2a86-69fe-4ace-ad09-1bd940475e3b)
![Most Common Words](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/c61a5536-0638-489a-a378-d524003423e9)
![Most Common Political Words](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/9cc209e7-6c66-4bdd-9fc2-344151f5bb70)
![Number of Emails Received Per Day](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/f55d9ef3-a9fa-42fb-99ba-b9a02f967e19)
![Number of Emails Received Per Hour](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/cca1d72f-6589-4e06-9dab-18fa710a9a9a)
![Distribution of Emails by Day of the Week](https://github.com/BU-Spark/ds-donovan-election-narratives/assets/143741813/582452ac-f06d-4f6f-ae97-d52fad098107)


By doing these analyses, we not only deepen our understanding of the dataset's thematic elements but also refine our methodological framework for subsequent data analysis and interpretation. This enriched understanding aids in tailoring our analytical strategies more precisely to uncover underlying patterns and insights within the data, thereby enhancing the overall effectiveness of our research endeavors.  

### Questions with the Data
When conducting an analysis of emails related to this year's U.S. presidential election, the scope of questions that can and cannot be answered depends on the type, range, quality, and detail of the data at hand. Here are examples based on common data types and analytical approaches:  
* **Questions that can be answered:**  

1. Email Sending Frequency: Analyze the timing and frequency of email dispatches, such as daily, weekly, or around specific events.

2. Topic Analysis: Identify the most common topics or subjects within the emails and how these topics evolve over time.

3. Sentiment Analysis: Assess the sentiment of the email content, such as positive, negative, or neutral, and differences in sentiment across different candidates or issues.

4. Use of Keywords and Phrases: Analyze the frequency and context of specific keywords and phrases used in the emails across different candidates or issues.

5. Audience Targeting: Analyze the intended audience based on the content and style of the emails, such as age, geographic location, or political leaning.

6. Engagement Rate Analysis: If data includes user interactions (like open rates, click-through rates, etc.), analyze which types of emails engage the audience more effectively.  

* **Questions that cannot be answered:**  

1. Actual Voting Intentions: Email analysis cannot directly predict the actual voting behavior of individuals, as many other factors can influence the final decision.

2. Detailed Voter Information: Without detailed personal information in the data, it's impossible to analyze specific voter profiles or behavior patterns.

3. Impact on Social Media: Without data on social media interactions, email analysis cannot gauge the sentiment or influence on social media platforms.

4. Effectiveness of Non-digital Communications: Email analysis cannot measure the impact of face-to-face communications, phone calls, or other non-digital communication methods.

5. Overall Effectiveness of Campaign Strategies: Emails are only part of campaign strategies; email analysis alone cannot fully evaluate the effectiveness or impact of an overall campaign strategy.  

In summary, email analysis can provide insights into campaign communication strategies, audience reactions, and content trends, but its capabilities are limited. It should be combined with other data and analytical methods to gain a more comprehensive understanding.

### Other Data Needed
* **Election Analysis from other Resources**  
This information is indeed crucial to ensure the completeness and accuracy of our analysis results. Given the dataset's manageable size (thousands of emails), there's a possibility that our models and analytical methods might seem effective for this particular dataset but fail to reveal broader trends. This highlights the importance of ensuring our analysis is robust and reflective of wider patterns, not just tailored to fit the specific characteristics of the data at hand.  
* **Weights on Different Medias**  
The accuracy and trustworthiness of our data sources, specifically various media outlets, exhibit significant variation. Therefore, assigning a precise weight to each media source and integrating these weights into our model's metrics would be advantageous. This approach will enhance the model's effectiveness by accounting for the varying degrees of reliability across different sources.
