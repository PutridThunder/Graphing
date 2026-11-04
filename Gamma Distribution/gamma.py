# Gamma Distribution
# the Gamma distribution is a generalization of the Exponential distribution
# the probability density function (PDF) of the Gamma distribution is given by:
# f(x) = (1/Γ(k)) * λ^k * x^(k-1) * e^(-λx) for x ≥ 0
# where k is the shape parameter and λ is the rate parameter

from matplotlib import pyplot as plt
import numpy as np

range = float(input("Enter the end-range of the gamma curve (e.g. 10): "))

x = np.linspace(0, range, 101)

print(x)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def gamma_distribution(x, a, rate):
    return (rate * np.exp(-rate * x) * (rate * x) **(a-1)) / factorial(a-1)

# the expectation of a gamma distribution is k/rate,
# where k is the number of events waiting on (shape)
# and rate is the expected number of events per unit time

# the gamma distribution is skewed to the right,
# so the mean is k/rate, where k is the shape
#  and λ is the rate parameter

# the variance is k/rate^2, given by E[X^2] - (E[X])^2

# after some testing, rate changes the shape of the curve,
# while the range changes the domain of the curve.
y = gamma_distribution(x, 1, 2)

print(y)

plt.plot(x, y)
plt.title("Gamma Distribution")
plt.xlabel("Random Variable (x)")
plt.ylabel("Probability Density Function (PDF)")
plt.grid(True)
plt.show()