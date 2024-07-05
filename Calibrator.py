import numpy as np
from DerivativePricer import DerivativePricing
import Helper as hp
from scipy.optimize import minimize

from LIBORSimulator import LIBORSim
from Parameters import Parameters
from PricingEngine import PricingEngine

class Calibrator:
    def __init__(self, pricer : DerivativePricing):
        print("Calibrator::init")
        self.pricer = pricer  
        Calibrator.volHist = list()

    @property
    def pricer(self):
        return self._pricer

    @pricer.setter
    def pricer(self, value:  DerivativePricing):
        self._pricer = value

    def calibrate(self):
        print("Calibrator::calibrate")
        vol = self.optimize()
        #hp.plotNP(Calibrator.volHist, title="Volatility History", clear=False)
        print("Calibrator::calibrate: RESULT", vol)
        return vol
    
    def objectiveFunc(volatility, pricer):                                                                     
        print("Calibrator::objectiveFunc", volatility, pricer)
        Calibrator.volHist.append(volatility)
        pricer.estimate(volatility)
        estimates: np.array = pricer.simulatedPrice                                                                                                                                   
        grounds: np.array = pricer.marketPrice
        print("Calibrator::objectiveFunc: ", "est: ", estimates, "gr: ", grounds)
        squared_diff = np.sum((estimates - grounds)**2)
        return squared_diff

    def optimize(self):
        print("Calibrator::optimize")
        initVol = Parameters.intervalVolatility
        result = minimize(fun=Calibrator.objectiveFunc, x0=initVol,
                  args=(self.pricer),
                  method='BFGS', options={'disp': True})
        return result.x
    
    
