"""Tasks:
1. div ko find karo.
2. .get_text() se complete text print karo.
3. separator=" | " use karke print karo.
4. separator=" | " aur strip=True dono use karke print karo"""

from bs4 import BeautifulSoup

html = """
<div class="product">
    <h2>   Samsung Phone   </h2>
    <p>   Price: ₹15,000   </p>
    <p>   Rating: 4.5 Stars   </p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

container = soup.find("div", class_='product')

print("Full text:",container.get_text())                 #dont forget to use ()---->.get_text()

print("with separator |::::",container.get_text(separator=" | "))
print("with separator | and strip::::",container.get_text(separator=" | ",strip=True))


''' 
.get_text(separator="",strip=false )   this is by default syntax   separator means hame extracted text ko kisse seapate karna hai
                                       strip means hame whitespaces and blanks hatane hai ya nahi true = yes false = no   
                                       isse extracted content ek hi line me aa jata hai
'''



