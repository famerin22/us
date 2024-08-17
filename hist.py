import numpy as np
import matplotlib.pyplot as plt

dim=1

plt.figure(figsize=(8, 6))

# Example filename (replace with your actual filename)
for i in range (15):
    filename = 'restraint_'+str(i+1)+'.dat'

    # Load data from the file (assuming it has two columns separated by whitespace)
    data = np.loadtxt(filename, usecols=dim)  # usecols=1 selects the second column (indexing starts from 0)

    # Plot histogram
    plt.hist(data, bins=20)  # Adjust bins as needed

for i in range (8):
    filename = './fill_gaps/restraint_'+str(i+1)+'_gap.dat'

    # Load data from the file (assuming it has two columns separated by whitespace)
    data = np.loadtxt(filename, usecols=dim)  # usecols=1 selects the second column (indexing starts from 0)

    # Plot histogram
    plt.hist(data, bins=20)  # Adjust bins as needed


#for i in range (10):
#    filename = '/home/usuario/pruebas/wham2d/restraint_'+str(i+1)+'_gap3.dat'

    # Load data from the file (assuming it has two columns separated by whitespace)
#    data = np.loadtxt(filename, usecols=dim)  # usecols=1 selects the second column (indexing starts from 0)

    # Plot histogram
#    plt.hist(data, bins=20)  # Adjust bins as needed


filename = './fill_gaps/fill_gaps2/restraint_2gap_6.dat'
# Load data from the file (assuming it has two columns separated by whitespace)
data = np.loadtxt(filename, usecols=dim)  # usecols=1 selects the second column (indexing starts from 0)
# Plot histogram
plt.hist(data, bins=20)  # Adjust bins as needed

filename = './fill_gaps/fill_gaps2/restraint_5_2gap.dat'
# Load data from the file (assuming it has two columns separated by whitespace)
data = np.loadtxt(filename, usecols=dim)  # usecols=1 selects the second column (indexing starts from 0)
# Plot histogram
plt.hist(data, bins=20)  # Adjust bins as needed


plt.xlabel('Values in Second Column')
plt.ylabel('Frequency')
plt.show()
