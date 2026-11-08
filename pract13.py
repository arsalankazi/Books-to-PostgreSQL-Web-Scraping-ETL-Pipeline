"""

one book data extract

A. Book title
simply website par jana aur book title par right click karna wo direct tag par le jata. wo tag ku extract karna
title = book.select_one("h3 a") aur us tag ke andar dekhna ki title kisme hai. text me hai means > yaha < ya koi attribute me hai. yaha title name ke 
attribute me thi to hamne .get("title") kare
HTML:
<a title="A Light in the Attic">A Light in the ...</a>


Code:
title = book.select_one("h3 a").get("title")



get("title") attribute ki value deta hai, jo full title hai.

B. Price
<p class="price_color">£51.77</p>

yaha bhi same karna. tag extract price = book.select_one(".price_color") and variable me store aur yaha text me tha
to get_text() kare

Code:
price = book.select_one(".price_color").get_text(strip=True)



C. Rating

HTML:
<p class="star-rating Three">


Yahan Three text nahi hai. Ye CSS class hai.

Code:
rating_tag = book.select_one(".star-rating")
rating = rating_tag.get("class")[-1]



Output:
Three


get("class") list return karega:
['star-rating', 'Three']



[-1] last item select karega.

D. Product URL

yaha bhi same hai . yaha url href attribute me tha to hamne .get("href") kiye
HTML:
<a href="catalogue/book.html">


Code:
link_tag = book.select_one("h3 a")
product_url = link_tag.get("href")



Complete URL chahiye toh:
from urllib.parse import urljoinproduct_url = urljoin(url, product_url)"""



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

try:

    response = requests.get(url, timeout = 15)                # you missed timeout
    print("Response code is:",response.status_code)
    response.raise_for_status()                               # you missed ()
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    books = soup.select(".product_pod")

    book = books[0]

    Book_Title = book.select_one("h3 a").get("title")
    price_tag = book.select_one(".price_color").get_text(strip= True)
    rating_tag= book.select_one(".star-rating")
    rating=rating_tag.get("class")[-1]
    product_url = book.select_one("h3 a").get("href")
    URL = urljoin(url,product_url)



    print("Title:",Book_Title)
    print("Cost:",price_tag)
    print("Rating:",rating)
    print("URL",URL)


except requests.exceptions.Timeout:
    print("site is taking too much time")

except requests.exceptions.RequestException as e:      # forgot to write as e
    print("something went wrong",e) 