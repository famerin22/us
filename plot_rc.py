import numpy as np
import matplotlib.pyplot as plt
import os

def converter(val):
    try:
        if float(val) > 30:
            return 30
        else:
            return float(val)
    except ValueError:
        return 30

def makePlot(path, ylims):

    figure, ax = plt.subplots()

    # Loop through each file
    for i in range(15):
        filename = f"../{path}/us_corrida1/restraint_{str(i+1)}.dat"
        if os.path.isfile(filename):    
            # Load data from file
            data = np.loadtxt(filename, converters={1: converter})
            # Ensure the file has at least 2 columns
            if data.shape[1] >= 2:
                x = data[:, 0]  # First column (if needed)
                y = data[:, 1]  # Second column

                # Plot the second column
                plt.plot(x, y, alpha=0.7)
                ax.set_ylim(ylims[0], ylims[1])

    # Labeling
    #    plt.xlabel('First Column')
    #    plt.ylabel('Second Column')
    #plt.title(set_de_datos)
    #plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))  # Adjust legend position

    # Show plot
    #    plt.tight_layout()  # Adjust layout to make room for the legend
    plt.savefig(f"../{path}/us_corrida1/rc.png")
    plt.close()

makePlot("ATP", [7, 14])
makePlot("apo", [12, 21])
