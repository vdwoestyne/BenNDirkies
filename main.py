from Dictionary import dataretriever, datahandler, dataplotter, datawarehouse
from matplotlib.widgets import Slider, RangeSlider, Button
import matplotlib.pyplot as plt
import json

def execute():
    setup_file = open(".\\Dictionary\\setup.json")
    setup_dict = json.load(setup_file)
    raw_data = dataretriever.DataRetriever( file_location=".\\TestData2.csv",
                                        delimiter=";", 
                                        class_setup_dict=setup_dict["Raw Data"]
                                        ).df
    
    dhandler = datahandler.DataHandler(  raw_data=raw_data, 
                                            class_setup_dict=setup_dict["Measurement"]
                                        )
    dhandler.handleData()
    meas_df = dhandler.convertMeasToDataframe()
    print(meas_df)

    # print(meas_df)
    # dplot2DIon = dataplotter.Plotter2DIon(  df=meas_df,
    #                                         xy_label=["Tambient", "COP"],
    #                                         class_setup_dict=setup_dict["Data"],
    #                                         plot_title="COP in functie van Ambient Temperature",
    #                                         ).plotIon()
                                            
    # plot(meas_df, xy_label=["Tambient", "COP"], setup_dict=setup_dict["Data"])

    
def plot(meas_df, xy_label, setup_dict, plot_title=""):
    
    # rng = [1000,1100]
    # df_part = meas_df.loc[meas_df["averageCapacity"].between(*rng)]
    # x,y = list(df_part['averageAmbient']), list(df_part["averageSample"])

    # fig, axs = plt.subplots(1,1, figsize=(10,5))

    # axs[0] = 


    # plt.scatter(x,y)
    # plt.title = "COP w.r.t. Tambient for Q in range {}-{} W".format(rng[0], rng[1])
    # plt.xlabel(xlabel=xy_label[0])
    # plt.ylabel(ylabel=xy_label[1])
    # plt.xlim(setup_dict["AmbientRange"][0],setup_dict["AmbientRange"][1])
    # plt.ylim(setup_dict["COPRange"][0], setup_dict["COPRange"][1])
    # # plt.legend()
    # plt.grid()
    
    # plt.show()
    pass    

if __name__ == "__main__":
    execute()