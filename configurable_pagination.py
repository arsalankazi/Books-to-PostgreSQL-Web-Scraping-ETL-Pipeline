
import os
import math
import requests
import pandas as pd
import psycopg2

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# STARTING URL
url = "https://books.toscrape.com/"
current_url = url

# STORE ALL SCRAPED BOOKS
extracted_data = []

# DATABASE CONNECTION VARIABLES
connection = None
cursor = None

# CONFIGURABLE PAGINATION
pages_to_scrape = None
pages_scraped = 0


# DATA VALIDATION FUNCTION
def validate_book(book):

    title = book.get("Title")
    raw_cost = book.get("Cost")
    rating = book.get("Rating")
    product_url = book.get("URL")

    # TITLE VALIDATION
    if not isinstance(title, str) or not title.strip():
        return False

    # URL VALIDATION
    if not isinstance(product_url, str) or not product_url.strip():
        return False

    # COST VALIDATION
    try:
        cost = float(str(raw_cost).replace("£", "").strip())

    except (TypeError, ValueError):
        return False

    if not math.isfinite(cost) or cost <= 0:
        return False

    # RATING VALIDATION
    if rating not in ["One", "Two", "Three", "Four", "Five"]:
        return False

    # STORE CLEAN NUMERIC COST
    book["Cost"] = cost

    return True


try:

    # PAGINATION LOOP
    while current_url and (
        pages_to_scrape is None
        or pages_scraped < pages_to_scrape
    ):

        pages_scraped += 1

        print(f"Scraping page {pages_scraped}: {current_url}")

        # DOWNLOAD CURRENT PAGE
        response = requests.get(current_url, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        # PARSE HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # SELECT BOOKS
        books = soup.select(".product_pod")

        # EXTRACT BOOK DATA
        for book_element in books:

            title_tag = book_element.select_one("h3 a")
            price_tag = book_element.select_one(".price_color")
            rating_tag = book_element.select_one(".star-rating")

            # EXTRACT TITLE
            title = (
                title_tag.get("title")
                if title_tag else None
            )

            # EXTRACT COST
            price = (
                price_tag.get_text(strip=True)
                if price_tag else None
            )

            # EXTRACT RATING
            rating_classes = (
                rating_tag.get("class", [])
                if rating_tag else []
            )

            rating = (
                rating_classes[-1]
                if rating_classes else None
            )

            # EXTRACT PRODUCT URL
            product_url = (
                title_tag.get("href")
                if title_tag else None
            )

            full_url = (
                urljoin(current_url, product_url)
                if product_url else None
            )

            listing = {
                "Title": title,
                "Cost": price,
                "Rating": rating,
                "URL": full_url
            }

            extracted_data.append(listing)

        # FIND NEXT PAGE
        next_link = soup.select_one(".next a")

        if next_link:
            current_url = urljoin(
                current_url,
                next_link.get("href")
            )
        else:
            current_url = None

    print("\nScraping completed!")
    print("Total extracted records:", len(extracted_data))

    # DATA VALIDATION
    valid_books = []
    invalid_books = []

    for book in extracted_data:

        if validate_book(book):
            valid_books.append(book)

        else:
            invalid_books.append(book)

    print("\nData Validation Results")
    print("Valid books:", len(valid_books))
    print("Invalid books:", len(invalid_books))

    # STOP IF NO VALID RECORDS
    if not valid_books:
        raise ValueError("No valid records found!")

    # CREATE DATAFRAME
    df = pd.DataFrame(valid_books)

    print("\nDataFrame Shape:", df.shape)
    print(df.head())

    # CSV EXPORT
    file_name = datetime.now().strftime(
        "Books_%Y%m%d_%H%M%S_%f.csv"
    )

    df.to_csv(file_name, index=False)

    print("\nCSV exported:", file_name)

    # SQL INSERT QUERY
    insert_query = """
    INSERT INTO books (title, cost, rating, url)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (url) DO NOTHING
    """

    # DATAFRAME TO LIST OF TUPLES
    records = list(
        df[["Title", "Cost", "Rating", "URL"]]
        .itertuples(index=False, name=None)
    )

    # POSTGRESQL CONNECTION
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    # BULK INSERT
    cursor.executemany(insert_query, records)

    connection.commit()

    print("\nData inserted into database successfully!")


except requests.exceptions.RequestException as e:

    print("Scraping error:", e)


except psycopg2.Error as e:

    if connection is not None:
        connection.rollback()

    print("Database error:", e)


except ValueError as e:

    print("Data validation error:", e)


finally:

    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()
        print("Database connection closed.")
