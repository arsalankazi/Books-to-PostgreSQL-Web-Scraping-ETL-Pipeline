'''
1. BeautifulSoup object banana hai.
2. Saare <a> tags find karne hain.
3. Har link ka title extract karna hai.
4. Har link ka href extract karna hai.
5. urljoin() se complete URL banana hai.
6. Title aur complete URL print karna hai.
Base URL:
base_url = "https://books.toscrape.com/"



Expected output:
Python Book
https://books.toscrape.com/catalogue/python.html

Java Book
https://books.toscrape.com/catalogue/java.html

SQL Book
https://books.toscrape.com/catalogue/sql.html

'''

from bs4 import BeautifulSoup
from urllib.parse import urljoin              # two url ko join karta hai 
base_url = "https://books.toscrape.com/"
html = """
<div class="books">

    <a href="catalogue/python.html">Python Book</a>

    <a href="catalogue/java.html">Java Book</a>

    <a href="catalogue/sql.html">SQL Book</a>

</div>
"""
soup =  BeautifulSoup(html,"html.parser")    # beautifulsoup object banaya
  
links = soup.select(".books a") # css selector se sare anchor tags extract kiye and store kiye links variable me in the form of list

for link in links:              # iterable(means list ) ke har item par operation karege with the help of loop 

    rel_url = link.get("href")            # sab rel url nikale means jo tag me likhe huwe the
    new_url = urljoin(base_url,rel_url)   # urljoin se join kardiye har rel url ko base url se
                                          # urljoin() relative URL ko current base URL ke saath combine karta hai.
    print(link.get_text(strip=True))      # har ek anchor tag ka text extract kiya 
    print(new_url)                        # new absolute url paste kiye











