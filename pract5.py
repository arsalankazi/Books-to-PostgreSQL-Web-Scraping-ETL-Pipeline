'''
Tasks:
1. .select() se dono h2 elements find karo.
2. .select() se dono prices find karo.
3. #p1 se first product find karo.
4. .product p se dono products ke paragraphs find karo.
5. .select_one() se first product ka price find karo.


'''



from bs4 import BeautifulSoup

html = """
<div class="product" id="p1">
    <h2>Samsung Phone</h2>
    <p class="price">₹15,000</p>
</div>

<div class="product" id="p2">
    <h2>iPhone</h2>
    <p class="price">₹60,000</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")


print("Both h2 elements:\n")
print(soup.select("h2"))

print("Both prices")
print(soup.select(".price"))       #it will give both prices in a list

print("First product")
print(soup.select("#p1"))  # we can do similar thing like this soup.find(id="p1") 

print(soup.select(".product p"))       #descendent selector
print(soup.select_one(".price"))

prices = (soup.select_one(".price"))
for price in prices:
    print("price.text")

