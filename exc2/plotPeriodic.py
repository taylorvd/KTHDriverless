import numpy as np
from Tkinter import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



class PlotPeriodic:
    """
    Class to produce and plot data given by periodic function 
    """
    def __init__ (self): 

        self.t = 0
        self.y = 0

        
    def get_data(self):
        
        self.t = np.arange(0,1,0.001)
        self.y = (3*np.pi*np.exp(-5*np.sin(2*np.pi*self.t)))
        return self, self.y

    def plot_function(self):
            
        self.get_data()
        plt.plot(self.t, self.y)
        plt.show()

 




class GUIPlot(PlotPeriodic):
    """
    Subclass to use Tkinter GUI with periodic plot
    -used https://www.tutorialspoint.com/how-can-we-run-matplotlib-in-tkinter as reference
    -used code from https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python 
    """

    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()
        self.t = PlotPeriodic.get_data(self)[0]
        self.y = PlotPeriodic.get_data(self)[1]

    def plot (self):

        fig = Figure(figsize=(6,6))
        gui = fig.add_subplot(111)
        gui.plot(self.t, self.y,color='blue')

        gui.set_title ("Periodic Function", fontsize=16)
        gui.set_ylabel("y", fontsize=14)
        gui.set_xlabel("t", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def edit_t_axis(self):
        #implement using tkinter based on this example
        #https://stackoverflow.com/questions/9997869/interactive-plot-based-on-tkinter-and-matplotlib
        pass

    def real_time_plot(self):
        #implement using matplotlib.animation based on this example
        #https://matplotlib.org/stable/api/animation_api.html
        pass

window= Tk()
start= GUIPlot (window)
window.mainloop()











'''
    def plotFigure(self):
        gui = Tk()

        matplotlib.use("TkAgg")
       # figure = Figure()
       # plot = plt.figure.add_subplot(1,1,1)
        figure = PlotPeriodic.plot_function(self)

        canvas = FigureCanvasTkAgg(figure, gui)
        canvas.get_tk_widget().grid(row=0, column=0)
        gui.mainloop()
'''


    #change to button that moves data to csv file




if __name__ == "__main__":

    testGui = GUIPlot()

