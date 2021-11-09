import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg

x1 = [1,15] # for approximation of the first degree polynomial
x2 = [1,8,15] # for approximation of the second degree polynomial
x3 = [1,4,10,15] # for approximation of the third degree polynomial

def f(x):
    return numpy.sin(x / 5) * numpy.exp(x / 10) + 5 * numpy.exp(-x / 2)
    # do not use math.sin, math.exp.
    # it result is a scalar and you need a vector to later plot a graph using x = numpy.linspace(....)



# resolve A*w = y,
# where A - matrix [[x_0^0, x_0^1, x_0^2..... x_0^n],
#                   [x_1^0, ...............  .x_1^n],
#                   ............................
#                  [[x_n^0 ...................x_n^n]]

#                  x_0.... x_n - points through which passes the polynomial
# w - vector of polynomial coefficients we lookinf for
# y - vector with function values
#     where x = [x0, x1, ....,         xn]
#           y = [f(x0), f(x1), ......f(xn)]

# first degree polynomial approximation

coef_matrix_1 = [[x1[0]**0, x1[0]**1],
                 [x1[1]**0, x1[1]**1]]
y1 = [f(x1[0]), f(x1[1])]

w1 = linalg.solve(coef_matrix_1, y1)

def f1(x):
    return w1[0] + w1[1]*x

# second degree polynomial approximation

coef_matrix_2 = [[x2[0]**0, x2[0]**1, x2[0]**2],
                 [x2[1]**0, x2[1]**1, x2[1]**2],
                 [x2[2]**0, x2[2]**1, x2[2]**2]]
y2 = [f(x2[0]), f(x2[1]), f(x2[2])]

w2 = linalg.solve(coef_matrix_2, y2)

def f2(x):
    return w2[0] + w2[1]*x + w2[2]*(x**2)

# third degree polynomial approximation

coef_matrix_3 = [[x3[0]**0, x3[0]**1, x3[0]**2, x3[0]**3],
                 [x3[1]**0, x3[1]**1, x3[1]**2, x3[1]**3],
                 [x3[2]**0, x3[2]**1, x3[2]**2, x3[2]**3],
                 [x3[3]**0, x3[3]**1, x3[3]**2, x3[3]**3]]
y3 = [f(x3[0]), f(x3[1]), f(x3[2]), f(x3[3])]

w3 = linalg.solve(coef_matrix_3, y3)

def f3(x):
    return w3[0] + w3[1]*x + w3[2]*(x**2) + w3[3]*(x**3)

# plot a graph

fig, ax = plt.subplots()

x = numpy.linspace(0, 16, 200) # to generate numpy array, x_i in [0,16], i = 200 - 1

ax.plot(x, f(x))
ax.plot(x, f1(x))
ax.plot(x, f2(x))
ax.plot(x, f3(x))
plt.show()

# save the result in the text file
# the result - coeff of w3 separated by spacebar

file_obj = open('fun_approximation_result.txt', 'w')
result = str(w3[0])
for i in range(len(w3)-1):
    result += ' ' + str(w3[i+1])
file_obj.write(result)
file_obj.close()
