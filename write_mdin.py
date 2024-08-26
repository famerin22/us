import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

def makeFile(path, imgs):
    root = "/home/noosh/fer_recuperado/Compuestos_nati/SinComp/noRNA/US/"
    for i in imgs:
        with open (root + path + "md"+str(i)+".in", "w") as f:
            f.write("MD MM T cte Ventana "+str(i)+"""
    &cntrl
    imin=0,
    ntx=1,irest=0,
    ntwr=200, ntpr=100, ntwx=100, ntwv=0, ntwe=0, iwrap=0, ioutfm=1, ntxo=1,
    nstlim=10000, dt=0.001, nrespa=1,
    nmropt=1, 	!prende restraint
    ntt=3, tempi=300.0, temp0=300.0, gamma_ln=5.0, ig=-1,
    ntp=0, pres0=1.0, taup=1.0,
    ntc=1, ntf=1, ntb=1, cut=10.0, ifqnt=1, igb=0,
    /
    &wt type='DUMPFREQ', istep1=1, /
    &wt type='END', /
    DISANG= restraint_"""+str(i)+""".rst
    DUMPAVE= restraint_"""+str(i)+""".dat
    """)

        f.close()
apoimgs = [1, 2, 3, 7, 12, 17, 21, 30, 31, 35, 48]
ATPimgs = [1, 4, 6, 7, 12, 21, 23, 28, 31, 39, 40, 44]

makeFile("apo/", apoimgs)
makeFile("ATP/", ATPimgs)
