'''
Task 1: .find() se first paragraph print karo.

Task 2: .find_all() se saare paragraphs print karo.

Task 3: .find_all() use karke sirf first 2 paragraphs print karo.

Task 4: .find("h2") karke output batao.
'''

from bs4 import BeautifulSoup

html = '''
<html>
<body>

<h1>My Skills</h1>

<p>Python</p>
<p>SQL</p>
<p>Pandas</p>
<p>Power BI</p>

</body>
</html>

'''
soup = BeautifulSoup(html,'html.parser')
print(soup.find('p'))
print(soup.find_all('p'))                    # .find_all() gives a list as output
print(soup.find_all('p',limit=2))
print(soup.find('h2'))





