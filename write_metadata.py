import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import math

df1 = pd.read_csv('r11.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r11"]) 
df2 = pd.read_csv('r12.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r12"])
df3 = pd.read_csv('r21.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r21"])
df4 = pd.read_csv('r22.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r22"])

difference_1 = df1["r11"] - df2["r12"]
difference_2 = df3["r21"] - df4["r22"]
print (difference_1)
print (difference_2)

cte= 500.0*2 

with open ("metadata.dat", "w") as f:
    for i in range (len(difference_1)):    
        f.write("/home/usuario/pruebas/wham2d/restraint_"+str(i+1)+".dat "+str(round(difference_1[i],2))+" "+str(round(difference_2[i],2))+" "+str(round(cte,3))+" "+str(round(cte,3))+"\n")
        f.close

