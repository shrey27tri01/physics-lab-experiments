# Defining max values for the axes 
maxRValue = 13
maxXValue = 10

# Assuming r (initial) to be 1
r_n = 1.0

# Defining r_(n - 1) and r_(n + 1)
r_nMinusOne = 0.0
r_nPlusOne = 0.0

# Assumed initial value of the Feigenbaum constant 
previousConstant = 3.2
 
# Print the output headline
print(" Bifurcation #       Feigenbaum constant")

# Looping through the bifurcations
for bifurcation in range(2, maxRValue + 1):

    # Defining r_(n + 1)
    r_nPlusOne = r_n + (r_n - r_nMinusOne) / previousConstant

    # Considering all the plot points between this bifurcation and the next one
    for j in range(1, maxXValue + 1):
        x = 0.0
        y = 0.0
        for k in range(1, (1 << bifurcation) + 1):
            y = 1.0 - 2.0 * y * x
            x = r_nPlusOne - x * x
        r_nPlusOne = r_nPlusOne - x / y

    # Feigenbaum constant for the two bifurcations
    constant = (r_n - r_nMinusOne) / (r_nPlusOne - r_n)

    # Printing the output for all the bifurcations
    print("     {0:2d}                    {1:.8f}".format(bifurcation, constant))

    # Changing the values of previousConstant, r_n, r_(n + 1) and r_(n - 1) so as to do the processing again
    previousConstant = constant
    r_nMinusOne = r_n
    r_n = r_nPlusOne