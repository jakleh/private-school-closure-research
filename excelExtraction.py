import pandas as pd

excel_file = "ultimateStatesFile.xlsx"

def excelExtraction(sheetName):

    xldata = pd.read_excel(excel_file, sheet_name = sheetName)

    searchList = []
    for i in range(len(xldata)):

        outString = str(xldata["sch_name"][i])
        outID = str(xldata["nlsdsch"][i])
        outCity = str(xldata["lcity"][i])

        #Create properly formatted street string...
        outStreet = str(xldata["lstreet"][i])
        streetWordList = outStreet.split()

        lastWord = streetWordList[-1]

        #Add period to string abbreviation...
        streetChars = ["", ""]
        if (lastWord == "RD" or lastWord == "AVE" or lastWord == "ST" or lastWord == "DR"):

            abbrevWord = streetWordList.pop(-1)

            for char in abbrevWord:
                streetChars.append(char)

            streetChars.append(".")

        newAbbrev = ''.join(map(str, streetChars))
        streetWordList.append(newAbbrev)

        finalStreetWordList = []

        #Make [most] uppercase letters lowercase and merge words into new string...
        for word in streetWordList:
            finalCharList = []
            index = 0

            for finalChar in word:
                if (index != 0 and finalChar.isupper()):
                    finalCharList.append(finalChar.lower())
                else:
                    finalCharList.append(finalChar)

                index += 1

            finalWord = ''.join(map(str, finalCharList)) + " "
            finalStreetWordList.append(finalWord)

        newStreetString = " " + ''.join(map(str, finalStreetWordList))

        #Adding values to list using tuple...
        tempTuple = (outString, outID, outCity, newStreetString)
        searchList.append(tempTuple)

    return searchList

caList = excelExtraction('CA')
paList = excelExtraction('PA')
