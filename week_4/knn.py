import pandas as pd
import numpy as np
import math

def readFile(filename='iris.csv'):
    """read csv file and convert it to array"""
    df = pd.read_csv(filename, header=0)    # read the file
    return df

def getDistance(x_data_row1, x_data_row2):
    """calculates distance between two rows of data (based on Euclidean distance)"""
    distance = 0                            
    length = len(x_data_row1)
    for i in range(length):
        distance += (x_data_row1[i] - x_data_row2[i])**2      # differences of the columns squared
    
    distance = math.sqrt(distance)

    return distance

def knnForOne(x_training_data, y_training_data, single_x_test_data, n_neighbors):
    """find the most common neighbor out of k nearest neighbors for 1 row of test data"""
    distances_list = []
    nearest_neighbors = []    
    length = len(x_training_data)

    for i in range(length):
        X2 = x_training_data[i,:]   # get current row of known data
        Y2 = y_training_data[i]     # get current label of known data
        distance = getDistance(single_x_test_data, X2)   # compare test to known data
        distances_list += [[distance, Y2]]
    
    distances_list = sorted(distances_list)
    for i in range(n_neighbors):
        nearest_neighbors += [distances_list[i][1]]

    return max(nearest_neighbors, key=nearest_neighbors.count)      


def knnForAll(x_training_data, y_training_data, x_test_data, n_neighbors):
    """find the most common neighbor out of k nearest neighbors for multiple rows of test data"""

    y_test_data = []
    for row in x_test_data:             # for multiple rows of test data
        y_test_data += [knnForOne(x_training_data, y_training_data, row, n_neighbors)]

    return y_test_data


def crossValidate(x_training_data, y_training_data, test_size_percentage):
    """find the value of k that produces the best results for the data"""

    data_length = len(x_training_data)
    foldSize = int(round(data_length * test_size_percentage))   # size of each temporary test data
    best_score = 0
    best_k = 0

    for k in [1,3,5,7]:             # Test different values of k
        score = 0
        for i in range(0, data_length, foldSize):      # Switch section of test data

            x_temp_test = x_training_data[i:i+foldSize]     # get temporary data to test
            known_y_test = y_training_data[i:i+foldSize]    # we already know their labels
            x_temp_training = np.append(x_training_data[0:i], x_training_data[i+foldSize:], axis=0) # the rest is our temporary training data
            y_temp_training = np.append(y_training_data[0:i], y_training_data[i+foldSize:], axis=0)
            
            y_temp_test = knnForAll(x_temp_training, y_temp_training, x_temp_test, k)   # labels determined for a current k value

            for i in range(len(known_y_test)):              # Score how well this value of k did based 
                if y_temp_test[i] == known_y_test[i]:       # on how well it matches the known labels
                    score += 1
                    
        if score > best_score:                              # Choose the best k value up to this point
            best_score = score
            best_k = k

    print("Best Percent Correct: ", best_score/data_length) # Print percentage that were correct using the best value of k
    print("Best k: ", best_k)
    return best_k

#---------------------------------
import time
df = readFile('iris.csv')
df = df.iloc[:,:].values        # Convert to numpy array

# Divide data up
x_training_data = df[9:, 0:4]
y_training_data = df[9:, 4]
x_test_data = df[0:9, 0:4]
y_test_data = df[0:9, 4]     

# Feature engineering here


#---------------------------------

def main():

    k = crossValidate(x_training_data, y_training_data, 0.25)

    return knnForAll(x_training_data, y_training_data, x_test_data, k)
