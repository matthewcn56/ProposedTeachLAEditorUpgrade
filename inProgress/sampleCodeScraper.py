import requests
from bs4 import BeautifulSoup
def pathComponentSwitcher(path):
    strippedName = path.partition("components/")[2]
    strippedName = strippedName.rstrip("/")
    translatedComponent = {
        "buttons" : "Button",
        "button-group" : "ButtonGroup",
        "checkboxes" : "Checkbox",
        "floating-action-button" : "Fab",
        "radio-buttons" : "Radio",
        "selects" : "Select",
        "slider" : "Slider",
        "switches" : "Switch",
        "TextField" : "text-fields"
    }
    return translatedComponent.get(strippedName, path)



def sampleCodeScraper(materialPath):
    sampleCode = []
    url =  "https://material-ui.com" + materialPath
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id = "main-content")
    contentDivs = content.find_all("div")
    for contentDiv in contentDivs:
        codeContainer = contentDiv.find("div", class_ = "MuiCollapse-container")
        print(codeContainer)
        if codeContainer is None:
            continue
        
        codeContainer = codeContainer.find("div", class_ = "MuiCollapse-wrapper")
        codeContainer = codeContainer.find("div", class_ = "MuiCollapse-wrapperInner")
        codeContainer = codeContainer.find("div")
        codeContainer = codeContainer.find("div")
        codeContainer = codeContainer.find("pre")
        codeContainer = codeContainer.find("code", class_ = "language-jsx")
        codeLines = codeContainer.find_all("span")
        