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


 def calculateOffset(value,start,step):
    return (value-start)/_Step

def store(Measurement):
    offsetAmbient=calculateOffset(Measurement.Ambient,minAmbient,stepAmbient)
    offsetCapacity=calculateOffset(Measurement.Capacity,minCapacity,stepCapacity)
    Measurements[offsetAmbient,offsetCapacity].append(Measurement)

def processCount(Mesurements,matrixCount):
    tempCount=0
    for x in Mesurements[0]:        #For each ambient
        for y in x:                 #For each capacity
            m
