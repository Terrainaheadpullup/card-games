# Variables
# m: Mass of the object [Kg]
# A: Frontal area, this is the area of the outline of the object when looked at head on [m^2]
# C: Drag Coefficient basically a measure of how aerodynamically efficient the object is [Kgm]
# p: The density of the air at sea level [Kgm^-3]
# t: Time elapsed [s]
# g: Acceleration due to gravity at a specific altitude assuming no air resistance [ms^-2]
# u: The velocity of the object at the previous data point [ms^-1]
# q: The air pressure at a specific altitude [Kgm^-1s^-2]
# p1: The density of the air at a specific altitude [Kgm^-3]
# T: Static Air Temperature at a specific altitude [K]
# s1: The altitude the object is being dropped from in kilometers [m]
# F0: The weight of the object at a specific altitude [N]
# a3x: The drag force experienced by the object in the X direction (Horizontal) [N]
# a3y: The drag force experienced by the object in the Y direction (Vertical) [N]
# a0x: Acceleration that the object is experiencing in the X direction (Horizontal) [ms^-2]
# a0y: Acceleration that the object is experiencing in the Y direction (Vertical) [ms^-2]
# g1x: G-force the object is experiencing in the X direction (Horizontal) [N/Kg]
# g1y: G-force the object is experiencing in the Y direction (Vertical) [N/kg]
# sX: Altitude of the object above the surface [m]
# sY: Range of the object [m]
# vX: Velocity of the object in the X direction (Horizontal) [ms^-1]
# vY: Velocity of the object in the Y direction (Vertical) [ms^-1]

# Import modules
import math

# Custom variables
m = float(input("Enter the mass of the object in Kilograms: "))
A = float(input("Enter the frontal area of the object in Meters squared: "))
C = float(input("Enter the drag coefficient of the object: "))
sY = float(input("Enter the height the object will be dropped from in Meters: "))
v = float(input("Enter the starting velocity of the object in Meters per second: "))
theta = math.radians(float(input("Enter the impulse angle from horizontal in degrees: ")))

# Set variables
p = 1.2041
t = 0
sX = 0

vY = v * math.sin(theta)
vX = math.sqrt((v**2)-(vY**2))

print("Time (s)",
      "Velocity (ms^-1)",
      "Velocity_X (ms^-1)",
      "Velocity_Y (ms^-1)",
      "Range (m)",
      "Altitude (m)",
      "G-force_X (N/Kg)",
      "G-force_X (N/Kg)")

# NASA Standard atmosphere equations
for i in range(6000):
    if 0 <= sY < 11000:
        T = 15.04 - (0.00649 * sY)
        q = 101.29 * ((T + 273.1) / 288.08) ** 5.256
        p1 = (q / 101.325) * p
    elif 11000 <= sY < 25000:
        q = 22.65 * (2.71828 ** (1.73 - 0.000157 * sY))
        p1 = (q / 101.325) * p
    else:
        T = -131.21 + 0.00299 * sY
        q = 2.488 * ((T + 273.1) / 216.6) ** -11.388
        p1 = (q / 101.325) * p

    # Gravity Equation
    s1 = sY / 1000
    g = (9.81 * (s1 + 6371) ** -2) / 6371 ** -2
    F0 = g * m

    # Drag force Equation X
    a1x = vX ** 2
    a2x = C * p1 * a1x * A
    a3x = a2x / 2

    a0x = a3x / m

    # Drag force Equation Y
    a1y = vY ** 2
    a2y = C * p1 * a1y * A
    a3y = a2y / 2

    a0y = (F0 - a3y) / m

    # Adding onto the velocity, time and displacement for X
    vX -= a0x / 10
    t += 0.1
    uX = vX - (a0x / 10)
    sX -= (0.1 * (vX + uX)) / 2

    # Adding onto the velocity, time and displacement for Y
    vY += a0y / 10
    uY = vY - (a0y / 10)
    sY -= (0.1 * (vY + uY)) / 2

    v = math.sqrt((vY**2)+(vX**2))

    # G-force Equations for X and Y
    g1x = (vX - uX)/(0.1 * g)
    g1y = (vY - uY)/(0.1 * g) - 1

    # Print t, v, g1x, g1y, vY, vX, sY, sX
    print(t, v, vX, vY, -sX, sY, g1x, g1y)
