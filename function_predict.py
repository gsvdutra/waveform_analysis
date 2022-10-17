from functions import *
from typing import List

class FunctionPredict:

    ACCEPTABLE_PREDICTION_R_VALUE = 0.9

    available_functions = [
        Sinus(),
        XSinus(),
        Linear(),
    ]

    def find_best_fit(self, xData, yData):
        current_r_squared = 0
        current_best_fit = 0
        current_best_prediction = []
        for i, function in enumerate(self.available_functions):
            
            fit, abs_error = self._predict(xData, yData, function)

            r_squared = abs(1.0 - (np.var(abs_error) / np.var(yData)))

            self._show_results(fit, abs_error, r_squared, function)

            if current_r_squared < r_squared:
                current_r_squared = r_squared
                current_best_fit = i
                current_best_prediction = fit

            if current_r_squared > self.ACCEPTABLE_PREDICTION_R_VALUE:
                break
            
        return [self.available_functions[current_best_fit], current_best_prediction]

    @staticmethod
    def _predict(xData, yData, function):
        fit = function.curve_fit(
                xData = xData, 
                yData = yData,
            )

        model_prediction = function.fit_function(xData, *fit) 

        abs_error = model_prediction - yData

        return [fit, abs_error]

    @staticmethod
    def _show_results(fit, abs_error, r_squared, function):
        
        squares_error = np.square(abs_error) # squared errors
        mean_squares_error = np.mean(squares_error) # mean squared errors
        root_mean_square_error = np.sqrt(mean_squares_error) # Root Mean Squared Error, RMSE
        
        print('Function: {}'.format(function.name))
        print('Parameters: {}'.format(fit))
        print('RMSE: {}'.format(root_mean_square_error))
        print('R-squared: {}\n'.format(r_squared))