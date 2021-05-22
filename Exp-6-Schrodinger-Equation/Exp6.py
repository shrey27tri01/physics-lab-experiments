import math
import numpy as np
import matplotlib.pyplot as plt

steps = 10000
gamma_sq = 200 
eigen_state = -0.9
precision = math.pow(10, -4)
U_x = -1 * np.ones(steps)
k_square = (gamma_sq) * (eigen_state - U_x)

def eigen_state(min, max, precision=1e-6):
	k_square = (gamma_sq) * (max - U_x)
	dis = abs(wave_function(k_square)[-1])
	offset = 4
	for eis in np.linspace(min, max, int(round(max - min, offset) / precision)):
		k_square = (gamma_sq) * (eis - U_x)
		dif = abs(wave_function(k_square)[-1])
		if(dis >= dif):
			eigen_state = eis
			dis = dif
	return eigen_state

def wave_function(k_square):
	offset = 1e-4
	l_square = math.pow((1.0 / (steps - 1)), 2)
	psi = [0, offset]

	for i in range(2, len(k_square)):
		num = 2 * (1 - (5.0 / 12) * l_square * k_square[i - 1]) * psi[i - 1] - (1 + (1.0 / 12) * l_square * k_square[i - 2]) * psi[i - 2]
		psi.append(num / (1 + (1.0 / 12) * l_square * k_square[i]))
	return psi

def plot_wave_function(eigenvalue):
	k_square = (gamma_sq) * (eigenvalue - U_x)
	plt.clf()
	plt.xlabel('x')
	plt.ylabel('Psi(x)')
	plt.axhline(y = 0, color = 'r')
	plt.plot(wave_function(k_square = k_square), color = 'r')
	plt.show()

def main():
	# Ground State
	eigenvalue = eigen_state(min = -0.960, max = -0.950, precision = precision)
	plot_wave_function(eigenvalue)

	# 1st excited state
	# eigenvalue = eigen_state(min = -0.803, max = -0.802, precision = precision)
	# plot_wave_function(eigenvalue)

	# 2nd excited state
	# eigenvalue = eigen_state(min = -0.556, max = -0.555, precision = precision)
	# plot_wave_function(eigenvalue)

	# 3rd excited state
	# eigenvalue = eigen_state(min = -0.211, max = -0.210, precision = precision)
	# plot_wave_function(eigenvalue)

main()