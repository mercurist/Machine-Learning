import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X = pd.read_csv("./Resources/Training Data/Linear_X_Train.csv")
Y = pd.read_csv("./Resources/Training Data/Linear_Y_Train.csv")

theta = np.load("ThetaList.npy")
T0 = theta[:, 0]
T1 = theta[:, 1]

plt.ion()

for i in range(0, 50, 3):
    y_ = T1[i]*X + T0[i]

    # points in the training data
    plt.scatter(X, Y)
    # prediction line
    plt.plot(X, y_)
    plt.draw()
    plt.pause(0.5)
    plt.clf()  # Destroys the previous object so that for each iteration, you get an updated graph
