# Variables
# m: Mass of the object in Kilograms
# A: Frontal area, this is the area of the outline of the object when looked at head on
# C: Drag Coefficient, measured in Kilograms per meter basically a measure of how aerodynamically efficient
#    the object is
# s: The altitude the object is being dropped from in meters
# v: The current velocity of the object
# p: The density of the air at sea level
# t: Time elapsed
# g: Acceleration due to gravity at a specific altitude assuming no air resistance
# g1: Acceleration due to gravity that the object is experiencing measured in g's
# u: The velocity of the object at the previous data point
# q: The air pressure at a specific altitude
# p1: The density of the air at a specific altitude
# T: Static Air Temperature at a specific altitude
# s1: The altitude the object is being dropped from in kilometers
# F0: The weight of the object at a specific altitude
# a3: The drag force experienced by the object
# a0: Acceleration due to gravity that the object is experiencing measured in meters per second squared
# a1 and a2: Intermediate steps of the drag force equation

# Custom variables
m = float(input("Enter the mass of the object in Kilograms: "))
A = float(input("Enter the frontal area of the object in Meters squared: "))
C = float(input("Enter the drag coefficient of the object: "))
s = float(input("Enter the height the object will be dropped from in Meters: "))
v = float(input("Enter the starting velocity of the object in Meters per second: "))

# Set variables
p = 1.2041
t = 0

# NASA Standard atmosphere equations
for i in range(6000):
    if 0 <= s < 11000:
        T = 15.04 - (0.00649 * s)
        q = 101.29 * ((T + 273.1) / 288.08) ** 5.256
        p1 = (q / 101.325) * p
    elif 11000 <= s < 25000:
        q = 22.65 * (2.71828 ** (1.73 - 0.000157 * s))
        p1 = (q / 101.325) * p
    else:
        T = -131.21 + 0.00299 * s
        q = 2.488 * ((T + 273.1) / 216.6) ** -11.388
        p1 = (q / 101.325) * p

    # Gravity Equation
    s1 = s / 1000
    g = (9.81 * (s1 + 6371) ** -2) / 6371 ** -2
    F0 = g * m

    # Drag force Equation
    a1 = v ** 2
    a2 = C * p1 * a1 * A
    a3 = a2 / 2

    a0 = (F0 - a3) / m

    # Adding onto the velocity, time and displacement
    v += a0 / 10
    t += 0.1
    u = v - (a0 / 10)
    s -= (0.1 * (v + u)) / 2

    # G-force Equations
    g1 = (v - u)/(0.1 * g)

    # Print t, v, s, or g1
    print(t, ",", s, ",", v, ",", g1)
