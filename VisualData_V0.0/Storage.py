from itertools import _Step
import math
from pprint import pformat


class Storage:
 minAmbient=-20.0                                                   #Colums: ambient
 maxAmbient=60.0
 stepAmbient=1.0
 rangesAmbient=math.ceil((maxAmbient-minAmbient)/stepAmbient)

 minCapacity=0.0                                                    #Rows: capacity
 maxCapacity=10000.0
 stepCapacity=10.0
 rangesCapacity=math.ceil((maxCapacity-minCapacity)/stepCapacity)

 maxMeasurements=1000                                               #Collection of measurements for one situation [ambient,capacity]

 Measurements =[ [ [ [0.0] * rangesAmbient ] * rangesCapacity ] * maxMeasurements ] #3D array with each element value as 0.0, contains all measurements
 matrixCount=[ [ [0.0] * rangesAmbient ] * rangesCapacity ]                         #2D array with count of measurements for each situation
 matrixCOP=[ [ [0.0] * rangesAmbient ] * rangesCapacity ]                           #2D array with average COP for each situation
 matrixPower=[ [ [0.0] * rangesAmbient ] * rangesCapacity ]                         #2D array with average POWER for each situation
 matrixCapacity=[ [ [0.0] * rangesAmbient ] * rangesCapacity ]                      #2D array with average CAPACITY for each situation #unnecessary
 matricConsumption= [ [ [0.0] * rangesAmbient ] * rangesCapacity ]                  #2D array with total CONSUMPTION for each situation 


 def calculateOffset(value,start,step):
    return (value-start)/_Step

def store(Measurement):
    offsetAmbient=calculateOffset(Measurement.Ambient,minAmbient,stepAmbient)
    offsetCapacity=calculateOffset(Measurement.Capacity,minCapacity,stepCapacity)
    Measurements[offsetAmbient,offsetCapacity].append(Measurement)

def processCount(Measurements,matrixCount):
    tempCount=0
    for x in Measurements[0]:        #For each ambient
        for y in x:                 #For each capacity
            processCount[x][y]=Measurements[x][y].length

def processCOP(Measurements,matrixCOP):
    tempCOP=0.0
    for x in Measurements[0]:           #For each ambient
        for y in x:                     #For each capacity
            for z in y:                 #For each measurement in a specific case    
                tempCOP+=Measurements[x][y][z].averageSample

            matrixCOP[x][y]=tempCOP/Measurements[x][y].length

def processPower(Measurements,matrixPower):
    tempPower=0.0
    for x in Measurements[0]:           #For each ambient
        for y in x:                     #For each capacity
            for z in y:                 #For each measurement in a specific case    
                tempPower+=Measurements[x][y][z].averagePower
            matrixPower[x][y]=tempPower/Measurements[x][y].length

def processConsumption(Measurements,matrixConsumption,sampleDuration):
    tempConsumption=0.0
    for x in Measurements[0]:           #For each ambient
        for y in x:                     #For each capacity
            for z in y:                 #For each measurement in a specific case    
                tempConsumption+=Measurements[x][y][z].totalPower #Total consumption during sample duration
            matrixConsumption[x][y]=(tempConsumption)/(3600.0/sampleDuration) #Total consumption in a specific case (scaled to kWh)

def processProduction(Measurements,matrixProduction,sampleDuration):
    tempProduction=0.0
    for x in Measurements[0]:           #For each ambient
        for y in x:                     #For each capacity
            for z in y:                 #For each measurement in a specific case    
                tempProduction+=Measurements[x][y][z].totalCapacity #Total consumption during sample duration
            matrixProduction[x][y]=(tempProduction)/(3600.0/sampleDuration) #Total consumption in a specific case (scaled to kWh)
