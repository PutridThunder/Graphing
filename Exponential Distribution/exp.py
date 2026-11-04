# Exponential Distribution
# the Exponential distribution is not symmetric, it is skewed to the right
# the probability density function (PDF) of the Exponential distribution is given by:
# f(x) = λ * e^(-λx) for x ≥ 0
# where λ is the number of events per unit time (rate parameter)

from matplotlib import pyplot as plt
import numpy as np

# x = np.array([x for x in range(-5,5, 0.1)])

# np.linspace() generates an array of evenly spaced numbers over a specified interval.
# linspace(start, stop, num)
# returns num evenly spaced samples, calculated over the interval [start, stop].

# calculated indexes by (start - stop) / (num - 1)
# (0, 10) / (101 - 1) = 10/100 = 0.1 points

range = float(input("Enter the end-range of the exponential curve (e.g. 10): "))

x = np.linspace(0, range, 101)

print(x)
# A single calculation (e^1)
# print(np.exp(1))

def exponential_distribution(x, rate):
    return rate * np.exp(-rate * x)

# the expectation of an exponential distribution is 1/λ, where λ is the rate parameter

# the exponential distribution is skewed to the right, so the mean is 1/λ, where λ is the rate parameter
# the variance is 1/λ^2, given by E[X^2] - (E[X])^2

# after some testing, rate changes the shape of the curve,
# while the range changes the domain of the curve.
y = exponential_distribution(x, 1)

print(y)

plt.plot(x, y)
plt.title("Exponential Distribution")
plt.xlabel("Random Variable (x)")
plt.ylabel("Probability Density Function (PDF)")
plt.grid(True)
plt.show()