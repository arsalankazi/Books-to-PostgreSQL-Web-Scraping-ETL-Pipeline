'''

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

pages_to_scrape = None
pages_scraped = 0


try:

    # Jab tak next page available hai
    while current_url and (pages_to_scrape is None   or  pages_scraped < pages_to_scrape):

        pages_scraped += 1
        print(f"Scraping page {pages_scraped}:{current_url}")

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

    # STEP 9: SQL QUERY

    insert_query = """
    INSERT INTO books (title, cost, rating, url)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (url) DO NOTHING
    """

    #STEP 10: DF TO LIST CONVERSION

    records = list(
        df[["Title", "Cost", "Rating", "URL"]].itertuples(index=False, name=None)
    )

    # STEP 9: POSGRESQL CONNECTION


    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
    )

    
    cursor = connection.cursor()
    cursor.executemany(insert_query, records)
    connection.commit()

    print("Data inserted into database successfully!")

    
except requests.exceptions.RequestException as e:
    print("Scraping error:", e)

except psycopg2.Error as e:
    if connection is not None:
        connection.rollback()

    print("Database error:", e)

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()

    print("Database connection closed.")