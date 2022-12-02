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
    print(meas_df)

    # Initialize Datawarehouse
    dwarehouse = datawarehouse.DataStorage( class_setup_dict=setup_dict["Data"], 
                                            df_meas=meas_df)

    # Initialize Storage withing Datawarehouse
    dwarehouse.initStorage()

    # Populate Measurement Landscape within Datawarehouse
    dwarehouse.populateMeasLandscape()

    ## Plot Measurement Landscape of Datawarehouse
    fig = plt.figure()
    upperLimitEnergy=  50
    upperLimitPower=  250

    # Subplot1
    ax1 = fig.add_subplot(2,3,1,projection='3d')
    ax1.set_xlabel('Tambient [°C]')
    ax1.set_ylabel('Capacity [W]')
    ax1.set_zlabel('COP [-]')
    ax1.set_xlim(setup_dict['Data']['AmbientRange'])
    ax1.set_ylim(setup_dict['Data']['CapacityRange'])
    ax1.set_zlim(setup_dict['Data']['COPRange'])
    ax1.set_title('Point Cloud Data')

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
    ax2.set_zlim([0.0, meas_df.shape[0]])
    ax2.set_title('Nr. of Meas')
    x,y,z = dwarehouse.process(proc=0)
    ax2.scatter(x,y,z)

    # #Subplot3
    ax3 = fig.add_subplot(2,3,3,projection='3d')
    ax3.set_xlabel('Tambient [°C]')
    ax3.set_ylabel('Capacity [W]')
    ax3.set_zlabel('COP [-]')
    ax3.set_xlim(setup_dict['Data']['AmbientRange'])
    ax3.set_ylim(setup_dict['Data']['CapacityRange'])
    ax3.set_zlim(setup_dict['Data']['COPRange'])
    ax3.set_title('COP\'s')
    x,y,z = dwarehouse.process(proc=1)
    ax3.scatter(x,y,z)

    # #Subplot4
    ax4 = fig.add_subplot(2,3,4,projection='3d')
    ax4.set_xlabel('Tambient [°C]')
    ax4.set_ylabel('Capacity [W]')
    ax4.set_zlabel('Power [kW]')
    ax4.set_xlim(setup_dict['Data']['AmbientRange'])
    ax4.set_ylim(setup_dict['Data']['CapacityRange'])
    ax4.set_zlim([0.0, upperLimitPower])
    ax4.set_title('Avg. Power')
    x,y,z = dwarehouse.process(proc=2)
    ax4.scatter(x,y,z)

    # #Subplot5
    ax5 = fig.add_subplot(2,3,5,projection='3d')
    ax5.set_xlabel('Tambient [°C]')
    ax5.set_ylabel('Capacity [W]')
    ax5.set_zlabel('Energy [kWh]')
    ax5.set_xlim(setup_dict['Data']['AmbientRange'])
    ax5.set_ylim(setup_dict['Data']['CapacityRange'])
    ax5.set_zlim([0.0, upperLimitEnergy])
    ax5.set_title('ConsumptionP Energy')
    x,y,z = dwarehouse.process(proc=3)
    ax5.scatter(x,y,z)

    # #Subplot6
    ax6 = fig.add_subplot(2,3,6,projection='3d')
    ax6.set_xlabel('Tambient [°C]')
    ax6.set_ylabel('Capacity [W]')
    ax6.set_zlabel('Energy [kWh]')
    ax6.set_xlim(setup_dict['Data']['AmbientRange'])
    ax6.set_ylim(setup_dict['Data']['CapacityRange'])
    ax6.set_zlim([0.0, upperLimitEnergy])
    ax6.set_title('ProductionQ Energy')
    x,y,z = dwarehouse.process(proc=4)
    ax6.scatter(x,y,z)

    fig.suptitle("Data Analytics Per Situation")
    plt.show()

if __name__ == "__main__":
    execute()