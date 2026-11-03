# Normal Distribution, more commonly known as the Bell curve
# the bell curve is symmetric
# the probability density function (PDF) of the normal distribution is given by:
# f(x) = (1 / ( sqrt(2πσ^2) )) * e^(-(x - μ)^2 / (2σ^2))

from matplotlib import pyplot as plt
import numpy as np

# x = np.array([x for x in range(-5,5, 0.1)])

# np.linspace() generates an array of evenly spaced numbers over a specified interval.
# linspace(start, stop, num)
# returns num evenly spaced samples, calculated over the interval [start, stop].

# calculated indexes by (start - stop) / (num - 1)
# (-5, 5) / (10 - 1) = 10/9 points

range = float(input("Enter the range of the bell curve (e.g., -3,3): "))

x = np.linspace(-range,range,101)

print(x)
# A single calculation (e^1)
# print(np.exp(1))

def normal_distribution(x, avg, sigma):
    return(1/(np.sqrt(2 * np.pi * sigma ** 2))) * np.exp(-(x -avg) ** 2 / (2 * sigma ** 2))


# the expectation of a normal distribution (mean) is the average of all possible values, 
# the bell curve is symmetric so the mean is 0 in this case,
# the standard deviation is 1, as the variance is 1, given by E[X^2] - (E[X])^2

# after some testing, avg moves the curve left or right, 
# while sigma changes the width of the curve, making it wider or narrower.
y = normal_distribution(x, 0, 1)

print(y)

plt.plot(x, y)
plt.title("Normal Distribution (Bell Curve)")
plt.xlabel("Random Variable (x)")
plt.ylabel("Probability Density Function (PDF)")
plt.grid(True)
plt.show()