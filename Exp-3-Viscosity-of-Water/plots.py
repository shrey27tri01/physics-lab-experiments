import numpy as np
import pylab
import math

h_t = np.array([14, 13, 12, 11, 10, 9, 8, 7, 6, 5])
t = np.array([20, 43, 68, 100, 123, 140, 183, 220, 241, 268])
X_t = np.array([12.6, 11.8, 11.2, 10.9, 10.1, 9.3, 8.1, 7.6, 6.7, 5.9])
x_2_t = np.array([158.76, 139.24, 125.44, 118.81, 102.01, 86.49, 65.61, 57.76, 44.89, 34.81])
ln_x = np.array([2.53, 2.46, 2.41, 2.38, 2.31, 2.23, 2.09, 2.02, 1.90, 1.77])

# x^2 vs H(t)
# pylab.title("$X^{2}$ vs H(t)")
# pylab.xlabel("H(t) (in cm)")
# pylab.ylabel("$X^{2}$ (in $cm^2$)")
# pylab.plot(h_t, x_2_t)

# slopes = []
# for i in range(9):
#     slopes.append((x_2_t[i+1] - x_2_t[i]) / (h_t[i+1] - h_t[i]))

# print(sum(slopes) / 9)

# H(t) vs t
# pylab.title("H(t) vs t")
# pylab.xlabel("t (in sec)")
# pylab.ylabel("H(t) (in cm)")
# pylab.plot(t, h_t)

# lnx vs t
# pylab.title("ln(x) vs t")
# pylab.xlabel("t (in sec)")
# pylab.ylabel("ln(x)")
# pylab.plot(t, ln_x)

slopes = []
for i in range(9):
    slopes.append((ln_x[i+1] - ln_x[i]) / (t[i+1] - t[i]))

print(sum(slopes) / 9)

pylab.show()

# list = [12.6, 11.8, 11.2, 10.9, 10.1, 9.3, 8.1, 7.6, 6.7, 5.9]
# for x in list:
#     print(math.log(x))