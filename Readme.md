# DevGPT Mining Challenge - MSR 2024

## Overview of the Mining Challenge

DevGPT Mining Challenge - MSR 2024
Introduction
The DevGPT Mining Challenge for MSR 2024 aims to explore and analyze the interactions between developers and ChatGPT, as captured in the DevGPT dataset. This dataset comprises developer prompts and ChatGPT's responses, including code snippets, all related to software development. The dataset is paired with software development artifacts like source code, commits, and discussions. With the DevGPT dataset, researchers can analyze the context and implications of developer interactions with ChatGPT.

## Our Selected Challenge: Identifying Prompt Patterns
We have chosen to address the following research question:

> **Can we identify patterns in the prompts developers use when interacting with ChatGPT, and do these patterns correlate with the success of issue resolution?**

In this challenge, to put it simply, we aim to: 

1. Identify common or recurring patterns in the way developers phrase their questions or problems when consulting ChatGPT.
2. Check if these patterns are linked with successful issue resolutions.

This insight can help improve the interaction between developers and ChatGPT, leading to more efficient problem-solving.

### Dataset Maintenance Script:

To ensure we always work with the latest data, we have a script in place that regularly updates the DevGPT dataset. Here's a brief overview of the script:

- **What It Does**: The script checks if we already have a local copy of the DevGPT dataset. If it exists, the script updates it with the latest changes. If not, it clones the entire repository.
- **Configuration**: We have set up the repository URL (`DEVGPT_REPO_URL`) and the local directory where the data should reside (`CLONE_DIR`).
- **Running Commands**: A helper function (`run_command`) allows us to run shell commands, whether it's for cloning the repository or updating it.
- **Clone or Update**: The main logic checks if the directory (`CLONE_DIR`) exists. If it does, the script pulls the latest changes. Otherwise, it clones the entire repository.

To use the dataset maintenance script please see the file `update_database.py` in this repository.

---

We look forward to sharing our findings and contributing to the understanding of developer interactions with ChatGPT. If you have any questions or wish to collaborate, feel free to reach out!
