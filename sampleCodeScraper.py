import requests
from bs4 import BeautifulSoup


def getSampleCode(materialPath):
    url =  "https://material-ui.com" + materialPath
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')