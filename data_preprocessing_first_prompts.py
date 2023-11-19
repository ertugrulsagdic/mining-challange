import json
import re
from bs4 import BeautifulSoup
from langdetect import detect 
import re
import string
from collections import Counter
import os
# import openai

# openai.api_base = "http://localhost:1234/v1" # point to the local server
# openai.api_key = "" # no need for an API key

# plaintext_extraction_prompt = ("Remove all the code or programming language elements in this string without changing any other word. If you do not detect any code or programming language elements, do not change the string. Then, return only the processed string\\n\\n")

# def remove_code(text):
#     # TODO: add code cleaning API
    
#     prompt_with_text_extraction = plaintext_extraction_prompt + text

#     completion = openai.ChatCompletion.create(
#     model="local-model", # this field is currently unused
#     messages=[
#             {"role": "system", "content": "Remove Code"},
#             {"role": "user", "content": prompt_with_text_extraction}
#         ],
#     )
    
#     print('############################TEXT#############################')
#     print(text)
#     new_text = completion.choices[0].message['content']
#     print('############################NEW TEXT#############################')
#     print(new_text)
#     print()

#     return new_text

def is_english(text, times=3):
    detections = []
    for _ in range(times):
        try:
            language = detect(text)
            detections.append(language)
        except Exception as e:
            return ''
    
    most_common_language, _ = Counter(detections).most_common(1)[0]
    if most_common_language == 'en':
        return text
    else:
        return ''

def clean_text(text):

    # remove all between ''' ''' or """ """ or ``` ```
    cleaned_text = re.sub(r"'''[\s\S]*?'''", "", text)
    cleaned_text = re.sub(r'"""[\s\S]*?"""', "", cleaned_text)
    cleaned_text = re.sub(r"```[\s\S]*?```", "", cleaned_text)

    # remove the string that has # Working set in it
    if re.search(r"# Working set", cleaned_text) is not None:
        return ""

    # # Removing non english characters
    # cleaned_text = re.sub(fr"[^a-zA-Z0-9 {string.punctuation}]+", " ", text)
    
    # Removing HTML tags
    cleaned_text = re.sub(r"<[^>]+>", "", cleaned_text)
    
    # Removing URLs
    cleaned_text = re.sub(r"http\S+|www\S+", "", cleaned_text)

    # remove "Used unknown plugin" string
    cleaned_text = re.sub(r"Used unknown plugin", "", cleaned_text)

    # remove "Finished browsing" string
    cleaned_text = re.sub(r"Finished browsing", "", cleaned_text)

    # remove "Finished working" string
    cleaned_text = re.sub(r"Finished working", "", cleaned_text)

    # remove "Show work"
    cleaned_text = re.sub(r"Show work", "", cleaned_text)

    # remove "Hide work"
    cleaned_text = re.sub(r"Hide work", "", cleaned_text)

    cleaned_text = re.sub(r"\[CODE_BLOCK_\d+\]", " ", cleaned_text)

    if cleaned_text == " " or cleaned_text == "":
        return ""

    cleaned_text = is_english(cleaned_text)

    if cleaned_text == " " or cleaned_text == "":
        return ""

    # cleaned_text = remove_code(cleaned_text)

    
    # check if fr"[^a-zA-Z0-9 {string.punctuation}]+" exists in text
    if re.search(fr"[^a-zA-Z0-9\s{string.punctuation}\\·–—…“”’∗]+", text) is not None:
        # print('#########################################################')
        # # print the captured group
        # print(string.punctuation)
        # print(re.search(fr"[^a-zA-Z0-9\s{string.punctuation}\\·—–…“”’∗]+", text))
        # print('#########################################################')
        # print(text)
        # # wait for user input
        # input()
        # print('#########################################################')
        # print('#########################################################')
        # print('#########################################################')
        # print('#########################################################')
        return ""

    
    return cleaned_text

pre_processed_data = []

# data_without_html = []
unique_urls = {}


path = "./DevGPT/snapshot_20231012/"
files = os.listdir(path)


total = 0
all_total = 0

for file in files:

    if 'hn_sharings' in file or 'ChatGPT_Link_Sharing.csv' in file:
        continue

    with open(path + file) as f:
        data = json.load(f)

        sources = data["Sources"]

        for s in sources:

            for gptsharing in s["ChatgptSharing"]:

                if "HTMLContent" not in gptsharing:
                    # print(gptsharing["Status"])
                    continue
                
                url = gptsharing["URL"]

                if url in unique_urls:
                    continue

                unique_urls[url] = 1

                soup = BeautifulSoup(gptsharing["HTMLContent"], 'html.parser')

                prompt_element = soup.find('div', class_="relative flex w-[calc(100%-50px)] flex-col gizmo:w-full lg:w-[calc(100%-115px)] gizmo:text-gizmo-gray-600 gizmo:dark:text-gray-300")

                if prompt_element is None:
                    continue

                all_total += 1

                prompt_text = clean_text(prompt_element.get_text())

                if prompt_text != "" and prompt_text != " ":
                    pre_processed_data.append(prompt_text)
                    total += 1
                        
                
        f.close()

print("Total: ", total)

# write pre_processed_data to file
with open("./pre_processed_data_non_english_removed.json", "w") as outfile:
    json.dump(pre_processed_data, outfile, indent=4)
