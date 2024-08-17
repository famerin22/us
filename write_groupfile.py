#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt   

with open ("groupfile", "w") as f:
    for i in range (15):    
        f.write("-O -p x.prmtop -c im"+str(i+1)+".rst7 -i md"+str(i+1)+".in -o md"+str(i+1)+".out -r md"+str(i+1)+".rst7 -x md"+str(i+1)+".nc\n")
    f.close()

