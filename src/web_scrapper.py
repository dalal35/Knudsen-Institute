from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

"""
TESTING CODE:

Scrapes quotes and authors from http://quotes.toscrape.com/ using Selenium and BeautifulSoup.

Selenium automates browser actions and can interact with dynamic web pages.

BeautifulSoup is used for parsing and extracting data from static HTML content.

Prints each quote along with its author to the console.
"""

# 1. Start Selenium
driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")

# 2. Wait for the quotes to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
except:
    print("Quotes not found within 10 seconds")

# 3. Get page source and parse with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 4. Extract quotes and authors
quotes = soup.find_all("div", class_="quote")
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{text} — {author}")

# 5. Close the browser
driver.quit()