from Dictionary import dataretriever, datahandler, dataplotter

import json

def execute():
    setup_file = open(".\\Dictionary\\setup.json")
    setup_dict = json.load(setup_file)
    raw_data = dataretriever.DataRetriever( file_location=".\\TestData2.csv",
                                        delimiter=";", 
                                        class_setup_dict=setup_dict["Raw Data"]
                                        ).df
    dataplot = dataplotter.Plotter3D(   plot_title="Raw Data Input",
                                        xyz_labels=setup_dict["Raw Data"]["Column Headers"][1:],
                                        xyz_ranges=[setup_dict["Data"]["AmbientRange"],
                                                    setup_dict["Data"]["CapacityRange"],
                                                    setup_dict["Data"]["COPRange"]],
                                        xyz_values=[raw_data[setup_dict["Raw Data"]["Column Headers"][1]],
                                                    raw_data[setup_dict["Raw Data"]["Column Headers"][2]],
                                                    raw_data[setup_dict["Raw Data"]["Column Headers"][3]]
                                                    ])
    datahandler.DataHandler(raw_data=raw_data, 
                            class_setup_dict=setup_dict["Measurement"]
                            ).handleData()

if __name__ == "__main__":
    execute()