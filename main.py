from Dictionary import dataretriever, datahandler, dataplotter, datawarehouse
from matplotlib.widgets import Slider, RangeSlider, Button
import matplotlib.pyplot as plt
import numpy as np
import json

def execute():

    ## Initialize setup Configuratio file.json
    # Open up setup.json file
    setup_file = open(".\\Dictionary\\setup.json")

    # Extract the setup dictionary from the setup.json with json.load
    setup_dict = json.load(setup_file)

    # Extract raw data from CSV into pandas.Dataframe-format
    raw_data = dataretriever.DataRetriever( file_location=".\\TestData2.csv",
                                        delimiter=";", 
                                        class_setup_dict=setup_dict["Raw Data"]
                                        ).df
    
    # Initialize Datahandler 
    dhandler = datahandler.DataHandler( raw_data=raw_data, 
                                        class_setup_dict=setup_dict["Measurement"]
                                        )

    # Activate the data handler
    dhandler.handleData()

    # Retract the pandas.Dataframe with the filtered Measurementpoints
    meas_df = dhandler.convertMeasToDataframe()
    
    # Show pandas.Dataframe of MeasurementPoints
    print(meas_df.head())

    # Initialize Datawarehouse
    dwarehouse = datawarehouse.DataStorage( class_setup_dict=setup_dict["Data"], 
                                            df_meas=meas_df)

    # Initialize Storage withing Datawarehouse
    dwarehouse.initStorage()

    # Populate Measurement Landscape within Datawarehouse
    dwarehouse.populateMeasLandscape()

    # print(dwarehouse.Measurements_landscape)
    print(dwarehouse.process())

    # meas_df.plot(x='averageAmbient', y='averageCapacity', z='averageSample', kind='scatter')
    # plt.show()
    ## Plot Measurement Landscape of Datawarehouse
    fig = plt.figure()

    # Subplot1
    ax1 = fig.add_subplot(2,3,1,projection='3d')
    ax1.set_xlabel('Tambient [°C]')
    ax1.set_ylabel('Capacity [W]')
    ax1.set_zlabel('COP [-]')
    ax1.set_xlim(setup_dict['Data']['AmbientRange'])
    ax1.set_ylim(setup_dict['Data']['CapacityRange'])
    ax1.set_zlim(setup_dict['Data']['COPRange'])
    
    x,y,z = [
            list(meas_df['averageAmbient']),
            list(meas_df['averageCapacity']),
            list(meas_df['averageCOP'])
            ]
    ax1.scatter(x,y,z)

    #Subplot2
    ax2 = fig.add_subplot(2,3,2,projection='3d')
    ax2.set_xlabel('Tambient [°C]')
    ax2.set_ylabel('Capacity [W]')
    ax2.set_zlabel('Nr. of Meas. [#]')
    ax2.set_xlim(setup_dict['Data']['AmbientRange'])
    ax2.set_ylim(setup_dict['Data']['CapacityRange'])
    ax2.set_zlim(setup_dict['Data']['COPRange'])

    x,y,z = dwarehouse.process(proc=1)
    ax2.scatter(x,y,z)

    # #Subplot3
    # ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
    # ax3.set_title = ""
    # ax3.set(xlabel="", ylabel="")

    # #Subplot4
    # ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
    # ax4.set_title = ""
    # ax4.set(xlabel="", ylabel="")

    # #Subplot5
    # ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)
    # ax5.set_title = ""
    # ax5.set(xlabel="", ylabel="")

    fig.suptitle("Data Analytics")
    plt.show()

if __name__ == "__main__":
    execute()