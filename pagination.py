'''
1. Page 1 kholo.
2. Uski 20 books collect karo.
3. Next page par jao.
4. Uski 20 books collect karo.
5. Aise hi 50 pages tak jao.
6. Saari 1000 books ek hi list mein save karo.
Python mein hum do loops use karenge:
- while loop: Pages change karega.
- for loop: Ek page ki saari books collect karega.

1. while current page handle karta hai.
2. requests.get() page download karta hai.
3. BeautifulSoup HTML parse karta hai.
4. books = soup.select(".product_pod") books select karta hai.
5. for loop har book extract karta hai.
6. extracted_data.append(listing) book ko common list mein save karta hai.
7. urljoin() next page ka URL banata hai.
8. Next page nahi mila toh current_url = None, aur while loop stop.

Sabse important 5 lines samajh
Line 1:
current_url = url
Starting mein hum Page 1 ka URL rakh rahe hain.

Line 2:
while current_url:
Jab tak current_url mein valid URL hai, loop chalta rahega.

Line 3:
for book in books:
Current page ki har book ko ek-ek karke extract karega.

Line 4:
current_url = urljoin(current_url, next_link.get("href"))
Next page ka URL banakar current_url update karega.

Line 5:
current_url = None
Jab next page nahi milega, loop stop ho jayega.
'''
import os
import requests
import pandas as pd
import psycopg2
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

url = "https://books.toscrape.com/"

# Starting page
current_url = url

# Saari books yahan collect hongi
extracted_data = []

try:

    # Jab tak next page available hai
    while current_url:

        print("Scraping:", current_url)

        # STEP 1: Current page download
        response = requests.get(current_url, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        # STEP 2: HTML parse
        soup = BeautifulSoup(response.text, "html.parser")

        # STEP 3: Current page ki books select
        books = soup.select(".product_pod")

        # STEP 4: Har book extract
        for book in books:

            Book_Title = book.select_one("h3 a").get("title")

            price_tag = book.select_one(".price_color").get_text(strip=True)

            rating_tag = book.select_one(".star-rating")
            rating = rating_tag.get("class")[-1]

            product_url = book.select_one("h3 a").get("href")
            URL = urljoin(current_url, product_url)

            listing = {
                "Title": Book_Title,
                "Cost": price_tag,
                "Rating": rating,
                "URL": URL
            }

            extracted_data.append(listing)

        # STEP 5: Next page find
        next_link = soup.select_one(".next a")

        if next_link:
            current_url = urljoin(current_url, next_link.get("href"))
        else:
            current_url = None

    # STEP 6: DataFrame
    df = pd.DataFrame(extracted_data)

    print(df.shape)

    #STEP 7: DATA CLEANING(TRANSFORM)
    df['Cost'] = df['Cost'].str.replace('£','',regex=False).astype(float)
    print(df.head())

    # STEP 8: CSV export
    file_name = datetime.now().strftime("Books_%Y%m%d_%H%M%S_%f.csv")
    df.to_csv(file_name, index=False)

    print("Scraping completed!")

    # STEP 9: POSGRESQL CONNECTION

    
    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
    )
    print("Connection successfull")
    
except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)