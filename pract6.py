'''
Task 1: .product ke andar saare paragraphs select karo.

Task 2: .product ke direct child paragraphs select karo.

Task 3: .details ke direct child paragraphs select karo.

Task 4: .product ke direct child div select karo
'''



from bs4 import BeautifulSoup

html = """
<div class="product">

    <h2>Laptop</h2>

    <p class="price">₹50000</p>

    <div class="details">
        <p>Brand: Dell</p>
        <p>RAM: 16GB</p>
    </div>

</div>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.select(".product p"))
print(soup.select(".product > p"))
print(soup.select(".details p"))
print(soup.select(".product > div"))


# if we want to print onnly text 
result = soup.select(".product p")

for item in result:
    print(item.get_text())


'''
soup.select() matching HTML elements return karta hai.
for item in result ek-ek element par loop chalata hai.
item.get_text() HTML tags hata kar andar ka text return karta hai.
'''

# onlu give text of one element
price = soup.select_one(".price")

print(price.get_text())





