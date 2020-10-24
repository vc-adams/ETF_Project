from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape(search_term):
    browser = init_browser()
    listings = []

    url = f"https://houston.craigslist.org/search/sss?query={search_term}"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all('li', class_='result-row')

    # for each result, create a dictionary and add it to a list
    for item in results:
        posting = {}

        posting["date"] = item.find("time", class_="result-date").text
        posting["headline"] = item.find("a", class_="result-title").text
        posting["price"] = item.find("span", class_="result-price").text

        # Some postings don't have a neighborhood, but we still want to capture the rest of the data
        try:
            posting["hood"] = item.find("span", class_="result-hood").text
        except AttributeError as e:
            print(e)

        listings.append(posting)
    return listings
