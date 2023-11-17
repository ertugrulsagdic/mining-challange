import json
import re
from bs4 import BeautifulSoup
from langdetect import detect 
import re
import string
from collections import Counter

def remove_code(text):
    # TODO: add code cleaning API
    return text

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

    cleaned_text = remove_code(text)

    # Removing non english characters
    cleaned_text = re.sub(fr"[^a-zA-Z0-9 {string.punctuation}]+", " ", text)
    
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
    
    return cleaned_text

pre_processed_data = []

# data_without_html = []
unique_urls = {}

with open("./DevGPT/snapshot_20231012/20231012_235128_issue_sharings.json") as f:
    data = json.load(f)

    sources = data["Sources"]

    closed_issues = 0
    open_issues = 0
    total = 0
    for s in sources:
        
        state = s["State"]
        if state == "OPEN":
            open_issues += 1
        else:
            closed_issues += 1


        for gptsharing in s["ChatgptSharing"]:

            if "HTMLContent" not in gptsharing:
                # print(gptsharing["Status"])
                continue
            
            url = gptsharing["URL"]

            if url in unique_urls:
                continue

            unique_urls[url] = 1

            soup = BeautifulSoup(gptsharing["HTMLContent"], 'html.parser')

            prompt_elements = soup.find_all('div', class_="relative flex w-[calc(100%-50px)] flex-col gizmo:w-full lg:w-[calc(100%-115px)] gizmo:text-gizmo-gray-600 gizmo:dark:text-gray-300")
            answer_elemets = soup.find_all("div", class_=re.compile('.*agent-turn.*'))
            
            if len(prompt_elements) != len(answer_elemets):
                print("ERROR: ", url)
                print()
                continue
            
            for i in range(len(answer_elemets)):
                prompt_text = clean_text(prompt_elements[i].get_text())
                if prompt_text != "" and prompt_text != " ":
                    pre_processed_data.append(prompt_text)
                    total += 1
                    
                answer_text = clean_text(answer_elemets[i].get_text())
                if answer_text != "" and  answer_text != " ":
                    pre_processed_data.append(answer_text)
                    total += 1
            
    f.close()

    print()
    print("Open: ", open_issues)
    print("Closed_issues: ", closed_issues)
    print("Total: ", total)

# write pre_processed_data to file
with open("./pre_processed_data.json", "w") as outfile:
    json.dump(pre_processed_data, outfile, indent=4)
