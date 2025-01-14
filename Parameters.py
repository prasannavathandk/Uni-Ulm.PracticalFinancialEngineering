import math

class Parameters:

    measures = {
            'SpotMeasure': 0,
            'ForwardMeasure': 1
        }
    
    schemes = {
            'General': 0,
            'Martingale': 1
        }

    derivatives = {
        'ZeroCouponBond': {
            'Maturity': 10,  # Maturity in years
            'FaceValue': 100,  # Face Value of Bond
            'Price': 90,  # Price of Bond
            'YieldRate': 5,  # Yield of Bond,
            'CouponRate': 0,  # Coupon Rate
            'riskFreeRate': 3,  # Risk Free Rate,
            'Payoff': None
        },
        'VanillaCouponBond': {

        },
        'Caplet': {
            'Exercise': 'European',
            'Type': 'Payer',
            'Frequency': 1,  # Annually
            'DiscountFactor': 0.95,  # Discount Factor
            'Notional': 1000000,
            'StrikeType': 'ATM',  # Same as the forward rate at that time
            'Strike': None,  # Swap/Fixed Rate
            'Tenor': 10,  # Interest Rate Swap Tenor
            'Maturity': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Option maturity (exercies) dates in years
            'Volatility': [31.15, 30.77, 29.98, 29.51, 29.12, 29.09, 29.21, 29.35, 29.57],
            'sigma': [10]*9,
            'ForwardRate': [0.29067, 0.69631, 1.307513, 2.339118, 2.293654, 0.267757, 0.130832, 2.610498, 5.584448],  # Forward Rate at time of exercise
            'RiskFreeRate': 3,
            'MarketBond':[0.95141468, 0.91125283, 0.87517107, 0.84101834, 0.80781669, 0.7752033 , 0.74311992, 0.71164181, 0.68088708, 0.65097184],
            'Price': None,
            'Payoff': lambda floating, fixed, period: max((floating - fixed), 0) * (period),
            'BondPricing': lambda faceValue, yieldRate, maturity: [fv/(1 + y/100)**n for n, fv, y in zip(maturity, faceValue, yieldRate)]
        },
        'Swaption': {
            'Exercise': 'European',
            'Type': 'Payer',
            'Frequency': 1,  # Annually
            'DiscountFactor': 0.95,  # Discount Factor
            'Notional': 1000000,
            'StrikeType': 'ATM',  # Same as the forward rate at that time
            'Strike': None,  # Swap/Fixed Rate
            'Tenor': 10,  # Interest Rate Swap Tenor
            'Maturity': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Option maturity (exercies) dates in years
            'Volatility': [31.15, 30.77, 29.98, 29.51, 29.12, 29.09, 29.21, 29.35, 29.57],
            'ForwardRate': [0.29067, 0.69631, 1.307513, 2.339118, 2.293654, 0.267757, 0.130832, 2.610498, 5.584448],  # Forward Rate at time of exercise
            'RiskFreeRate': 3,
            'Price': None,
            'Payoff': lambda floating, fixed, period, notional: (floating - fixed) * (1/(1 + period*floating)) * notional,
            'BondPricing': lambda faceValue, yieldRate, maturity: [fv/(1 + y/100)**n for n, fv, y in zip(maturity, faceValue, yieldRate)]
        }
    }
    
    #Input Data to Simulation
    maturityDates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    #Maturity Dates in years
    resetPeriod = 0.25        #Reset Period of 3 months
    faceValue = 100           #Face Value of Bond
    yieldRate = 5             #Yield of Bond
    _faceValue = [faceValue]*len(maturityDates)
    _yieldRate = [yieldRate]*len(maturityDates)                 #Yield Curve
    volatility = 2.52           #Annual Volatility in percent
    intervalVolatility = ([volatility/100]*len(maturityDates[:-1])*len(maturityDates[:-1]))
    bondPrices = [fv/(1 + y/100)**n for n, fv, y in zip(range(1,len(maturityDates)+1), _faceValue, _yieldRate)]
    capletPrices = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]  #Caplet Prices
    riskFreeRate = 3            #Risk Free Rate in percent
    tradingDays = 252           #Number of trading days in a year

    measure = measures['SpotMeasure']
    scheme = schemes['General'] 
    derivative = derivatives['Swaption']
        
    #Simulation Parameters
    epoch = 5      #Number of epochs or batches to run
    batch = lambda core: 5*core        #Number of iterations per epoch = Number of sample paths
    parallel = True     #Flag to run the simulation in parallel
    

    

