import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('boston.csv', header=0)
df = df.iloc[:,:].values

X_train = # ???
y_train = # ???
X_test = # ???

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
# Fit only to the training data
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# SEARCH MULTIPLE SIZES
# 10 ITERATIONS OF CROSS VALIDATION

mlp = MLPRegressor(hidden_layer_sizes=(1,1,1),solver='sgd', max_iter=1000)
cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
    train_test_split(X_train, y_train, test_size=0.25)

mlp.fit(cv_data_train, cv_target_train)
training_score = mlp.score(cv_data_train,cv_target_train)
testing_score = mlp.score(cv_data_test,cv_target_test)
        


print("MLP cv training-data score:", training_score)
print("MLP cv testing-data score:", testing_score)

# NOW MAKE PREDICTIONS USING THE BEST HIDDEN LAYER SIZE

predictions = mlp.predict(X_test)
print(predictions)