from .classtemplate import ClassTemplate
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