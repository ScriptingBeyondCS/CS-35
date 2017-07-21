import numpy as np
import cv2
from matplotlib import pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

# Get Data


# Now split the image to 1300 cells, each 10x10 pixels


# Make it into a Numpy array. It shape will be (50,26,10,10) 
    # (note: for a colored picture it would be (50,26,10,10,3)
    # because colored pixels have RGB values instead of a 
    # single brightness value)


# Randomly shuffle data columns (use np.random.permutation)


# Now we prepare train_data and test_data.
    # Training Shape = (988, 100)
    # Testing Shape = (312, 100)


# Create labels for train and test data
L = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # convert to list
# Repeat the list for each row
y_train = np.tile(L, 38) # Shape = (988,)
y_test = np.tile(L, 12)  # Shape = (312,2700)


# Do Machine Learning with a Neural Network (MLPClassifier)






# Compute accuracy


