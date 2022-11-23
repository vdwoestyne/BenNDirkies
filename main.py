from Dictionary import dataretriever, datahandler, dataplotter, datawarehouse
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

    dwarehouse = datawarehouse.DataStorage(class_setup_dict=setup_dict["Data"])

    dwarehouse.initStorage()

    print(dwarehouse.bins_ambient)
    print(dwarehouse.bins_capacity)
    print(dwarehouse.bins_COP)

    # dplotter2D = dataplotter.Plotter2D(  plot_title="Raw Data Input",
    #                                     xyz_labels=setup_dict["Raw Data"]["Column Headers"][1:],
    #                                     xyz_ranges=[[0.0,2000.0],
    #                                                 setup_dict["Data"]["CapacityRange"],
    #                                                 setup_dict["Data"]["COPRange"]],
    #                                     xyz_values=[raw_data[setup_dict["Raw Data"]["Column Headers"][1]],
    #                                                 raw_data[setup_dict["Raw Data"]["Column Headers"][2]],
    #                                                 raw_data[setup_dict["Raw Data"]["Column Headers"][3]]
    #                                                 ]).plot()
    

if __name__ == "__main__":
    execute()