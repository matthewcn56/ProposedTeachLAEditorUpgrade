import requests
from bs4 import BeautifulSoup
import json

def getSampleCode(materialPath):
    url =  "https://material-ui.com" + materialPath
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')