#######################################################################
######### A three-layered neural network code as an alternative approach ########################
#### Dependencies (imported libraries) are needed to be installed ###
#### The code is mainly based on https://pytorch.org/tutorials/beginner/examples_nn/two_layer_net_nn.html
## we assume the data files are in the reconstruction folder
#######################################################################

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
####################################################################




# D_in is the number of input nodes; H is number of hidden nodes; D_out is the number of output nodes.
D_in, H, D_out = 2, 3, 1



# Data is gathered from our github repository: https://github.com/mamadpierre/NOAA-Refined-Stations
df_46042=pd.read_csv( 'reconstruction/46042FeatureSelection.cvs' , index_col='time', dtype=object,error_bad_lines=False )
df_46042[['WVHT','APD', 'DPD','MWD']]= df_46042[['WVHT','APD', 'DPD','MWD']].astype('float64')
df_46069=pd.read_csv( 'reconstruction/46069FeatureSelection.cvs' , index_col='time', dtype=object,error_bad_lines=False )
df_46069[['WVHT','APD', 'DPD','MWD']]= df_46069[['WVHT','APD', 'DPD','MWD']].astype('float64') 
df_46025=pd.read_csv( 'reconstruction/46025FeatureSelection.cvs' , index_col='time', dtype=object,error_bad_lines=False )  
df_46025[['WVHT','APD', 'DPD','MWD']]= df_46025[['WVHT','APD', 'DPD','MWD']].astype('float64') 


#dividing the dataset into 50% train - 50% test as conducted by alternative papers (Cornejo et. al., (2016-2018))
df_46042_train = df_46042.loc[:'2009-12-31 23:00:00']
df_46042_test = df_46042.loc['2010-01-01 00:00:00':]
df_46025_train = df_46025.loc[:'2009-12-31 23:00:00']
df_46025_test = df_46025.loc['2010-01-01 00:00:00':]
df_46069_train = df_46069.loc[:'2009-12-31 23:00:00']
df_46069_test = df_46069.loc['2010-01-01 00:00:00':]

  



def prepareData(raw_x):
    x=[]
    for i in range(len(raw_x[0])):
        x_iterate = []
        for element in raw_x:
            x_iterate.append(element[i])
        x.append(x_iterate)
    return x

x = np.array(prepareData([np.array(df_46042_train['WVHT']),np.array(df_46025_train['WVHT'])]))
y = np.expand_dims(np.array(df_46069_train['WVHT']),1)

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(5000):
    # Forward pass: compute predictions of y
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)
    
    # Compute and print the training loss based on MSE
    loss = mean_squared_error(y_pred , y)
    print("epoch: ", t,"training loss (MSE loss): ", loss)

    # Backpropagation to compute the gradients  (ReLU activation)
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # Update weights using SGD optimziation algorithm
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
    
############################################ test ##############################
print('-'*40,"evaluation on test dataset",'-'*40)
x = np.array(prepareData([np.array(df_46042_test['WVHT']),np.array(df_46025_test['WVHT'])]))
y = np.expand_dims(np.array(df_46069_test['WVHT']),1)





h = x.dot(w1)
h_relu = np.maximum(h, 0)
y_pred = h_relu.dot(w2)



###################################################################
# Compute and print loss
def MAE(actual,predicted):
    actual=np.ravel(actual)
    predicted=np.ravel(predicted)
    return np.sum( np.abs(actual-predicted)  ) / len(actual)



RMSEloss = sqrt(mean_squared_error(y_pred , y))
MAEloss = MAE(y_pred,y)
CC=np.cov(np.ravel(y_pred),np.ravel(y))[0][1] / sqrt( np.var(y_pred ) * np.var(np.ravel(y)))     
r2 = CC**2

print("Test RMSE loss: ", RMSEloss)
print("Test MAE loss: ", MAEloss)
print("Test r^2: ", r2)


    
    
