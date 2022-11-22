import pandas as pd


class DataRetriever():
    def __init__(self, file_location, delimiter, class_setup_dict) -> None:
        self.file = file_location
        self.delimiter = delimiter
        self.df = pd.read_csv(self.file, delimiter=self.delimiter)
        self.setup_dict = class_setup_dict

        self.cleanData()


    def cleanData(self):
        if not self.df.shape[0] == len(self.setup_dict["Column Headers"]):
            self.df = self.df.transpose()

        self.df.columns = self.df.iloc[0]
        self.df = self.df.drop(self.df.index[0])
        
        self.df = self.df.dropna()
        self.df = self.df.reset_index()
        
        self.df[self.setup_dict['Column Headers'][1]]= self.chageColumnTypeTo(1,str)
        self.df[self.setup_dict['Column Headers'][2]]= self.chageColumnTypeTo(2,str)
        self.df[self.setup_dict['Column Headers'][3]]= self.chageColumnTypeTo(3,str)
        
        self.df[self.setup_dict['Column Headers'][1]]=self.df[self.setup_dict['Column Headers'][1]].str.replace(',','.')
        self.df[self.setup_dict['Column Headers'][2]]=self.df[self.setup_dict['Column Headers'][2]].str.replace(',','.')
        self.df[self.setup_dict['Column Headers'][3]]=self.df[self.setup_dict['Column Headers'][3]].str.replace(',','.')
        
        self.df[self.setup_dict['Column Headers'][1]]= self.chageColumnTypeTo(1,float)
        self.df[self.setup_dict['Column Headers'][2]]= self.chageColumnTypeTo(2,float)
        self.df[self.setup_dict['Column Headers'][3]]= self.chageColumnTypeTo(3,float)


    def chageColumnTypeTo(self, colNr, type):
        return self.df[self.setup_dict['Column Headers'][colNr]].astype(type)
        