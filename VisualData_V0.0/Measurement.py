class Measurement(object):
 #global variables
 flatDetected=0
 sampleCounter=0        #amount of samples in candidate measuremt
 sampleLength=10        #10 samples in one meseurement
 maxDeviation=0.1       #10% deviation in one meseurement
 firstSample=0.0        #First sample of the candidate
 
 actualSample=0.0       #Latest sample of the candidate
 averageSample=0.0      #Average of samples in candidate
 totalSample=0.0        #Sum of all samples in candidate

 averagePower=0.0       #Average of power in candidate
 totalPower=0.0         #Sum of all power in candidate

 averageCapacity=0.0    #Average of capacity in candidate
 totalCapacity=0.0      #Sum of all capacity in candidate

 averageAmbient=0.0     #Average of ambient temperature in candidate
 totalAmbient=0.0       #Sum of ambient in candidate




def newMeasurement(self,ambient_T,Capacity,Power,COP,timeStamp):#Create new object
    self.ambient_T=ambient_T
    self.Capacity=Capacity
    self.Power=Power
    self.COP=COP
    self.timeStamp=timeStamp
    firstSample=0.0     #Reset First sample 
    averageSample=0.0   #Average of samples in candidate 
    sampleCounter=0


     
def detectFlat(Capacity,Power,Ambient,maxDeviation,sampleLength,flatDetected):#Analyze data feed to extraxt flat graph 
    actualSample=Capacity/Power                                 #Most recent sample COP
    deviation=abs((actualSample/firstSample)-1)                 #Deviation of actual sample in %
    if  deviation<= maxDeviation + firstSample==0.0  :          #Deviation smaller than max deviation or first sample
        sampleCounter+=1                                        #Sample
        totalSample+=actualSample
        averageSample=totalSample/sampleCounter

        totalPower+=Power                                       #Power
        averagePower=totalPower/sampleCounter

        totalCapacity+=Capacity                                 #Capacity    
        averageCapacity=totalCapacity/sampleCounter

        totalAmbient+=Ambient                                   #Ambient temperature    
        averageAmbient=totalAmbient/sampleCounter
    else :                                                      #Actual sample deviation too big=> Accept new first sample
        sampleCounter=1                                         #Reset sample counter
        firstSample=actualSample                                #New first sample
        totalSample=actualSample                                #Reset total sample
        averageSample=actualSample                              #Reset average sample   
        
        averagePower=Power                                      #Power
        totalPower=Power

        averageCapacity=Capacity                                #Capacity
        totalCapacity=Capacity

        averageAmbient=Ambient                                  #Ambient temperature  
        totalAmbient=Ambient


    if sampleCounter>=sampleLength:                             #Signal end of mesearument
        flatDetected=1
    else:
        flatDetected=0
