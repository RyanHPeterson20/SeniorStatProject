# -*- coding: utf-8 -*-

import pandas as pd
import re

import numpy as np


def main():

    

    ###below this is importing the data sets _______________________________________________
    
    ##denver-aurora-lakewood MSA counties
    MSA_countycodes = ['001', '005', '014', '019', '031', '035', '039', '047', '059', '093']
        
    ##econ data 2015
    ##remove the weird column headers before importing
    econData2015 = pd.read_csv('~/Spring 2021/Stat Project/ACS Data/2015_2019_ecoData_tract/ACSDP5Y2015.DP03_data_with_overlays_2021-02-15T164745.csv')
    
        
    ##create new column with county codes
    econData2015['CountyCodes'] = countyCodes(econData2015['id'])

    MSA_econData2015 = econData2015[econData2015["CountyCodes"].isin(MSA_countycodes)]

    
    ##set cleaned data as new column data, create new column with tract number instead
    MSA_econData2015['Geographic Area Name'] = censusTractNumbers(MSA_econData2015['Geographic Area Name'])
    
    #combine tract code with county code by extracting this from id data
    MSA_econData2015['CodeID'] = codeID(MSA_econData2015['id'])

    #test print
    print(MSA_econData2015['CodeID'])    
    
    ##demo data 2015
    demoData2015 = pd.read_csv('~/Spring 2021/Stat Project/ACS Data/2015_2019_demoData_tract/ACSDP5Y2015.DP05_data_with_overlays_2021-02-15T165132.csv')

    ##create new column with county codes
    demoData2015['CountyCodes'] = countyCodes(demoData2015['id'])

    MSA_demoData2015 = demoData2015[demoData2015["CountyCodes"].isin(MSA_countycodes)]

    
    #extract Census Tract name from id number
    MSA_demoData2015['Geographic Area Name'] = censusTractNumbers(MSA_demoData2015['Geographic Area Name'])
    
    #combine tract code with county code by extracting this from id data
    MSA_demoData2015['CodeID'] = codeID(MSA_demoData2015['id'])
    
    
    ##social data 2015
    socData2015 = pd.read_csv('~/Spring 2021/Stat Project/ACS Data/2015_2019_socialData_Tract/ACSDP5Y2015.DP02_data_with_overlays_2021-02-15T164333.csv')
        
    #extract Census Tract name from id number
    socData2015['Geographic Area Name'] = censusTractNumbers(socData2015['Geographic Area Name'])
    
    ##create new column with county codes
    socData2015['CountyCodes'] = countyCodes(socData2015['id'])

    MSA_socData2015 = socData2015[socData2015["CountyCodes"].isin(MSA_countycodes)]
    
    #combine tract code with county code by extracting this from id data
    MSA_socData2015['CodeID'] = codeID(MSA_socData2015['id'])
    
    
    ##housing data 2015
    houseData2015 = pd.read_csv('~/Spring 2021/Stat Project/ACS Data/2015_2019_housingData_tract/ACSDP5Y2015.DP04_data_with_overlays_2021-02-15T164949.csv')
    
    #extract Census Tract name from id number
    houseData2015['Geographic Area Name'] = censusTractNumbers(houseData2015['Geographic Area Name'])
    
    ##create new column with county codes    
    houseData2015['CountyCodes'] = countyCodes(houseData2015['id'])

    MSA_houseData2015 = houseData2015[houseData2015["CountyCodes"].isin(MSA_countycodes)]   
    
    #combine tract code with county code by extracting this from id data
    MSA_houseData2015['CodeID'] = codeID(MSA_houseData2015['id'])
    
    #export of cleaned data
    MSA_houseData2015.to_csv('~/Spring 2021/Stat Project/MSA_house_clean_2015.csv')
    MSA_socData2015.to_csv('~/Spring 2021/Stat Project/MSA_soc_clean_2015.csv')
    MSA_demoData2015.to_csv('~/Spring 2021/Stat Project/MSA_demo_clean_2015.csv')
    MSA_econData2015.to_csv('~/Spring 2021/Stat Project/MSA_econ_clean_2015.csv')
    
   
    
###----------------------------
    tract_centroid = pd.read_csv('~/Spring 2021/Stat Project/CenPop2010_Mean_TR08.txt', dtype=str)

    ##county code to form 000
    countyCode = []
    for i in tract_centroid['COUNTYFP']:
        i = str(i)
        if len(i) != 3:
            if len(i)==1:
                countyCode.append("00" + i)
            else:
                countyCode.append("0" + i)
        else:
            countyCode.append(i)        
            
    newCountyCode = pd.Series(countyCode)
    
    tract_centroid["COUNTYFP"] = newCountyCode
    
    ##format latitude without the +
    latitude = []
    for i in tract_centroid['LATITUDE']:
        i = i.replace('+', '')
        latitude.append(i)
        
    newLatitude = pd.Series(latitude)
    
    tract_centroid['LATITUDE'] = newLatitude
    
    ##select for only counties from Denver MSA    
    MSA_tract_centroid = tract_centroid[tract_centroid['COUNTYFP'].isin(MSA_countycodes)]
    
    ##create codeID to compare with other data frames
    MSA_tract_centroid['CodeID'] = MSA_tract_centroid['COUNTYFP'] + MSA_tract_centroid['TRACTCE']
    
    print(MSA_tract_centroid)


        

def censusTractNumbers(tractname):

    censusTract = []
    censusTractNum = []
    censusTractFinal = []

    for i in tractname:
        tempList = list(re.split(",{1}", i))
        censusString = tempList[0]
        censusTract.append(censusString)

    for i in censusTract:
        tempList = list(re.split('\s+', i))
        censusTractNum.append(tempList[2])
        
    for i in censusTractNum:
        i = i.replace('.', '')
        if len(i)==2:
            i=i+'00'
        if len(i)==3:
            i=i+'0'
        censusTractFinal.append(i)
        

    return censusTractFinal

def countyCodes(idValue):
    ##takes id from census data and extracts county code
    county_code = []
    
    for i in idValue:
        j = i[11:14]
        county_code.append(j)
    return county_code


def codeID(idValue):
    ##takes id from census data and extracts county code and tract number into a single code that can be compared
    code_New = []
    
    for i in idValue:
        j = i[11:]
        code_New.append(j)
    return code_New


if __name__ == '__main__':
    main()
