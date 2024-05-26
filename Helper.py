import functools
import threading
import matplotlib.pyplot as plt
import numpy as np
import time, datetime 

#a vector of standard normal variables
def stdNormal(shape):
    #return np.array([-0.69511166,-2.25442564,0.56286789,-0.67288228,0.58605277,2.0122941,0.07528879,0.3352865,0.72428062,-1.13506461,2.1739821,0.28026353,-0.10277649,2.01482385,-0.2705569,0.90480372,-1.36964219,0.74224638,1.09706617,0.18001245,-2.09024943,-0.03243608,2.74061983,-0.35022726,-0.10823543,1.89083485,-0.27594371,-0.24193671,-0.15853338,-1.97768694,1.26467866,0.16575812,-0.37737465,-1.85474389,1.52383889,-1.30428544,0.28419197,-2.64291795,-0.48269691,-1.94674713,0.02677038,2.09714116,-0.64712907,0.82669255,-1.76665483,-1.339802,-0.42387499,-0.06360226,0.50896399,0.26715213,0.64841311,0.04387311,-0.29551041,-0.31612793,-1.29547972,0.51577754,-0.37826052,1.52981799,-1.05717633,0.05065605,-1.09062576,1.81271648,0.71953656,1.86212085,0.42922757,0.84882177,-1.34745368,-0.44444672,-0.12616003,2.18826138,1.10751477,-0.49274679,-0.68418851,1.5048691,-0.17685499,0.67983191,0.76565422,-0.41400026,-0.09092187,-1.00399145,0.97840073,0.47312952,1.03253265,0.11677718,0.21954567,0.14175459,0.41899549,-0.4067415,-1.08410176,1.02381477,-1.29799996,-0.52320722,0.35008901,-0.07839458,-1.24280537,1.44192172,0.31563991,0.88749338,2.62853982,2.13468057,1.39909804,-0.23974188,2.75596203,0.21905443,1.14264956,-0.06104295,-1.51835881,-1.94758327,1.22147177,1.19064103,-0.92646949,0.13483907,-0.23747524,-1.74905336,1.75266344,-0.69317285,0.50661797,1.36896053,-0.59770515,0.06269847,-1.49061146,0.42244233,1.40417306,0.07310747,0.97228245,0.25762379,-0.04495436,0.1487119,0.72502882,-1.12327356,0.18844487,-2.27443516,0.59450789,-1.90238467,-1.40798399,0.34720394,-1.11003429,-0.45963995,1.01719479,1.07764809,0.36522999,0.2367714,0.39940647,0.91219808,-0.49237218,0.202169,-0.54878203,-0.17301365,-0.86970634,-1.22444188,-1.02991171,0.27796334,0.68972834,-2.00760947,1.89467904,-2.0196429,0.38754869,0.00446748,0.57910423,-0.44892674,0.47997578,0.83401689,0.99035205,-1.56708476,0.69317297,-0.61376998,-0.17772125,-0.90382938,-0.41271823,-1.09736836,0.74757685,-1.766127,-0.04211907,0.93387941,0.44321372,-1.34692592,-1.06281018,1.6279536,1.70454878,-0.04040953,0.64489809,0.64211786,-0.31326777,-0.39155812,-0.34664311,0.96118807,-1.43702067,0.63544725,1.06716021,-0.71946547,0.48057941,-1.15305154,1.78086149,-0.09707811,-1.45390619,-2.37259495,-0.01787142,0.34608555,0.83625555,-0.0123965,0.09879391,1.17146678,0.48092022,-1.4584915,0.14152949,-0.20813464,-1.54941927,1.15907616,0.48169647,0.40814776,-0.54507841,-0.11265492,-0.60435679,1.155282,0.69775105,-0.34100741,0.5950456,0.79102352,1.62252625,-1.41369786,0.75996145,-0.79037586,1.3216341,-0.9979197,0.01675937,0.19896522,-2.50202576,1.27353607,0.39363003,-0.33251165,-1.30373926,0.28227662,-0.52179692,0.83242528,0.81675199,-0.0255081,-0.33892845,1.15886367,-1.16362767,-0.13218565,-0.82094275,0.69528499,1.03394082,0.09842689,-1.04326808,-1.0014308,-0.90603,-1.97692126,-0.4624485,1.1986837,-1.50175481,-1.26016696,-0.36176141,-0.00910921,0.10836029,-0.53370966,0.34612513,-1.34667633,-0.40238391,0.7710441,0.31856918,-1.35975657,-0.29317777,-1.5050641,0.160843,1.69474572,-0.35242884,0.04448567,0.26593628,2.08686027,-1.05290094,-1.03479679,0.08084663,-1.34396698,-0.06382878,1.80256644,1.29417419,0.69085266,0.02740956,1.36152057,-0.43807682,0.09633801,-0.42813157,-1.33149808,-1.03865708,1.4838105,-0.02982876,-0.83331239,-0.22949506,1.28893858,-0.07529384,1.29863923,-0.19345242,-0.07507259,1.10111043,-0.96960371,1.74566985,-1.94202727,-0.80018655,0.20482053,0.00456483,0.70571893,-1.2925935,-1.37845106,0.68338011,0.38277322,-0.74274969,1.19732658,-0.83672394,-1.21524409,-2.50175144,-0.16555866,-0.46397151,0.67195086,0.80407337,-0.51200714,0.06856244,0.22548368,1.07042914,-0.21549803])
    return np.random.default_rng().standard_normal(size=shape)

#plot function
def plotSP(data):
    #Remove loop and implement direct plot
    for dat in data:
        plt.plot(dat)
    plt.savefig("plt.png") 
    plt.clf()   

class timer:     
    tick = datetime.datetime.now()
    tock = datetime.datetime.now()
    def start(self):
        self.tick = time.time()
    def stop(self):
        self.tock = datetime.datetime.now()
        print("--- %s seconds ---" % (time.time() - self.tick)) 
       
#test individuals function calls from the class
def unitTest(myClass):
    pass

def discretize(arr, num):
    arr = np.concatenate([[0], arr])
    for i in range(num):
        arr = np.sort(np.concatenate([arr,np.add(arr[:-1],np.diff(arr)/2)]))
    return arr

def plot():
    plt.savefig("plot")
    plt.show()

def synchronized(wrapped):
    lock = threading.Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)
    return _wrap