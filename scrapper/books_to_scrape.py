import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
def scrape_books():
    response = requests.get(url)
    response.status_code
    
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    #books=soup.find_all('div',class_= 'book')
    book_data=[]
    for book in books:
        #title= book.find('p',class_='title').get_text(strip=True)
        title = book.find("h3").find("a")["title"]
        #author=book.find('p',class_='author').get_text(strip=True)
        #price=book.find('p',class_='price').get_text(strip=True)
        #price = book.find("p", class_="price_color").get_text(strip=True)
        price = book.find("p", class_="price_color").text.strip()
        #publication_year = book.find('p',class_='publication-year').get_text(strip = True)
        #genre=book.find('p',class_='genre').get_text(strip=True)
        #description=book.find('p',class_='description').get_text(strip=True)
        rating = book.find("p", class_="star-rating")["class"][1]
        book_data.append({
        'Title' : title,
        #'author' : author,
        'Price' : price,
        'Rating' : rating,
        #'publication year' : publication_year,
        #'Genre' : genre,
        #'Description' : description
    })
    return book_data
