# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import haversine as hs
from haversine import Unit

def main():
    
    #import routing and location data for 
    location_data = pd.read_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/MSA_location.csv')
    
    ##convert duration data from string to float then seconds to minutes
    duration = []
    for i in location_data['DURATION']:
        i = str(i)[1:-1]
        i = float(i)
        i = i/60
        duration.append(i)
        
    location_data['DURATION'] = pd.Series(duration)
    
    
    #add in haversine distance (euclidian)
    location_lng = location_data['LONGITUDE']
    location_lat = location_data['LATITUDE']
    loc2 = (39.7453, -105.0007)
    haversine_distance = []
    for i in range(0,620):
        loc1 = (location_lat[i], location_lng[i])
        distance_crow = hs.haversine(loc1, loc2, unit = Unit.MILES)        
        haversine_distance.append(distance_crow)

    location_data['DISTANCE'] = pd.Series(haversine_distance)       

    
    ##import econ data
    econ_data = pd.read_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/MSA_econ_clean_2015.csv')
    
    ##rename columns with more appropriate names
    econ_data.rename(columns = {'Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed' : 'LABOR_PARTICIPATION'}, inplace=True)
    econ_data.rename(columns = {'Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed': 'UNEMPLOYED'}, inplace=True)
    econ_data.rename(columns = {'Estimate!!INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)':'MEDIAN_INCOME'}, inplace=True)
    econ_data.rename(columns = {'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people':'BELOW_POVERTY'}, inplace=True)
    
    
    ##import demographic data
    demo_data = pd.read_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/MSA_demo_clean_2015.csv')
    
    #rename column with appropriate names
    demo_data.rename(columns = {'Percent!!RACE!!One race!!White':'%POP_WHITE'}, inplace=True)
    
    #create data frame with only codeID and factors of interest
    demo_regression_data = pd.DataFrame(demo_data, columns=['CodeID', '%POP_WHITE'])
    
    
    ##import housing data
    house_data  = pd.read_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/MSA_house_clean_2015.csv')  
    
    #rename columns with more appropriate names
    house_data.rename(columns = {'Percent!!UNITS IN STRUCTURE!!Total housing units!!1-unit, detached':'%SINGLE_FAMILY_HOMES'}, inplace=True)
    house_data.rename(columns = {'Percent!!VEHICLES AVAILABLE!!Occupied housing units!!No vehicles available':'NO_VEHICLE'}, inplace=True)
    house_data.rename(columns = {'Percent!!GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!35.0 percent or more':'GT35%_INCOME_RENT'}, inplace=True)
    
    #create data frame with only codeID and factors of interest
    house_regression_data = pd.DataFrame(house_data, columns=['CodeID','%SINGLE_FAMILY_HOMES','NO_VEHICLE','GT35%_INCOME_RENT'])
    
    
    ##import social data
    social_data = pd.read_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/MSA_soc_clean_2015.csv')

    #rename columns with more appropriate names
    social_data.rename(columns = {'Percent!!HOUSEHOLDS BY TYPE!!Households with one or more people under 18 years':'1+_UNDER18'}, inplace=True)
    social_data.rename(columns = {'Percent!!HOUSEHOLDS BY TYPE!!Households with one or more people 65 years and over':'1+_OVER65'}, inplace=True)
    social_data.rename(columns = {"Percent!!EDUCATIONAL ATTAINMENT!!Percent bachelor's degree or higher":'EDUCATION_BACHELORS'}, inplace=True)
    social_data.rename(columns = {"Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)":'EDUCATION_HS'}, inplace=True)
    social_data.rename(columns = {'Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Language other than English':'LANGUAGE_OT_ENGLISH'}, inplace=True)

    #create data frame with only codeID and factors of interest
    social_regression_data = pd.DataFrame(social_data, columns=['CodeID','1+_UNDER18','1+_OVER65','EDUCATION_BACHELORS','EDUCATION_HS','LANGUAGE_OT_ENGLISH'])
    
    #merge data between location(i.e route) and econ data
    route_econ_data = pd.merge(location_data, econ_data, on='CodeID')
    
          
    ##build regression data frame
    regression_data = pd.DataFrame(route_econ_data, columns=['CodeID', 'COUNTYFP', 'TRACTCE', 'DURATION', 'DISTANCE', 'LABOR_PARTICIPATION', 'UNEMPLOYED', 'COMMUTE_PUBLIC', 'COMMUTE_PRIVATE_ALONE', 'COMMUTE_PRIVATE_CARPOOL', 'MEDIAN_INCOME', 'BELOW_POVERTY'])
    
    #merge other data to regression df
    regression_data = pd.merge(regression_data, demo_regression_data, on='CodeID')
    regression_data = pd.merge(regression_data, house_regression_data, on='CodeID')
    regression_data = pd.merge(regression_data, social_regression_data, on='CodeID')
    
 
        
        
    regression_data.to_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/StatProject_Final.csv')

    
    
    ##random sampling from data frame:
    np.random.seed(5)
    Random_tract = pd.Series(np.random.randint(1, 620, size = 62))  
    ##sample for initial variable exploration/reduction
    var_Reduction_Id = pd.Series(Random_tract)

    
    random_sample = pd.DataFrame(regression_data, index = var_Reduction_Id)
    
    random_sample.to_csv('C:/Users/Omegon/Documents/Spring 2021/Stat Project/Random_Sample.csv')
    
    
if __name__ == '__main__':
    main()