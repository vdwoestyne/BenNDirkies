from .classtemplate import ClassTemplate
import numpy as np

class DataStorage(ClassTemplate):
    def __init__(self, class_setup_dict) -> None:
        super().__init__(class_setup_dict)
        self.bins_ambient = None
        self.bins_capacity = None
        self.bins_COP = None

    def initStorage(self):                                    
        self.bins_ambient = self.createRange(self.setup_dict["AmbientRange"][0], self.setup_dict["AmbientRange"][1], self.setup_dict["stepAmbient"])
        self.bins_capacity = self.createRange(self.setup_dict["CapacityRange"][0], self.setup_dict["CapacityRange"][1], self.setup_dict["stepCapacity"])
        self.bins_COP = self.createRange(self.setup_dict["COPRange"][0], self.setup_dict["COPRange"][1], self.setup_dict["stepCOP"])
       
        
    def createRange(self, start, stop, inc=1):
        return np.arange(start,stop+inc,inc)