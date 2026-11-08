'''
.price element ka parent print karo.
.book ke direct children print karo.
.book ke descendants print karo.
.price ka next sibling element find karo.
.rating ka previous sibling element find kar

'''

from bs4 import BeautifulSoup
html = html = """
<div class="book">
    <h2>Python</h2>
    <p class="price">500</p>
    <p class="author">John</p>
    <p class="rating">5 Stars</p>
</div>
"""
soup = BeautifulSoup(html,"html.parser")
price = soup.select_one(".price")
print("",price)

children = soup.select_one(".book")

for child in children :
    print(child)

print("-----------------------------------")
for item in children.descendants :
    print(item)

print(price.find_next_sibling())            # dont forget to write ()

rating = soup.select_one(".rating")
print(rating.find_previous_sibling())       # dont forget to write ()






