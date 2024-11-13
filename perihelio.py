from vpython import *

rM0 = 4.60    # Initial radius of Mercury orbit, in units of R0
vM0 = 5.10e-1 # Initial orbital speed of Mercury, in units of R0/T0
c_a = 9.90e-1 # Base acceleration of Mercury, in units of R0**3/T0**2
rS  = 2.95e-7 # Schwarzschild radius of Sun,in units of R0
rL2 = 8.19e-7 # Specific angular momentum, in units of R0**2

vec_rM0 = vector(0, rM0, 0) # Initial position vector of Mercury
vec_vM0 = vector(vM0, 0, 0) # Initial velocity vector of Mercury

def evolve_mercury(vec_rM_old, vec_vM_old, alpha, beta):
    """
    Advance Mercury in time by one step of length dt.
    Arguments:
         - vec_rM_old: old position vector of Mercury
         - vec_vM_old: old velocity vector of Mercury
         - alpha: strength of 1/r**3 term in force
         - beta: strength of 1/r**4 term in force
    Returns:
         - vec_rM_new: new position vector of Mercury
         - vec_vM_new: new velocity vector of Mercury
    """

    # Compute the factor coming from General Relativity
    fact = 1 + alpha * rS / vec_rM_old.mag + beta * rL2 / vec_rM_old.mag**2
    # Compute the absolute value of the acceleration
    aMS = c_a * fact / vec_rM_old.mag**2
    # Multiply by the direction to get the acceleration vector
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # Update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # Update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

def angle_between(v1, v2):
    """Compute angle between two vectors. Result is in degrees."""
    return acos( dot(v1, v2) / (v1.mag * v2.mag) ) * 180. / pi

dt = 2. * vM0 / c_a / 200 # Time step
alpha      = 0.0          # Strength of 1/r**3 term
beta       = 1.e5         # Strength of 1/r**4 term
vec_r_last = vec_rM0      # Previous position of Mercury
turns      = 0            # Number of completed turns
max_turns  = 10           # Maximum number of turns
list_perih = list()       # List of perihelion locations
sum_angle  = 0.           # Angle between first and last perihelion



