import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plotter3D():
    def __init__(   self, 
                    plot_title="Default Title", 
                    xyz_labels=["x","y","z"], 
                    xyz_ranges=[[0,100],[0,100],[0,100]], 
                    xyz_values=[[0],[0],[0]], 
                    value_color = 'blue'
                    ) -> None:
                    
        self.plt_title= plot_title
        [self.x_label, self.y_label, self.z_label] = xyz_labels
        [self.x_range, self.y_range, self.z_range] = xyz_ranges
        [self.x_values, self.y_values, self.z_values] = xyz_values
        self.color = value_color

    def plot(self):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111, projection='3d')

        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_zlabel(self.z_label)

        plt.xlim(self.x_range)
        # plt.ylim(self.y_range)
        # plt.zlim(self.z_range)

        ax.scatter(self.x_values,self.y_values, self.z_values, c=self.color)

        plt.title(self.plt_title)

        plt.draw() 