import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import math
import write_rst



def makeFile(path, imgs):
    root = "/home/noosh/fer_recuperado/Compuestos_nati/SinComp/noRNA/US/"

    # df1 = pd.read_csv('r11.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r11"])
    # df2 = pd.read_csv('r12.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r12"])
    # df3 = pd.read_csv('r21.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r21"])
    # df4 = pd.read_csv('r22.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r22"])

    # difference_1 = df1["r11"] - df2["r12"]
    # difference_2 = df3["r21"] - df4["r22"]
    # print (difference_1)
    # print (difference_2)

    df = pd.read_csv(root + path+"dists.dat", skiprows=1, delimiter='\s+', names = ["Frame", "dist"])
    df = df["dist"]

    cte= float(write_rst.const)*2

    with open (root + path + "metadata.dat", "w") as f:
        for i in imgs:
            f.write(root+path+"wham/"+str(i)+".dat "+str(round(df[i-1],2))+" "+str(round(cte,3))+"\n")
            f.close

apoimgs = [1, 2, 3, 7, 12, 17, 21, 30, 31, 35, 48]
ATPimgs = [1, 4, 6, 7, 12, 21, 23, 28, 31, 39, 40, 44]

makeFile("apo/", apoimgs)
makeFile("ATP/", ATPimgs)
