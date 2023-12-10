# DevGPT Mining Challenge - MSR 2024

## Overview of the Mining Challenge

### Introduction
The DevGPT Mining Challenge for MSR 2024 aims to explore and analyze the interactions between developers and ChatGPT, as captured in the DevGPT dataset. This dataset comprises developer prompts and ChatGPT's responses, including code snippets, all related to software development. The dataset is paired with software development artifacts like source code, commits, and discussions. With the DevGPT dataset, researchers can analyze the context and implications of developer interactions with ChatGPT.

## Our Selected Challenge: Topic Analysis of Developer Interactions with ChatGPT

### Objective
Our project focuses on understanding the different topics discussed between developers and ChatGPT. To do this, we will use data from the DevGPT dataset. This dataset contains a collection of conversations between developers and ChatGPT, which will help us in analyzing and understanding the common themes and topics discussed.

### Process
In the first part of the project, we will prepare the data for analysis. This means we will organize and clean the data, removing any parts that are not needed for our study. Next, we will use methods to find out what topics are most common in the conversations. We will sort the questions and answers into different groups based on what they are about.

Finally, we will study the results to better understand what developers are most interested in when they talk to ChatGPT. We will create visual reports to make it easy to see what the most common topics are.

### Data Preprocessing

We have a designated data preprocessing script to ensure the dataset is cleaned and formatted correctly for analysis. The script performs various tasks such as:

- **Text Cleaning**: Removing code segments, HTML tags, URLs, and specific unwanted strings from the text.
- **Data Extraction**: Extracting necessary information, such as issue statuses and interactions with ChatGPT.
- **Unique URL Processing**: Making sure each URL in the dataset is processed only once to maintain uniqueness.
- **Output Preparation**: Saving the cleaned and pre-processed data into a new JSON file for further analysis.

The details and the code for the data preprocessing can be found within the `data_preprocessing.py` file in this repository.
