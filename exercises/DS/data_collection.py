import requests
from bs4 import BeautifulSoup
def getURL(page):
    """

    :param page: html of web page (here: Python home page)
    :return: urls in that page
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote


url ='https://oddanchatramvegetablemarket.net/oddanchatram-vegetable-price/page'
for i in range(0,1):
    page_url = url + str(i)
    response = requests.get(page_url)
    output = str(BeautifulSoup(response.content))
    url, n = getURL(output)
    print(url)
    print(n)