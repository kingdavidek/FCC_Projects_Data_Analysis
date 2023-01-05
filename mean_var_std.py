import numpy as np

def calculate(list):
    
    calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": [],
    }

    counter = 0
    if len(list) < 9 :
        raise ValueError("List must contain nine numbers.")
        exit
    
    else: 
        ar = np.array(list)
        mar = ar.reshape(3, 3)
        
        #print(calculations)
        
        mean = []
        variance = []
        stdev = []
        maxim = []
        minim = []
        sumof = []
        
        while counter < 2:
            mean.append(np.mean(mar, counter).tolist())
            variance.append(np.var(mar, axis=counter).tolist())
            stdev.append(np.std(mar, axis=counter).tolist())
            maxim.append(np.max(mar, axis=counter).tolist())
            minim.append(np.min(mar, axis=counter).tolist())
            sumof.append(np.sum(mar, axis=counter).tolist())
            counter = counter + 1
            

        mean.append(np.mean(ar))
        variance.append(np.var(ar))
        stdev.append(np.std(ar))
        maxim.append(np.max(ar))
        minim.append(np.min(ar))
        sumof.append(np.sum(ar))
            
        allcalcs = [mean, variance, stdev, maxim, minim, sumof]
        kcounter = 0

        for k in calculations:
            calculations[k] = allcalcs[kcounter]
            kcounter = kcounter + 1
    
    return calculations

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
calculate(list)