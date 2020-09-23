import pandas as pd
from time import sleep
import requests
from bs4 import BeautifulSoup

df = pd.read_csv("../assets/data/df-clean.csv")
df.drop(columns="Unnamed: 0", inplace=True)

# Organize each dot_number with url for scrape tool
url_list = []

for dot_number in df["DOT_NUMBER"]:
    url_dict = {}
    url = f"https://ai.fmcsa.dot.gov/SMS/Carrier/{dot_number}/CarrierRegistration.aspx"
    url_dict = {dot_number: url}
    url_list.append(url_dict)

# Check the request response
    # This can be used to check any 400 or 500 issues
for carrier in url_list[:2]:
    for url in carrier.values():
        sleep(60.0)
        res = requests.get(url)
        print(res)

#print(url_list[0].values())

"""
HTML tag order of Cargo Carried:
    1) <body>
    2) <div id="page-wrapper">
    3) <div id="page" class="container">
    4) <article id="regInfo" class="carrier-data eventPnl">
    5) <div class="modelBody">
    6) <div id ="regBox">
    7) <ul class="cargo">
    8) Then <li class> or <li class="checked">
    9) With text X for check
"""



