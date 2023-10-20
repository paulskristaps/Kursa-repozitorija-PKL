from bs4 import BeautifulSoup
import requests

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

# Ja rāda 'failed to fetch the page', palaist velreiz

page = "https://www.amazon.com/gp/bestsellers?&linkCode=sl2&tag=pandatech02-20&linkId=a45d9b9261d98350ed2ae157280272e1&language=en_US&ref_=as_li_ss_tl"
response = requests.get(page, headers=headers)
if response.status_code == 200:
    html = response.text
    doc = BeautifulSoup(html, "lxml")

    rows = doc.findAll('a', class_='a-link-normal')

    print("----- AMAZON BEST SELLING ITEMS -----")

    # Izprintē visu, kas web scrapots
    
    for row in rows:
        if len(row.text) == 0:
            continue
        print(row.text + "\n")


    # Raksta web-scrapoto contentu uz jaunu failu

    with open('Bestselling items.txt', 'w', encoding='utf-8') as file:
        file.write("\nAmazon BEST SELLING ITEMS \n")
        for row in rows:
            if row.text == "See More":
                continue
            file.write(row.text + "\n")
        
        print("New file created with scraped information!")
else:
    print("failed to fetch the page")