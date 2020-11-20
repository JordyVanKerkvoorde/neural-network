import numpy as np

# outputs fom neurons in the previous layer
inputs = [1, 2, 3, 2.5]

# every input has a unique weight
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

# every unique neuron has a unique bias
biases = [2, 3, 0.5]

# calculating output
output = np.dot(weights, inputs) + biases

print(output)
