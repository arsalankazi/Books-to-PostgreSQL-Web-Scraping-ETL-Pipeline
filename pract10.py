'''Pagination ka logic:
1. Current page download karo.
2. Us page se books extract karo.
3. Next button ka URL find karo.
4. Next page par jao.
5. Jab Next button nahi mile, scraping stop kar do.

1. BeautifulSoup object banana hai.
2. Next link select karna hai.
3. href extract karna hai.
4. urljoin() se absolute URL banana hai.
5. Print karna hai.
Expected output:
https://example.com/catalogue/page-2.html
'''

from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = """
<div class="pagination">
    <a href="page-2.html">Next</a>
</div>
"""
soup = BeautifulSoup(html,"html.parser")
base_url ="https://example.com/catalogue/page-1.html"

anchor = soup.select_one(".pagination a")
link = anchor.get("href")
next_button = urljoin(base_url,link)
print(next_button)

    



















