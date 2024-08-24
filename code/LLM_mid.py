import os
import json
from openai import OpenAI

'''
This file is based on OpenAi's gpt-4-turbo model.
Through specific prompts, the model strictly analyzes emails in the context of email analysis according to the format. 
The specific output is subject/candidate name (attitude) [evaluation]<relevant region>, 
and the difficulty in subsequent data analysis work caused by inconsistent GPT output format is minimized as much as possible.
'''


# Set OpenAI API key
Client = OpenAI(api_key='') # Your API

def condense_email(email_text):
    prompt = f"Analyze the following email and answer the questions:\n{email_text}\n---\n" \
             f"Question.1: Please provide the theme of this article in no more than three independent words(Only provide words, Separate each word with a comma) (The theme should not be emotions or attitudes, which will be raised in the second question).\n " \
             f"Question.2: This article mainly involves which candidates(Just need the full name, without any other modifiers and separate names with comma), what is the attitude towards each candidate, and is this attitude neutral, negative, or positive? Is there any relevant state? " \
             f"The format of your answer is as follows: full name of candidate (attitude or emotion, provide this in no more than three independent words) [neutral, negative or positive]<related state>. The three answers should be placed separately in (), [], and<>." \
             f"Here are some requirements for your answer: Independent words refer to words that should not be combined into phrases, and they all have specific meanings. Do not use phrases. " \
             f"If there are no results for any answer, please skip. " \
             f"If this email is unrecognizable or unrelated to the campaign, simply output error without answering any questions. " \
             f"Use/to separate the answers betweed question.1 and question.2."
    response = Client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=1000,
    )
    email_analysis = response.choices[0].message.content
    return email_analysis

# Specify the folder containing your email JSON files
folder_path = ''

# Specify the path for the output text file
output_file_path = ''

# Open the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Iterate over all files in the folder
    for i in range (1,2444):
        # Construct the full file path
        file_path = folder_path + 'email_' + str(i) + '.json'
        # Load and analyze the email
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            body_content = data['body']
            result = condense_email(body_content)
            # Write the result to the output file
            output_file.write(f"{result}\n")

print("Analysis complete. Results saved to", output_file_path)
