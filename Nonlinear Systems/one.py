import numpy as np
import pylab

def f(x, r):
    """Discrete logistic equation with parameter r"""
    return r * x * (1 - x)

if __name__ == '__main__':
    # Store values of x_n, with x+0 being 0.1
    xValues = [0.1]

    # Store n values, where n takes values 0, 0.1, 0.2, ...., 99.8, 99.9
    n = np.arange(0, 10, 0.1)

    # Value of r
    r = 3.857083

    # Find x_(n + 1) values from x_n and store the values in the array xValues
    for i in range(len(n)):
        x = f(xValues[i], r)
        xValues.append(x)

    # Remove the last element from xValues, since it is not needed
    xValues.pop()

    # Plot the graph
    pylab.xlabel('n')
    pylab.ylabel('$x_n$')
    pylab.title(f'r = {r}')
    pylab.plot(np.array(n), np.array(xValues))
    pylab.show()
