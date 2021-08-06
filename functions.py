import selenium
from selenium import webdriver
import pandas as pd
import xlsxwriter

#Reads input from user...
def chooseScript(choiceVar):
    if choiceVar == "Ca":
        return True
    elif choiceVar == "Pa":
        return False
    else:
        userChoice = input("Would you like to scrape Ca or Pa?")
        chooseScript(userChoice)

#Reads text in CDE and returns google-search-protocol value...
def evaluateCell(activityStatus, openString):
    if activityStatus == openString:
        returnVar = "0"
    elif activityStatus == "Closed":
        returnVar = "1"
    else:
        returnVar = "Unclear"

    return returnVar

#Scrapes CDE site for activity value...
def scrapeCalifornia(school):
    driver = webdriver.Chrome()
    driver.get("https://www.cde.ca.gov/SchoolDirectory/")

    barID = driver.find_element_by_id('AllSearchField')
    barID.send_keys(school)

    submitButton = driver.find_element_by_xpath("/html/body/div/div[5]/div[1]/div[3]/div/span[2]/button")
    submitButton.click()

    activityElement = driver.find_element_by_xpath('//*[@id="outer-container"]/div[3]/div[1]/table/tbody/tr[12]/td')
    status = activityElement.text

    finalVar = evaluateCell(status, "Active")
    driver.close()

    return finalVar

#Scrapes PDE site for activity value...
def scrapePennsylvania(school, city):

    #Entering data into search page...
    driver = webdriver.Chrome()
    driver.get('http://www.edna.pa.gov/Screens/wfSearchEntity.aspx')

    closedCheckBox = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div[6]/div/table/tbody/tr/td[2]/input')
    closedCheckBox.click()

    barName = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div[1]/div[2]/input')
    barName.send_keys(school)

    barCity = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div[3]/div[2]/input')
    barCity.send_keys(city)

    #Submitting data...
    searchButton = driver.find_element_by_xpath('/html/body/form/div[3]/input[1]')
    searchButton.click()

    #Checking activity status...
    activityElement = driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/table/tbody/tr/td[5]')
    status = activityElement.text

    finalVar = evaluateCell(status, "Open")
    driver.close()

    #Returning activity status...
    return finalVar
