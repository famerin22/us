import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt   

# df1 = pd.read_csv('r11.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r11"]) 
# df2 = pd.read_csv('r12.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r12"])
# df3 = pd.read_csv('r21.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r21"])
# df4 = pd.read_csv('r22.dat', skiprows=1, delimiter='\s+', names = ["Frame", "r22"])

# dif_dist1 = df1["r11"] - df2["r12"]
# dif_dist2 = df3["r21"] - df4["r22"]



def makeFile(path):
    root = "/home/noosh/fer_recuperado/Compuestos_Nati/SinComp/noRNA/US/"
    path = root + path
    NGLY141 = 2246
    OE1GLU304 = 4820

    df = pd.read_csv(path+"dists.dat", skiprows=1, delimiter='\s+', names = ["Frame", "dist"])
    df = df["dist"]

    for i in range (15):    
        with open (path + "restraint_"+str(i+1)+".rst", "w") as f:
            f.write("restraint ventana "+str(i+1)+"""
    &rst
    iat="""+str(NGLY141)+""","""+str(OE1GLU304)+""", 
    r1="""+str(round(df[i]-20.0,2))+ """,
    r2="""+str(round(df[i],2))+ """, 
    r3="""+str(round(df[i],2))+ """, 
    r4="""+str(round(df[i]+20.0,2))+ """,
    rk2=500,
    rk3=500, 
    /
    &end


    """)

            f.close

makeFile("apo/")
makeFile("ATP/")


