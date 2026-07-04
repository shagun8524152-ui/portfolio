import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.amazon.in/s?k=laptop&crid=YLH7SZQM1WE6&sprefix=laptop%2Caps%2C610&ref=nb_sb_noss_2"
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.google.com/'
}
def scrap_laptops():

    response = requests.get(url,headers=headers)
    response.status_code
    soup=BeautifulSoup(response.content,"html.parser")
    laptops = soup.find_all('div',class_='s-result-item')
    laptop_data=[]
    for laptop in laptops :
        title = laptop.find('h2', class_='a-size-medium a-spacing-none a-color-base a-text-normal')
        title = title.get_text(strip=True) if title else "N/A"

        price = laptop.find('span', class_='a-price-whole')
        price = price.get_text(strip=True) if price else "N/A"

        rating = laptop.find('span', class_='a-icon-alt')
        rating = rating.get_text(strip=True) if rating else "N/A"
        
    
        laptop_data.append(
        {
        'Title': title,
       'Price': price,
        'Rating': rating,
}
)
    return laptop_data
