import numpy as np
import pylab
import math

frequency = np.array([1100, 839, 602, 387])
frequency_squared = np.array([1210000, 703921, 362404, 149769])
volumes = np.array([423.33, 538.78, 654.24, 769.70])
volume_inverse = np.array([0.0023622233245931073, 0.001856045139017781, 0.0015284910736121302, 0.0012992074834351046])

# for x in [423.33, 538.78, 654.24, 769.70]:
#     print(1/x)

pylab.title("$f^{2}$ vs 1/V")
pylab.xlabel("1/V (in $cm^{-3}$)")
pylab.ylabel("$f^{2}$ (in $Hz^2$)")
pylab.plot(volume_inverse, frequency_squared, marker=".")
pylab.show()



