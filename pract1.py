from bs4 import BeautifulSoup

html = '''

<html>
<body>

<h1>Data Engineering</h1>

<p>Learn Python</p>

<p>Learn SQL</p>

</body>
</html>


'''
soup = BeautifulSoup(html,"html.parser")

print(soup.h1)            #Ye HTML ka sirf pehla <h1> element return karega  
print(soup.p)             #Ye HTML ka sirf pehla <p> element return karega  


