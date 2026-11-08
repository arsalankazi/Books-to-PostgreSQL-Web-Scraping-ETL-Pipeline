'''
1. Adjacent sibling selector +
soup.select(".price + .brand")

OP: <p class="brand">Dell</p>
Meaning: .price ke immediately baad aane wala .brand element.

General sibling selector ~
soup.select(".price ~ p")
op: <p class="brand">Dell</p>
    <p class="ram">16GB</p>
Meaning: .price ke baad aane wale saare sibling paragraphs.
-----------------------------------------------------------
-----------------------------------------------------------

practice:

.course ke immediately baad wala paragraph select karne ka selector?
.course ke baad ke saare paragraphs select karne ka selector?

'''

from bs4 import BeautifulSoup
HTML = """
<div class="student">
    <h2>Arsalan</h2>
    <p class="course">MCA</p>
    <p class="college">University</p>
    <p class="city">Shirpur</p>
</div>
"""

soup = BeautifulSoup(HTML,"html.parser")
print(soup.select(".course + p"))
print(soup.select(".course ~ p"))


for item in soup.select(".course + p"): 
    print(item.get_text(strip=True))

for item in soup.select(".course ~ p"):
    print(item.get_text(strip=True))


