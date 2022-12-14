from .classtemplate import ClassTemplate
from .Datastructure import measurement
import numpy as np

class DataStorage(ClassTemplate):
    def __init__(self, class_setup_dict, df_meas) -> None:
        super().__init__(class_setup_dict)
        self.minAmbient = self.setup_dict["AmbientRange"][0]
        self.maxAmbient = self.setup_dict["AmbientRange"][1]
        self.minCapacity = self.setup_dict["CapacityRange"][0]
        self.maxCapacity = self.setup_dict["CapacityRange"][1]

        self.stepAmbient = self.setup_dict["stepAmbient"]
        self.stepCapacity = self.setup_dict["stepCapacity"]
        self.stepCOP = self.setup_dict["stepCOP"]

        self.df = df_meas
        self.bins_ambient = None
        self.bins_capacity = None
        self.bins_COP = None

        self.Measurements_landscape = None
        self.blank_space = ""
        self.inclusivity = 'right'

    def initStorage(self):                                    
        self.bins_ambient = self.createRange(   self.setup_dict["AmbientRange"][0],
                                                self.setup_dict["AmbientRange"][1], 
                                                inc=self.setup_dict["stepAmbient"])
        self.bins_capacity = self.createRange(  self.setup_dict["CapacityRange"][0], 
                                                self.setup_dict["CapacityRange"][1], 
                                                inc=self.setup_dict["stepCapacity"])
        self.bins_COP = self.createRange(       self.setup_dict["COPRange"][0], 
                                                self.setup_dict["COPRange"][1], 
                                                inc=self.setup_dict["stepCOP"])
        self.Measurements_landscape =[]

    def populateMeasLandscape(self):
        for i in range(0,len(self.bins_capacity)):                # 1001 (0 tot en met 1000 = 1001 indexen) steps for Capacity
            row = []
            for j in range(0,len(self.bins_ambient)):         # 81 steps for Tambient
                lbound_ambient = self.minAmbient + j*self.stepAmbient
                ubound_ambient = self.minAmbient + (j+1)*self.stepAmbient

                lbound_capacity = self.minCapacity + i*self.stepCapacity
                ubound_capacity = self.minCapacity + (i+1)*self.stepCapacity
                
                df_part = self.df.loc[(self.df['averageAmbient'].between(lbound_ambient,ubound_ambient, inclusive=self.inclusivity)) & (self.df['averageCapacity'].between(lbound_capacity,ubound_capacity, inclusive=self.inclusivity))]
                
                meas_indexs = self.blank_space
                if not df_part.empty:
                    # print("Temp Range: {} - {} ??C; Cap Range: {} - {} kW; Real Value: {} ??C & {} kW".format(lbound_ambient, 
                                                                                                            # ubound_ambient, 
                                                                                                            # lbound_capacity, 
                                                                                                            # ubound_capacity, 
                                                                                                            # df_part['averageAmbient'],
                                                                                                            # df_part['averageCapacity']))
                    meas_indexs = list(df_part.index)
                    
                row.append(meas_indexs)
            pass
            self.Measurements_landscape.append(row)
        self.checkLandscape()
        pass
    
    def checkLandscape(self):
        count = 0
        for i in range(len(self.Measurements_landscape)):
            for j in range(len(self.Measurements_landscape[0])):
                if self.Measurements_landscape[i][j] is not np.NAN:
                    record = self.Measurements_landscape[i][j]
                    if type(record) is float:
                        count += 1
                    else:
                        count += len(self.Measurements_landscape[i][j])
                pass
            pass
        print("Landscape has been filled correctly: {}".format(self.df.shape[0]==count))
        return self.df.shape[0] == count
    
    def createRange(self, start, stop, inc=1):
        return list(np.arange(start,stop,inc))  

    def process(self, proc=0):
        x,y,z=[],[],[]
        temp=0
        for i,a in enumerate(self.Measurements_landscape):          #For each capacity
            for j,b in enumerate(a):                                #For each ambient
                if not b == self.blank_space:
                    lbound_ambient = self.minAmbient + j*self.stepAmbient
                    ubound_ambient = self.minAmbient + (j+1)*self.stepAmbient
                    
                    lbound_capacity = self.minCapacity + i*self.stepCapacity
                    ubound_capacity = self.minCapacity + (i+1)*self.stepCapacity
                    
                    x.append(ubound_ambient)
                    y.append(ubound_capacity)

                    temp=0
                    sampleDuration = 0
                    for c in b:
                        match proc:
                            case 0:
                                # Method of counting Measurements per Tambient/Capacity bin
                                temp+=1
                            case 1:
                                # Method of Calculating the Average COP for a Tambient/Capacity bin
                                data = self.df.loc[c]
                                temp += data['averageCOP']
                                pass
                            case 2:
                                # Method of Calculating the Average Power for a Tambient/Capacity bin
                                data = self.df.loc[c]
                                temp += data['averagePower']

                            case 3:
                                # Method of Calculating the Energy Consumed by the system for a Tambient/Capacity bin
                                data = self.df.loc[c]
                                temp += data['totalPower']
                                sampleDuration += data['sampleCounter']
                                pass
                            case 4:
                                # Method of Calculating the Energy Produced by the system for a Tambient/Capacity bin
                                data = self.df.loc[c]
                                temp += data['totalCapacity']
                                sampleDuration += data['sampleCounter']
                                pass
                            case _:
                                pass
                    
                    if proc == 1 or proc == 2:
                        temp = temp/len(b)
                    elif proc == 3 or proc == 4:
                        temp = temp/(3600.0/sampleDuration)
                        pass

                    z.append(temp)

        return x,y,z