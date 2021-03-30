import requests
from bs4 import BeautifulSoup
import json



def getTurtleMethodParametersList(methodName):
    methodID = "turtle." + methodName
    url = "https://docs.python.org/3/library/turtle.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    correspondingTag = soup.find(id = methodID)
    content = soup.find(id = "methods-of-rawturtle-turtle-and-corresponding-functions")
    methodSections = content.find_all("div", class_ = "section")
    for methodSection in methodSections:
        methodSubsections = methodSection.find_all("dl")
        for methodSubsection in methodSubsections:
            methodTags = methodSubsection.find_all("dt")
            for methodTag in methodTags:
                #return None if no parameters
                if methodTag is correspondingTag: #if you found the requested methodName
                    methodParametersContainer = methodSubsection.find("dd")
                    if methodParametersContainer is None:
                        return None
                    methodParametersContainer = methodParametersContainer.find("dl")
                    if methodParametersContainer is None:
                        return None
                    methodParametersContainer = methodParametersContainer.find("dd")
                    # print("Found!")
                    listOfParams = []
                    multipleParameterList = methodParametersContainer.find("ul")
                    singleParameter = methodParametersContainer.find("p")
                    #if multiple parameters
                    if multipleParameterList is not None:
                        
                        parameterContainers = multipleParameterList.find_all("li")
                        for parameterContainer in parameterContainers:
                            parameterDescription = parameterContainer.text
                            parameterName = parameterContainer.find("strong")
                            parameterName=parameterName.text
                            # print(parameterName) 
                            parameterDescription = parameterDescription.replace(parameterName, "")
                            parameterDescription = parameterDescription.lstrip(" ")
                            # print(parameterDescription)
                            newParam = {
                                "name" : parameterName,
                                "description" : parameterDescription
                            }
                            listOfParams.append(newParam)
                        return listOfParams
                    
                    elif singleParameter is not None: 
                        parameterDescription = singleParameter.text
                        parameterName = singleParameter.find("strong")
                        if parameterName is None:
                            return None
                        parameterName=parameterName.text
                        # print(parameterName) 
                        parameterDescription = parameterDescription.replace(parameterName, "")
                        parameterDescription = parameterDescription.lstrip(" ")
                        # print(parameterDescription)
                        newParam = {
                            "name" : parameterName,
                            "description" : parameterDescription
                        }
                        listOfParams.append(newParam)
                        return listOfParams
                    else: 
                        return None
                    #if only one parameter
                    





                

       

