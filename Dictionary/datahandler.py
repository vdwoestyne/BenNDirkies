from .classtemplate import ClassTemplate
from .Datastructure import measurement
import pandas as pd

class DataHandler(ClassTemplate):
    def __init__(self, raw_data, class_setup_dict) -> None:
        super().__init__(class_setup_dict)

        self.raw_data = raw_data
        self.measurements = []
        
        pass

    def handleData(self):
        new_meas = True
        for i in range(1, self.raw_data.shape[0]):
            record = self.raw_data.values[i]
            [actualTimeStamp, actualAmbient, actualCapacity, actualSample] = record

            actualPower = actualCapacity/actualSample

            if new_meas:
                meas = measurement.Measurement( firstSample=actualSample,
                                                firstTimeStamp=actualTimeStamp,
                                                maxDeviation=self.setup_dict["maxDeviation"],
                                                sampleLength=self.setup_dict["sampleLength"],
                                                averageSample=actualSample,
                                                totalSample=actualSample,
                                                averageAmbient=actualAmbient,
                                                totalAmbient=actualAmbient,
                                                averageCapacity=actualCapacity,
                                                totalCapacity=actualCapacity,
                                                )
                new_meas = not new_meas
                next
            
            deviation = abs((actualSample/meas.firstSample)-1)
            if deviation <= meas.maxDeviation or meas.firstSample == 0.0:
                
                meas.sampleCounter += 1
                meas.totalSample += actualSample
                meas.averageSample = meas.totalSample/meas.sampleCounter

                meas.totalPower += actualPower
                meas.averagePower = meas.totalPower/meas.sampleCounter

                meas.totalCapacity += actualCapacity
                meas.averageCapacity += meas.totalCapacity/meas.sampleCounter

                meas.totalAmbient += actualAmbient
                meas.averageAmbient = meas.totalAmbient/meas.sampleCounter

            else:
                meas.sampleCounter = 1
                meas.firstSample = actualSample
                meas.totalSample = actualSample
                meas.averageSample = actualSample

                meas.totalPower = actualPower
                meas.averagePower = actualPower

                meas.totalCapacity = actualCapacity
                meas.averageCapacity = actualCapacity
                
                meas.totalAmbient = actualAmbient
                meas.averageAmbient = actualAmbient

            if meas.sampleCounter >= meas.sampleLength:
                self.measurements.append(meas)
                new_meas = True
              
    def convertMeasToDataframe(self):
        variables = list(self.measurements[0].__annotations__.keys())
        return pd.DataFrame([[getattr(i,j) for j in variables] for i in self.measurements], columns = variables)