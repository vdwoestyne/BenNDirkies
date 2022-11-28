from dataclasses import dataclass
import numpy as np

# Gebruik van een dataclass omdat dit het concept van een "Datapunt" zal vergemakkelijken. 
@dataclass
class Measurement():
    firstSample: float              # First sample of the candidate
    firstTimeStamp: float           # First time stamp
    maxDeviation: float             # I.e. 10% deviation in one meseurement
    sampleCounter: int = 1          # amount of samples in candidate measuremt
    sampleLength: int = 0           # I.e. 10 samples in one meseurement

    averageSample: float = 0.0      # Average of samples in candidate
    totalSample: float = 0.0        # Sum of all samples in candidate

    averagePower: float = 0.0       # Average of power in candidate
    totalPower: float = 0.0         # Sum of all power in candidate

    averageCapacity: float = 0.0    # Average of capacity in candidate
    totalCapacity: float = 0.0      # Sum of all capacity in candidate

    averageAmbient: float = 0.0     # Average of ambient temperature in candidate
    totalAmbient: float = 0.0       # Sum of ambient in candidate

    def __array__(self) -> np.ndarray:
        return np.array([self.sampleLength, 
                        self.averageSample, 
                        self.averagePower, 
                        self.totalPower, 
                        self.averageCapacity,
                        self.totalCapacity,
                        self.averageAmbient,
                        self.totalAmbient])
    pass