import requests
import os
import json
import sys

from package.Constants import FILE_PATH, API_KEY

from datetime import datetime, date


data = {}


def news():

    # Get Current Date and Hour
    full_date = datetime.now()
    full_date = full_date.strftime("%B %d, %Y | %H:%M:%S")
    day_date = date.today().strftime("%d/%m/%Y")
    print(full_date)

    # Creating File if not exists
    if not os.path.exists(FILE_PATH):
        try:
            f = open(FILE_PATH, "w+")
        except FileNotFoundError:
            print("File/Directory does not exists !!")
            sys.exit()  # Stop the program

    data[day_date] = {}

    # API
    base_url = "http://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey="
    full_url = base_url + API_KEY

    open_page = requests.get(full_url).json()

    articles = open_page["articles"]

    # title and URL storage list
    titles = []
    urls = []

    for article in articles:
        titles.append(article["title"])
        urls.append(article["url"])

    # Building the (nested) dictionary in terms of news information
    for i in range(len(titles)):
        new = {"id": i + 1, "title": titles[i], "url": urls[i]}
        data[day_date][("id" + str(i + 1))] = new

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("File is loaded")


if __name__ == '__main__':
    news()
