'''
.text, .string aur .get()

.text and .string are attributes bcz they do not have()
.get() is method bcz it have ()


1. Real-life example
Socho ek gift box hai.
- Box ka outer cover = HTML tag
- Box ke andar gift = Text/content
- Box ke label par likhi information = Attribute

Example:
<p class="book-price">₹300</p>


Ismein:
- <p> = Box
- class="book-price" = Label
- ₹300 = Box ke andar ka content
Ab humein sirf gift chahiye, yaani ₹300.

.get attributes print karne ke liye 
.text inside text print karne ke liye

'''




from bs4 import BeautifulSoup 

html = """

<div id="book1" class="book featured">
    <h2>Python Programming</h2>
    <p class="price">₹500</p>
</div>

"""
soup = BeautifulSoup (html,"html.parser")  # this will take the html content and parse it means understand its structure

container = soup.find("div")              # .find() will find first div tag in the html
print("full text")
print(container)                          #This will print full content present in html tag


print("\n id")
print(container. get("id"))
print("\n class")                       
print(container. get("class"))        # it will give list of the class

heading=soup.find("h2")

print("h2 printing \n")
print(heading.string)       #  yaha .text bhi use kar sakte the--> print(heading.text)

paragraph = soup.find("p")
print("printing p")
print (paragraph.text)

print(container.text)
