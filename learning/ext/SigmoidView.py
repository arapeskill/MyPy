'''python绘制sigmoid图像'''
import time

import numpy as np
import matplotlib.pyplot as plt


#  定义 sigmoid(x)

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y


#  定义 sigmoid(x)

def plot_sigmoid():
    x = np.arange(-10, 10, 0.01)
    y = sigmoid(x)
    plt.title("sigmoid ", fontsize=23)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    plot_sigmoid()
    time.sleep(1000)
