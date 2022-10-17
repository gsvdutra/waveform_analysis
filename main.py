import numpy as np
from plotter import DataPlotter
from function_predict import FunctionPredict
from settings import Settings
import pandas as pd
from csv_parser import CsvParser

# Load config data
settings = Settings().load_config().data[0]

char_displacement_ascii = ord('A')
x_column = ord(settings.options.x_column[0]) - char_displacement_ascii
y_column = ord(settings.options.y_column[0]) - char_displacement_ascii

csv_parser = CsvParser()
csv_parser.set_current_csv_file('data.csv')
csv_parser.load_valid_data_from_columns([x_column, y_column])

if (settings.remove_mean):
    csv_parser.remove_mean_from_data(x_column)
if (settings.treshold is not None):
    csv_parser.remove_data_bellow_treshold(
        upper_treshold = settings.treshold.upper, 
        lower_treshold = settings.treshold.lower, 
        column = y_column
    )

xData = csv_parser.df.iloc[:,x_column].values 
xData -= xData[0]
yData = csv_parser.df.iloc[:,y_column].values

# Generate data
#xData = np.linspace(0, 1232, 500)
#yData = np.array([2*i for i in xData])
#yData = np.array([2*np.sin(np.deg2rad(i)) for i in xData])
#yData = np.array([2*i*np.sin(np.deg2rad(i)) for i in xData])

function_predict = FunctionPredict()
[best_fit, best_fit_parameters] = function_predict.find_best_fit(xData, yData)
print(best_fit.name)

DataPlotter.plot_results(
    best_fit, 
    best_fit_parameters,
    xData,
    yData,
)