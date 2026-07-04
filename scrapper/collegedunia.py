import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://collegedunia.com"
headers={ "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64 ; x64) appleWebKit/537.36 (KHTML ,Like Gecko Chrome/91.0.4472.124 Safari/537.36"}


def scrap_colleges():
    response = requests.get(url , headers = headers)
    response.status_code
    html_code = response.text
    soup = BeautifulSoup(html_code, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    information = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3: 
             Rank= cols[0].get_text(strip=True) 
             college_name= cols[1].get_text(strip=True)
             ranking = cols[2].get_text(strip=True)
            
             information.append({
                "Rank": Rank,
                "College_Name": college_name,
                "Ranking": ranking
            })
    return information