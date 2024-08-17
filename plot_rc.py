import numpy as np
import matplotlib.pyplot as plt
import os

datos = ["c1","c2","11","12","21","22"]
for set_de_datos in datos:

    # Number of files
    start = 1
    num_files = 43 

    # Create a plot
    plt.figure(figsize=(12, 8))

    # Loop through each file
    for i in range(start, num_files+1):
        filename = "r"+set_de_datos+"_"+str(i)+".dat"
        if os.path.isfile(filename):    
            # Load data from file
            data = np.loadtxt(filename)
            # Ensure the file has at least 2 columns
            if data.shape[1] >= 2:
                x = data[:, 0]  # First column (if needed)
                y = data[:, 1]  # Second column

                # Plot the second column
                plt.plot(x, y, alpha=0.7)

    # Labeling
#    plt.xlabel('First Column')
#    plt.ylabel('Second Column')
    plt.title(set_de_datos)
    #plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))  # Adjust legend position

    # Show plot
#    plt.tight_layout()  # Adjust layout to make room for the legend
    plt.show()
    plt.close()
