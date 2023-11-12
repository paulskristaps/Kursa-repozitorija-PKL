import os
import yaml
import requests

print("Checking if config file exists...")
assert os.path.isfile("Webscraper/logging_config.yaml") == True
print("Everything OK!")

#Pārbauda vai filename parametrs ir konfigurācijas failā
with open("Webscraper/logging_config.yaml", 'r') as file:
    config_data = yaml.safe_load(file)
assert 'filename' in config_data.get('handlers', {}).get('file', {}), "Filename parameter does not exist in config"

print("Checking if webscraped data collecting file exists...")
assert os.path.isfile("Webscraper/Bestselling items.txt") == True
print("Everything OK!")

#Pārbauda vai savienojums ar amazon.com ir veiksmīgs
headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
page = "https://www.amazon.com/gp/bestsellers?&linkCode=sl2&tag=pandatech02-20&linkId=a45d9b9261d98350ed2ae157280272e1&language=en_US&ref_=as_li_ss_tl"
response = requests.get(page, headers=headers)

assert response.status_code == 200

