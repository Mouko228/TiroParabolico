import numpy as np
import math

def parabola(x1,y1,x2,y2,x3,y3,mass,k_spring,g):
  
  #trajectory starting point (x1,y1)
  #trajectory goes through (x2,y2), (x3,y3)

# ------------Step one (Find highest point, solve equation of the parabola)
  # make a system of equations for y = ax^2 + bx + c, taking values from the 3 points
  # we take in favor that we know values of x and y to make a linear equation and use a simple algorythm to solve for it
  # y = (x^2)a + (x)b + (1)c -> we solve it creating matrixes and running the algorythm
  # we were going to solve system of equations by method Gauss Jordan but found converting into linear to be more efficient
  coef = np.array([(x1**2,x1,1),(x2**2,x2,1),(x3**2,x3,1)])
  y_values = np.array([y1,y2,y3])
  a,b,c = np.linalg.solve(coef,y_values)

  # find h,k,p with values a, b, c considering [ax^2 + bx + c => (x-h)^2 = -4p(y-k)]
  h=-b/a
  k = a*(h**2) + b*(h) + c

# -----------Step two (Find angle)
  # find tangent of parabola with d/dx of ax^2 + bx + c
  # evaluate d/dx f(x) at x0 -> theta = tan-1(f'(x))
  dx0 = 2*a*(x1) +b
  theta = math.degrees(math.atan(math.radians(dx0))) 

# -----------Step three (Find V0)
  # find V0 with h,k using sqrt((2g*k)/sin(theta))
  V0 = math.sqrt((2*g*k)/math.degrees(math.sin(math.radians(theta))))

# ---------- Step four (Hooke's Law)
  # Find compression through equalation of Potential spring energy and Kinetic energy
  # Adapt Hooke's formula to find "r" -> r = sqrt((mass*V0^2)/k) ....... k being spring constant
  r = math.sqrt((mass*V0**2)/k_spring)

  return theta, r, a, b, c

def convert(mass,projectile_diameter,gravity,k,target_diameter,target_height, shooter_height, distance, x, y):
  x1 = 0 + (projectile_diameter/2)
  y1 = shooter_height + (projectile_diameter/2)
  x2 = x
  y2 = y
  x3 = x1 + distance
  y3 = target_height + projectile_diameter
  mass = mass
  k_spring = k
  g = gravity

  return x1,y1,x2,y2,x3,y3,mass,k_spring,g