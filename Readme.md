Certainly! Below is your updated README incorporating the Data Preprocessing part:

# DevGPT Mining Challenge - MSR 2024

## Overview of the Mining Challenge

### Introduction
The DevGPT Mining Challenge for MSR 2024 aims to explore and analyze the interactions between developers and ChatGPT, as captured in the DevGPT dataset. This dataset comprises developer prompts and ChatGPT's responses, including code snippets, all related to software development. The dataset is paired with software development artifacts like source code, commits, and discussions. With the DevGPT dataset, researchers can analyze the context and implications of developer interactions with ChatGPT.

## Our Selected Challenge: Topic Analysis of Developer Interactions with ChatGPT

### Objective
Our project focuses on understanding the different topics discussed between developers and ChatGPT. We aim to find out what kind of questions developers ask and how ChatGPT responds to them. To do this, we will use data from the DevGPT dataset. This dataset contains a collection of conversations between developers and ChatGPT, which will help us in analyzing and understanding the common themes and topics discussed.

### Process
In the first part of the project, we will prepare the data for analysis. This means we will organize and clean the data, removing any parts that are not needed for our study. Next, we will use methods to find out what topics are most common in the conversations. We will sort the questions and answers into different groups based on what they are about.

Finally, we will study the results to better understand what developers are most interested in when they talk to ChatGPT. We will create visual reports to make it easy to see what the most common topics are.


Certainly! Here’s the revised “Dataset Maintenance Script” section, rewritten for consistency with the “Data Preprocessing” section:

### Data Preprocessing

Data preprocessing is a crucial part of our project, ensuring that the data is cleaned and formatted correctly to facilitate accurate and efficient analysis. Here is a walkthrough of our preprocessing steps as encapsulated in our script:

- **Code Removal**:
   - Our script is currently designed to have a placeholder for code removal. This will be essential to ensure that non-textual code elements do not interfere with our text analysis.

- **Language Filtering**:
   - The script employs language detection to ensure that the analyzed text is in English. Texts detected as non-English are filtered out to maintain language consistency within the dataset.

- **Text Cleaning**:
   - Non-English Characters: Removal of characters that fall outside the conventional English alphanumeric characters and punctuation.
   - HTML Tags: Stripping the text of HTML tags to leave only the raw textual content.
   - URL Removal: Extracting and removing URLs from the text.
   - Placeholder and Extra Strings: The removal of specific placeholder strings and additional textual elements like “Used unknown plugin”, “Finished browsing”, etc.
   - English Verification: Ensuring that the cleaned text is valid and non-empty English text.

- **Data Extraction and Storage**:
   - Reading Data: The script reads from a specific JSON file and iteratively processes the contents.
   - Unique URL Checking: To avoid duplicate processing, the script ensures each URL is uniquely processed.
   - Text Extraction: Prompts and responses are extracted, cleaned, and stored if they pass the cleaning criteria.
   - JSON Output: Cleaned and preprocessed data are stored in a JSON file for subsequent use in analysis.

The details and actual code of the Dataset Maintenance Script are housed within the `update_database.py` file in this repository. 

### Data Preprocessing

We have a designated data preprocessing script to ensure the dataset is cleaned and formatted correctly for analysis. The script performs various tasks such as:

- **Text Cleaning**: Removing code segments, HTML tags, URLs, and specific unwanted strings from the text.
- **Data Extraction**: Extracting necessary information, such as issue statuses and interactions with ChatGPT.
- **Unique URL Processing**: Making sure each URL in the dataset is processed only once to maintain uniqueness.
- **Output Preparation**: Saving the cleaned and pre-processed data into a new JSON file for further analysis.

The details and the code for the data preprocessing can be found within the `data_preprocessing.py` file in this repository.
