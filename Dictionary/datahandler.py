from .Datastructure import measurement

class DataHandler():
    def __init__(self, raw_data, class_setup_dict) -> None:
        self.raw_data = raw_data
        self.setup_dict = class_setup_dict
        self.measurements = []
        pass

    def handleData(self):
        
        for i in range(1, self.raw_data.shape[0]+1):
            
        pass

    