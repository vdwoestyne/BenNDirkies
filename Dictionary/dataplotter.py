from .classtemplate import ClassTemplate
import numpy as np
from matplotlib.widgets import Slider, RangeSlider, Button
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plotter(ClassTemplate):
    def __init__(   self, 
                    class_setup_dict,
                    plot_title="Default Title", 
                    value_color = 'blue',
                    ) -> None:
        super().__init__(class_setup_dict)
                    
        self.plt_title= plot_title
        self.color = value_color

    def plot(self):
        pass

class Plotter3D(Plotter):
    def __init__(   self, 
                    plot_title="Default Title", 
                    xyz_labels=["x","y","z"], 
                    xyz_ranges=[[0,100],[0,100],[0,100]], 
                    xyz_values=[[0],[0],[0]], 
                    value_color = 'blue'
                    ) -> None:
        super().__init__(plot_title, value_color)

        [self.x_label, self.y_label, self.z_label] = xyz_labels
        [self.x_range, self.y_range, self.z_range] = xyz_ranges
        [self.x_values, self.y_values, self.z_values] = xyz_values

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_zlabel(self.z_label)

        plt.xlim(self.x_range)
        # plt.ylim(self.y_range)
        # plt.zlim(self.z_range)

        ax.scatter(self.x_values,self.y_values, self.z_values, c=self.color)
        plt.title(self.plt_title)
        plt.show()

class Plotter2D(Plotter):
    def __init__(   self, 
                    xy_values=[[0],[0]], 
                    xy_ranges=[[0,100],[0,100]], 
                    xy_labels=["x","y"], 
                    plot_title="Default Title", 
                    value_color='blue') -> None:

        super().__init__(plot_title, value_color)

        [self.x_label, self.y_label] = xy_labels
        [self.x_range, self.y_range] = xy_ranges
        [self.x_values, self.y_values] = xy_values

    def plot(self):
        pass


class Plotter2DIon(Plotter):
    def __init__(self, class_setup_dict, df, xy_label=["x","y"], plot_title="Default Title", value_color='blue') -> None:
        super().__init__(class_setup_dict, plot_title, value_color)
        self.df = df
        self.xy_label = xy_label


    def plotIon(self):
        # df_part = self.df.loc[(self.df["averageCapacity"]>1000) & (self.df["averageCapacity"]<=1100), ["averageAmbient", "averageSample"]]
        rng = [1000,1100]
        df_part = self.df.loc[self.df["averageCapacity"].between(*rng)]
        x,y = list(df_part['averageAmbient']), list(df_part["averageSample"])

        fig = plt
        fig.scatter(x,y)

        # plt.scatter(x,y)
        fig.title = self.plt_title
        # plt.xlabel = "teste" #self.xy_label[0]
        # plt.ylabel = self.xy_label[1]
        fig.show()









        # plt.subplots_adjust(left=0.25, bottom=0.25)
        # t_ambient = np.arange(self.setup_dict["AmbientRange"][0], self.setup_dict["AmbientRange"][0] + self.setup_dict["stepAmbient"], self.setup_dict["stepAmbient"])
        



        # plt.scatter(x,y, label="test1")
        # plt.legend(["COP(Ta) for Capacity of {} W".format(str(1))])
        # plt.title = self.plt_title
        # plt.xlabel = "teste" #self.xy_label[0]
        # plt.ylabel = self.xy_label[1]
        # plt.xlim(self.setup_dict["AmbientRange"][0], self.setup_dict["AmbientRange"][1])
        # plt.ylim(self.setup_dict["COPRange"][0], self.setup_dict["COPRange"][1])
        # plt.grid()
        # plt.show()