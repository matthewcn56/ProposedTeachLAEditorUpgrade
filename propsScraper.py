import requests
from bs4 import BeautifulSoup
def pathComponentSwitcher(path):
    path.replace("https://material-ui.com/", "")
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



def getValidProps(materialPath):
    validProps = []
    url =  materialPath
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id = "main-content")
    contentDivs = content.find_all("div")
    for contentDiv in contentDivs:
        codeContainer = contentDiv.find("div", class_ = "MuiCollapse-container")
        # print(codeContainer)
        if codeContainer is None:
            continue
        
        codeContainer = codeContainer.find("div", class_ = "MuiCollapse-wrapper")
        codeContainer = codeContainer.find("div", class_ = "MuiCollapse-wrapperInner")
        codeContainer = codeContainer.find("div")
        codeContainer = codeContainer.find("div")
        codeContainer = codeContainer.find("pre")
        codeContainer = codeContainer.find("code", class_ = "language-jsx")
        # print(codeContainer)
        codeLinesWithComponent = codeContainer.find_all("span", class_ = "token tag")
        for codeLineWithComponent in codeLinesWithComponent:
            componentNames = codeLineWithComponent.find_all("span", class_ = "token tag")
            for componentName in componentNames: 
                # print(componentName)
                if componentName is None:
                    continue
                componentName = componentName.find("span", class_ = "token class-name")
                
                if componentName is None:
                    continue
                componentName = componentName.text
                
                if componentName != pathComponentSwitcher(materialPath):
                    continue
                #print(componentName)
                propNames = codeLineWithComponent.find_all("span", class_ = "token attr-name")
                for propName in propNames:
                    if propName is None:
                        continue
                    propName = propName.text
                    #add the propName to the validProps 
                    validProps.append(propName)
                    #print(propName)
                #remove duplicates
    rV = []
    [rV.append(x) for x in validProps if x not in rV]
    return rV



        


props = getValidProps("https://material-ui.com/components/radio-buttons")
for prop in props:
    print(prop)
