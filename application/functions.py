import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Function:

    name = None

    def curve_fit(
        self, 
        xData, 
        yData,
    ):
        pass

    def fit_function(self, *args):
        pass

class Sinus(Function):

    name = "Sinus"
        
    def curve_fit(
        self,
        xData, 
        yData
    ):
        '''
        Fit sin to the input time sequence, and return fitting parameters 
        "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"
        '''
        xData = np.array(xData)
        yData = np.array(yData)
        fourier_frequency = np.fft.fftfreq(len(xData), (xData[1]-xData[0]))   # assume uniform spacing
        FyData = abs(np.fft.fft(yData))
        guess_freq = abs(fourier_frequency[np.argmax(FyData[1:])+1])   # excluding the zero frequency "peak", which is related to offset
        guess_amp = np.std(yData) * 2.**0.5
        guess_offset = np.mean(yData)
        guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])
        
        popt, pcov = curve_fit(self.fit_function, xData, yData, p0=guess)
        #A, w, p, c = popt
        #f = w/(2.*np.pi)
        #fitfunc = lambda t: A * np.sin(w*t + p) + c
        
        #print( "Amplitude=%(amp)s, Angular freq.=%(omega)s, phase=%(phase)s, offset=%(offset)s, Max. Cov.=%(maxcov)s" % res )

        return popt

    @staticmethod
    def fit_function(x, A, w, p, c):  
        return A * np.sin(w*x + p) + c

class XSinus(Sinus):

    name = "Raising Sinus"

    @staticmethod
    def fit_function(x, A, w, p, c):  
        return A * x * np.sin(w*x + p) + c
    #def curve_fit_old(
    #    self, 
    #    xData, 
    #    yData,
    #):
    #    initial_point = yData[0]
    #    initialParameters = np.array([-1.0, 180.0, 180.0, initial_point])
    #    fit, pcov = curve_fit(self.fit_function, xData, yData, initialParameters)
    #    return fit

    #def fit_function_old(self, x, amplitude, center, width, displacement):
    #    return amplitude * x * np.sin(np.pi * (x - center) / width) + displacement
        
    

class Linear(Function):

    name = "Linear"

    def curve_fit(
        self, 
        xData, 
        yData,
    ):
        initial_point = yData[0]
        initialParameters = np.array([1.0, initial_point])
        fit, pcov = curve_fit(self.fit_function, xData, yData, initialParameters)
        return fit

    def fit_function(self, x, a, b):
        return a*x + b