import pandas as pd
from bs4 import BeautifulSoup

html = """
<table>
    <tr>
        <th>Name</th>
        <th>Department</th>
    </tr>
    <tr>
        <td>Ali</td>
        <td>IT</td>
    </tr>
    <tr>
        <td>Rahul</td>
        <td>HR</td>
    </tr>
    <tr>
        <td>Sara</td>
        <td>Finance</td>
    </tr>
</table>
"""
soup = BeautifulSoup(html,"html.parser")

table = soup.find("table")
rows = table.find_all("tr")

data = []

for row in rows:
    cells = row.find_all(['th','td'])   # yaha ham dono tag find karne ka bol rahe hai. th OR td (or condition hai)
                                        # <th> mile ya <td> mile, dono ko return karo.
                                        #  pehli iteration me td milega only and 2nd iteration se td only

    item = []
     
    for cell in cells:
        item.append(cell.get_text(strip=True))

    data.append(item)

headers = data[0]
content = data[1:]

df =pd.DataFrame(content,columns=headers)  # here (data,columns=headers) ye galat hoga because hamne actual content banaya hai

print(df)


   


















