import json
from bs4 import BeautifulSoup
import re

with open("./DevGPT/snapshot_20231012/20231012_235128_issue_sharings.json") as f:
    data = json.load(f)

    sources = data["Sources"]

    closed = 0
    open = 0
    total = 0
    for s in sources:
        
        state = s["State"]
        if state == "OPEN":
            open += 1
        else:
            closed += 1

        for gptsharing in s["ChatgptSharing"]:

            if "HTMLContent" not in gptsharing:
                print(gptsharing["Status"])
                continue

            pattern = r'<div class="">(.*?)<\/div>'

            div_elements = re.findall(pattern, gptsharing["HTMLContent"], re.DOTALL)

            for i in range(len(div_elements)):
                div = div_elements[i]
                # if gptsharing["URL"] == "https://chat.openai.com/share/bc62c60f-245f-4d72-9ccd-fd5938e53a65":
                if gptsharing["URL"] == "https://chat.openai.com/share/b508ddd3-af83-4206-89fe-bb55b88ec212":
                    if i < len(gptsharing['Conversations']):
                        print(gptsharing['Conversations'][i]["Prompt"])
                        print("############################")
                    print(div)
                    print()
                total += 1

            # if "Conversations" in gptsharing:
            #     total += len(gptsharing["Conversations"])

    print()
    print("Open: ", open)
    print("Closed: ", closed)
    
    print()
    print(total)
    print(len(sources))