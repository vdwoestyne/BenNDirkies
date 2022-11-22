from .Datastructure import measurement

class DataHandler():
    def __init__(self, raw_data, class_setup_dict) -> None:
        self.raw_data = raw_data
        self.setup_dict = class_setup_dict
        self.measurements = []
        pass

    def handleData(self):
        new_meas = True
        for i in range(1, self.raw_data.shape[0]):
            record = self.raw_data.values[i]
            actualSample = record[3]
            actualAmbient = record[1]
            actualCapacity = record[2]
            actualPower = actualCapacity/actualSample

            if new_meas:
                meas = measurement.Measurement( firstSample=actualSample,
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
                

        print(self.measurements)
        print(len(self.measurements))
        pass

    