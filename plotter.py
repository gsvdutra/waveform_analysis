import numpy as np
import matplotlib.pyplot as plt

from functions import Function

class DataPlotter:
    
    def ModelAndScatterPlot(
        func, 
        fitted_parameters,
        xData,
        yData,
        graphWidth = 800, 
        graphHeight = 600, 
    ):
        f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
        axes = f.add_subplot(111)

        # first the raw data as a scatter plot
        axes.plot(xData, yData,  'D')

        # create data for the fitted equation plot
        xModel = np.linspace(min(xData), max(xData))
        yModel = func(xModel, *fitted_parameters)

        # now the model as a line plot
        axes.plot(xModel, yModel)

        axes.set_xlabel('X Data') # X axis data label
        axes.set_ylabel('Y Data') # Y axis data label

        plt.show()
        plt.close('all') # clean up after using pyplot

    def plot_results(
        func : Function,
        fitted_parameters,
        xData,
        yData,
    ):
        N = xData.size
        fig, axs = plt.subplots(2)
        fig.suptitle(func.name)
        axs[0].plot(xData, yData, "-k", label="y", linewidth=2)
        axs[1].plot(xData, func.fit_function(xData, *fitted_parameters), "r-", label="y fit curve", linewidth=2)
        for ax in axs:
            ax.legend(loc="upper right")
        plt.show()
        plt.close() 