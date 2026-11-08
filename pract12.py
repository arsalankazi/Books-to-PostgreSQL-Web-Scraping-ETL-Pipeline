'''
requests import karo.
BeautifulSoup import karo.
Website URL variable mein store karo.
requests.get() se page download karo.
raise_for_status() se HTTP error check karo.
BeautifulSoup se HTML parse karo.
.select("article.product_pod") se book containers find karo.
len() se total books count karo.
'''

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/?utm_source=chatgpt.com"

try:

    response = requests.get(url, timeout = 15)                # you timeout missed
    print("Response code is:",response.status_code)
    response.raise_for_status()                               # you missed ()
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    books = soup.select(".product_pod")
    No_of_books =len(books) 
    print("Total books are:",No_of_books)


except requests.exceptions.Timeout:
    print("site is taking too much time")

except requests.exceptions.RequestException as e:      # forgot to write as e
    print("something went wrong",e) 















