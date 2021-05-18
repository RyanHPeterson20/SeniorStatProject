# -*- coding: utf-8 -*-


import openrouteservice as ors  ##open source software
import pandas as pd


def main():


    location_data = pd.read_csv('~/Spring 2021/Stat Project/MSA_location.csv')
    
    location_lng = location_data['LONGITUDE']
    location_lat = location_data['LATITUDE']
    location_routing_data=[[-105.0007,39.7453]]
    
    for i in range(len(location_data)-1):
        location_routing_data.append([location_lng[i],float(location_lat[i])])
        
    #This is ugly but it worked    
    source_id_1 = list(range(1, 100))
    source_id_2 = list(range(100, 200))
    source_id_3 = list(range(200, 300))
    source_id_4 = list(range(300, 400))
    source_id_5 = list(range(400, 500))
    source_id_6 = list(range(500, 600))
    source_id_6_21 = list(range(600, 622))

    routes = []
    route_extract = ors_matrix(location_routing_data, source_id_1)
    for i in route_extract:
        routes.append(i)
        
    route_extract = ors_matrix(location_routing_data, source_id_2)
    for i in route_extract:
        routes.append(i)
        
    route_extract = ors_matrix(location_routing_data, source_id_3)
    for i in route_extract:
        routes.append(i)
        
    route_extract = ors_matrix(location_routing_data, source_id_4)
    for i in route_extract:
        routes.append(i)

    route_extract = ors_matrix(location_routing_data, source_id_5)
    for i in route_extract:
        routes.append(i)        
        
    route_extract = ors_matrix(location_routing_data, source_id_6)
    for i in route_extract:
        routes.append(i)        
        
    route_extract = ors_matrix(location_routing_data, source_id_6_21)
    for i in route_extract:
        routes.append(i)        
                
        
    print(routes)
    
    route_series = pd.Series(routes)
    
        
    location_data['DURATION'] = route_series
    location_data.to_csv('~/Spring 2021/Stat Project/MSA_location.csv')
        
    ##sort by county to keep matrix size down, needs to be kept down even more 3500 max. 
    #(max rows 58 + 1 for desto = 59; 59^2 = 3481


    #start with adams county (county code 001)
    adams_co = location_data[location_data['COUNTYFP'] == 1]
    adams_lng = adams_co['LONGITUDE']
    adams_lat = adams_co['LATITUDE']

    ##all lists must be initialized with the destination coordinatess
    adams_routing_list_1 = [[-105.0007,39.7453]]

    #range function is to but not including the parameter
    for i in range(58):
        adams_routing_list_1.append([adams_lng[i],float(adams_lat[i])])
    
    adams_routing_list_2 = [[-105.0007,39.7453]]

    for i in range(58, 97):
        adams_routing_list_2.append([adams_lng[i],float(adams_lat[i])])

    
    
    ##add function call and realigning this to the data

    ##arapahoe county (code 005)
    arapahoe_co = location_data[location_data['COUNTYFP'] == 5]
    arapahoe_lng = arapahoe_co['LONGITUDE']
    arapahoe_lat = arapahoe_co['LATITUDE']


    ##all lists must be initialized with the destination coordinatess
    arapahoe_routing_list_1 = [[-105.0007,39.7453]]

    #range function is to but not including the parameter
    for i in range(97, 155):
        arapahoe_routing_list_1.append([arapahoe_lng[i],arapahoe_lat[i]])
    
    arapahoe_routing_list_2 = [[-105.0007,39.7453]]

    for i in range(155, 213):
        arapahoe_routing_list_2.append([arapahoe_lng[i],float(arapahoe_lat[i])])
        
    arapahoe_routing_list_3 = [[-105.0007,39.7453]]

    for i in range(213, 244):
        arapahoe_routing_list_3.append([arapahoe_lng[i],float(arapahoe_lat[i])])
        
    ##replace print with function calls
    
    
    
    ##broomfield county (code 014)
    broomfield_co = location_data[location_data['COUNTYFP'] == 14]
    broomfield_lng = broomfield_co['LONGITUDE']
    broomfield_lat = broomfield_co['LATITUDE']
    
    broomfield_routing_list_1 = [[-105.0007,39.7453]]
    
    for i in range(244, 262):
         broomfield_routing_list_1.append([broomfield_lng[i],float(broomfield_lat[i])])
 
    ##replace print with function calls
        
    
    
    ##clear creak county (code 019)
    clearcreak_co = location_data[location_data['COUNTYFP'] == 19]
    clearcreak_lng = clearcreak_co['LONGITUDE']
    clearcreak_lat = clearcreak_co['LATITUDE']
    
    clearcreak_routing_list_1 = [[-105.0007,39.7453]]
    
    for i in range(262, 265):
         clearcreak_routing_list_1.append([clearcreak_lng[i],float(clearcreak_lat[i])])

    ##replace print with function calls    
    

    
    ##denver county (code 31)
    denver_co = location_data[location_data['COUNTYFP'] == 31]
    denver_lng = denver_co['LONGITUDE']
    denver_lat = denver_co['LATITUDE']
    
    denver_routing_list_1 = [[-105.0007,39.7453]]
    
    for i in range(265, 323):
         denver_routing_list_1.append([denver_lng[i],float(denver_lat[i])])
         
    denver_routing_list_2 = [[-105.0007,39.7453]]
    
    for i in range(323, 381):
         denver_routing_list_2.append([denver_lng[i],float(denver_lat[i])])
         
    denver_routing_list_3 = [[-105.0007,39.7453]]
    
    for i in range(381, 409):
         denver_routing_list_3.append([denver_lng[i],float(denver_lat[i])])
    
    ##replace print with function calls
     
    
    ##douglas county (code 035)
    douglas_co = location_data[location_data['COUNTYFP'] == 35]
    douglas_lng = douglas_co['LONGITUDE']
    douglas_lat = douglas_co['LATITUDE']
    
    douglas_routing_list_1 = [[-105.0007,39.7453]]   
    
    for i in range(409, 451):
        douglas_routing_list_1.append([douglas_lng[i],float(douglas_lat[i])])
        
    douglas_routing_list_2 = [[-105.0007,39.7453]]   
    
    for i in range(451, 470):
        douglas_routing_list_2.append([douglas_lng[i],float(douglas_lat[i])])
        
    ##replace print with function calls
    
    
    ##el paso county (code 039)
    elpaso_co = location_data[location_data['COUNTYFP'] == 39]
    elpaso_lng = elpaso_co['LONGITUDE']
    elpaso_lat = elpaso_co['LATITUDE']
    
    elpaso_routing_list_1 = [[-105.0007,39.7453]]  
    
    for i in range(470, 477):
        elpaso_routing_list_1.append([elpaso_lng[i],float(elpaso_lat[i])])
        
    ##replace print with function calls
    
    
    ##gilpin county (code 047)
    gilpin_co = location_data[location_data['COUNTYFP'] == 47]
    gilpin_lng = gilpin_co['LONGITUDE']
    gilpin_lat = gilpin_co['LATITUDE']
    
    gilpin_routing_list_1 = [[-105.0007,39.7453]]  
    
    for i in range(477, 478):
        gilpin_routing_list_1.append([gilpin_lng[i],float(gilpin_lat[i])])
        
    ##replace print with function calls
        
    
    ##jefferson county (code 059)    
    jefferson_co = location_data[location_data['COUNTYFP'] == 59]
    jefferson_lng = jefferson_co['LONGITUDE']
    jefferson_lat = jefferson_co['LATITUDE']
    
    jefferson_routing_list_1 = [[-105.0007,39.7453]]
    
    for i in range(478, 536):
        jefferson_routing_list_1.append([jefferson_lng[i],float(jefferson_lat[i])])
        
    jefferson_routing_list_2 = [[-105.0007,39.7453]]
    
    for i in range(536, 594):
        jefferson_routing_list_2.append([jefferson_lng[i],float(jefferson_lat[i])])        
        
    jefferson_routing_list_3 = [[-105.0007,39.7453]]
    
    for i in range(594, 616):
        jefferson_routing_list_3.append([jefferson_lng[i],float(jefferson_lat[i])])


    
    ##park county (code  093)
    park_co = location_data[location_data['COUNTYFP'] == 93]
    park_lng = park_co['LONGITUDE']
    park_lat = park_co['LATITUDE']
    
    park_routing_list_1 = [[-105.0007,39.7453]]  
    
    for i in range(616, 621):
        park_routing_list_1.append([park_lng[i],float(park_lat[i])])
        
    




##convert below into a function
def ors_matrix(county_coordinates, source_list):
    client = ors.Client(key='')#requires key from ORS
    
    #  organized as [longitude, latitude]
    coordinates = county_coordinates

    matrix = client.distance_matrix(
        locations=coordinates,
        sources = source_list,
        destinations = [0],
        profile='driving-car',
        metrics=['duration'],
      validate=False,
    )

    return matrix['durations']



if __name__ == '__main__':
    main()

