import numpy as np
import matplotlib.pyplot as plt
import sympy

#Constants
gamma = 1.4
R = 287
T_s = 3500
P_s = 10000000
p_s = P_s/(T_s * R)
k_b = 1.38066 * 10**-23
s = 3.617 * 10 **-10
m_a = 5.6 * 10 **-26
E = 97
upperbound = 2
Discretisations = 2048
delta_x = upperbound/Discretisations
numerator = 1
denominator = 1

#2D Arrays of zeros
V_arr = np.zeros((Discretisations, 1))
Radii = np.zeros((Discretisations, Discretisations + 1))
wall_distances = np.zeros((Discretisations, Discretisations+1))
n_arr = np.zeros((Discretisations, Discretisations+1))

#Calculating key values of polynomial
x = sympy.symbols("x", real=True)
g = 0.5*(x - 2)**4 + (x - 2)**3 + 1
dgdx = sympy.diff(g, x)
x_min = sympy.solve(dgdx, x)
y_min = g.subs([(x,x_min[0])])
a_min = y_min**2

#Calculating the derivative of the area-mach relationship
a, k, A = sympy.symbols("a k A", real=True)
f = (1 / a) * ((2 / (k + 1)) * (1 + ((k - 1) / 2) * a ** 2)) ** ((k + 1) / (2 * (k - 1))) - A
dfda = sympy.diff(f, a)

def Calculations(Mach):
    global numerator
    global denominator
    global Radii
    global V_arr

    #Using Newton-Raphson to calculate the mach number
    while abs(numerator / denominator) > 0.0001:
        numerator = f.subs([(a, Mach), (k, gamma), (A, Area_ratio)]).evalf()
        denominator = dfda.subs([(a, Mach), (k, gamma), (A, Area_ratio)]).evalf()

        Mach = Mach - numerator / denominator

    #Calculate Parameters for Velocity array
    Temperature = T_s / (1 + ((gamma - 1) / 2) * Mach ** 2)
    Velocity = ((gamma * R * Temperature) ** 0.5 * Mach)

    #Calculate Discretation Points and Vertical Limits
    sample_point = upperbound * j/Discretisations
    upper_limit = round(2/3 * g.subs([(x, sample_point)]) * (Discretisations / 2) + (Discretisations / 2))
    lower_limit = round(-2/3 * g.subs([(x, sample_point)]) * (Discretisations / 2) + (Discretisations / 2))

    #1D arrays of zeros
    Velocity_column = np.zeros((Discretisations, 1), dtype=float)

    #Generating constant 2d arrays
    for l in range(lower_limit, upper_limit):
        Radii[l][j] = (upper_limit - lower_limit)/Discretisations
        wall_distances[l][j] = (abs(((2*(l - lower_limit))/(upper_limit - lower_limit))-1))

    #Create 2D velocity array
    Velocity_column[lower_limit:upper_limit] = Velocity
    V_arr = np.hstack((V_arr, Velocity_column))

for j in range (Discretisations):
    Area_ratio = (g.subs([(x, upperbound/Discretisations * j)]))**2/a_min
    mach_supersonic = 2
    mach_subsonic = 0.001
    numerator = 1
    denominator = 1

    if delta_x * j < x_min[0]:
        Calculations(mach_subsonic)
        print(j)
    else:
        Calculations(mach_supersonic)
        print(j)

#Increasing accuracy of arrays
for z in range(10):
    V_arr = V_arr.astype(float)
    T_arr = T_s - ((gamma - 1) * V_arr ** 2) / (2 * gamma * R)
    P_arr = P_s * (T_arr / T_s) ** ((gamma) / (gamma - 1))
    Density_arr = P_arr / (R * T_arr)
    Collison_Integral_arr = 1.16145 * (T_arr / E) ** (- 0.14874) + 0.52487 * np.e ** (-0.77320 * (T_arr / E)) + 2.16178 * np.e ** (-2.43787 * (T_arr / E))
    viscosity_arr = (5 * (np.sqrt(m_a * k_b * T_arr)) / (16 * s ** 2 * Collison_Integral_arr * np.sqrt(np.pi)))
    Re_arr = (Density_arr * V_arr * 2 * Radii) / viscosity_arr

    #Dealing with log(0) and log(negative number)
    for t in range(Discretisations):
        for u in range(Discretisations+1):
            if Re_arr[t][u] <= 0:
                n_arr[t][u] = 0
            else:
                n_arr[t][u] = 0.77 * np.log(Re_arr[t][u]) - 3.47

    V_arr = V_arr * (1 - (wall_distances ** n_arr))
    print(V_arr)

#Plotting arrays
plt.imshow(V_arr, cmap = "inferno")
plt.colorbar()
plt.show()
