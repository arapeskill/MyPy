from numpy import random, dot, exp, array

X = array([[1, 0, 1], [1, 1, 0], [0, 0, 1], [0, 1, 0]])
y = array([1, 1, 1, 0]).T

random.seed(1)

weights = random.random((3, 1)) * 2 - 1
for it in range(10000):
    output = 1 / (1 + exp(-dot(X, weights)))
    error = y - output
    slope = output * (1 - output)
    delta = error * slope
    weights = weights + dot(X.T, delta)
print(output)
