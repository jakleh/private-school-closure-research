import selenium
from selenium import webdriver
import pandas as pd
import xlsxwriter
from excelExtraction import caList, paList
from functions import *

userChoice = input("Would you like to scrape Ca or Pa?\n")

if chooseScript(userChoice):
    #Create excel file and worksheet for California...
    caOutWorkbook = xlsxwriter.Workbook("California_Schools.xlsx")
    caOutSheet = caOutWorkbook.add_worksheet()

    for i in range(len(caList)):
        tempName = caList[i][0]
        tempID = caList[i][1]

        try:
            activityVal = scrapeCalifornia(tempName)
        except:
            activityVal = "Not Found"

        sheetIndex = i + 1
        caOutSheet.write(i, 0, tempID)
        caOutSheet.write(i, 1, activityVal)

    caOutWorkbook.close()


else:
    #Create excel file and worksheet for Pennsylvania...
    paOutWorkbook = xlsxwriter.Workbook("Pennsylvania_Schools.xlsx")
    paOutSheet = paOutWorkbook.add_worksheet()

    for j in range(len(paList)):
        tempName = paList[j][0]
        tempID = paList[j][1]
        tempCity = paList[j][2]

        try:
            activityVal = scrapePennsylvania(tempName, tempCity)
        except:
            activityVal = "Not Found"

        sheetIndex = j + 1
        paOutSheet.write(j, 0, tempID)
        paOutSheet.write(j, 1, activityVal)

    paOutWorkbook.close()
