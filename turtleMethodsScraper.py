import requests
from bs4 import BeautifulSoup
import json



def getTurtleMethodsList():
    allMethods = []
    url = "https://docs.python.org/3/library/turtle.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id = "turtle-methods")
    content = content.find("dl")
    methodsContainers = content.find_all("dd")
    for methodsContainer in methodsContainers:
        methodsContainer = methodsContainer.find("dl")
        if methodsContainer is None:
            continue
        methodsLines = methodsContainer.find_all("dd")
        for methodsLine in methodsLines:
            methodLineContainers = methodsLine.find_all("div", class_ = "line")
            for methodLineContainer in methodLineContainers:
                # print(methodLineContainer)
                methodLinks = methodLineContainer.find_all("a", class_ = "reference internal")
                for methodLink in methodLinks:
                    methodPath = methodLink['href']
                    # methodURL = methodPath.lstrip("#")
                    methodURL = url + methodPath
                    method = methodLink.find("code")
                    method = method.find("span", class_ = "pre")
                    methodName = method.text
                    methodName = methodName.rstrip("()")
                    #print(methodName)
                    newMethod = {
                        "methodName": methodName,
                        "methodLink": methodURL
                    }
                    allMethods.append(newMethod)
    return allMethods





methods = getTurtleMethodsList()
for method in methods:
    print(method)

