'''
HTML table structure
HTML tag	Meaning
<table>	Complete table
<tr>	Table row
<th>	Header cell
<td>	Normal data cell

table se data kaise extract karege?
logic: 
1. table extract karo and ek variable me store karo. if css selectors nahi diye hai like class = ... to use karna .find()
(like in below example), if diye hai css selector to dono .find() and .select_one() use kar sakte hai
2. rows extract karo .find_all() ka use karke ya fir css selectors diye ho to .select() ka use karke
3. ab har row par loop lagao and cells print karo 
4. ab ek nested loop laga kar cels ka data print kardo .get_text(strip=True) 
'''

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
</table>
"""

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")  # shortcur rows = soup.find("table").find_all("tr")

rows = table.find_all("tr")

for row in rows:
    cells = row.find_all(["th", "td"])
    items = []
     
    for cell in cells:
        
        items.append(cell.get_text(strip=True))

    print (items)

        
        