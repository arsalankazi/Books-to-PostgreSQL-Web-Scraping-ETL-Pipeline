'''
response.encoding	               Requests library currently kaunsi encoding use kar raha hai
response.apparent_encoding	       Content ko dekhkar detected encoding

issue ye the ki price esi print ho rahi thi Â£51.77
 problem ye mili ki requests library alag encoding use kar rahi thi aur website se data kisi aur encoding me aaraha 
 tha. 
ise fix karne ke liye response.encoding = response.apparent_encoding kiya
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime


url = "https://books.toscrape.com/"

try:

    response = requests.get(url, timeout = 15)                # you missed timeout
    print("Response code is:",response.status_code)
    response.raise_for_status()                               # you missed ()
    
    # fixed encoding issue

    response.encoding = response.apparent_encoding            

    
    html = response.text
    soup = BeautifulSoup(html,"html.parser")


    # Extraction

    books = soup.select(".product_pod")                        # container extract kare

    extracted_data = []                                        # make an empty list. yaha complete extracted data hoga



    for book in books:

        Book_Title = book.select_one("h3 a").get("title")
        
        price_tag = book.select_one(".price_color").get_text(strip= True)

        rating_tag= book.select_one(".star-rating")
        rating=rating_tag.get("class")[-1]
        
        product_url = book.select_one("h3 a").get("href")
        URL = urljoin(url,product_url)

        #print("Title:",Book_Title)
        #print("Cost:",price_tag)
        #print("Rating:",rating)
        #print("URL",URL)

        listing = {

            "Title"  : Book_Title,
            "Cost"   : price_tag,
            "Rating" : rating,
            "URL"    : URL

        }
        

        extracted_data.append(listing)  

    df = pd.DataFrame(extracted_data)

    
    '''print(type(extracted_data))
    print(type(extracted_data[0]))
    print((extracted_data))'''
     
    print("DataFrame is:",df)
    print(df.shape)
    #print(df.head())
    
    # EXPORTING DATAFRAME INTO THE CSV FILE
    file_name = datetime.now().strftime("Books_%Y%m%d_%H%M%S_%f.CSV")
    df.to_csv(file_name,index=False)




except requests.exceptions.Timeout:
    print("site is taking too much time")

except requests.exceptions.RequestException as e:      # forgot to write as e
    print("something went wrong",e) 















