import requests
from bs4 import BeautifulSoup
import json

def inputItemSwitcher(inputName):
    translatedItem = {
        #Adjust Fab, remove date/time and transfer list since they aren't components
        "FloatingActionButton": "Fab",
        "Date/Time" : "",
        "TransferList" : ""
    }
    return translatedItem.get(inputName, inputName)
def getInputComponentList():
    url =  "https://material-ui.com/components/container"

    listOfInputComponents = []
    page = requests.get(url)

    #strip the container part of the url
    url = url.replace("components/container", "")

    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find("html")
    soup = soup.find("body")
    results = soup.find("div", class_ = "MuiDrawer-root" )
    navContainer = soup.find("div", class_ = "MuiPaper-root")
    navContainer = navContainer.find("div") # Might be wrong if he adds more divs to the page later! Easily fixable
    navContainer = navContainer.find("ul", class_ = "MuiList-root")
    navSections = navContainer.find_all("li", class_ = "MuiListItem-root")
    for navSection in navSections:
        navSectionTitle = navSection.find("button", class_ = "MuiButtonBase-root")
        if navSectionTitle is None:
            continue
        navSectionTitle = navSectionTitle.find("span", class_ = "MuiButton-label").text #This finds the nav section title!
        # print(navSectionTitle)
        if navSectionTitle == "Components": #only continue inside the components section
            # print ("Entered components!")
            components = navSection.find("div", class_ = "MuiCollapse-container")
            components = components.find("div", class_ = "MuiCollapse-wrapper")
            components = components.find("div", class_ = "MuiCollapse-wrapperInner")
            components = components.find("ul", class_ = "MuiList-root")
            possibleComponents = components.find_all("li")
            for possibleComponent in possibleComponents:
                componentsTitle = possibleComponent.find("button", class_ = "MuiButtonBase-root")
                if componentsTitle is None:
                    continue
                componentsTitle = componentsTitle.find("span", class_ = "MuiButton-label").text
                #print(componentsTitle)
                if componentsTitle == "Inputs": #only continue inside the inputs section
                    inputComponents = possibleComponent.find("div", class_ = "MuiCollapse-container")
                    inputComponents = inputComponents.find("div", class_ = "MuiCollapse-wrapper")
                    inputComponents = inputComponents.find("div", class_ = "MuiCollapse-wrapperInner")
                    inputComponents = inputComponents.find("ul", class_ = "MuiList-root")
                    possibleInputs = inputComponents.find_all("li", class_ = "MuiListItem-root")
                    for possibleInput in possibleInputs:
                        possibleInput = possibleInput.find("a", class_ = "MuiButtonBase-root")
                        inputLink = possibleInput['href']
                        inputLink = inputLink.rstrip("/")
                        inputLink = inputLink.lstrip("/")
                        inputLink = url + inputLink
                        # print(inputLink)
                        inputTitle = possibleInput.find("span", class_ = "MuiButton-label").text
                        inputTitle = inputTitle.replace(" ", "")
                        inputTitle = inputItemSwitcher(inputTitle)
                        if inputTitle is not "":
                            newInput = {
                                "componentName" : inputTitle,
                                "componentLink" : inputLink
                            }
                            listOfInputComponents.append(newInput)
    return listOfInputComponents


# inputs = getInputComponentList()
# for input in inputs:
#     print(input["componentName"])


    


