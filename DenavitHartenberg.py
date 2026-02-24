import sympy as sp
from sympy.matrices import rot_axis3
#Para poder graficar:
import matplotlib.pyplot as plt
import numpy as np
#Para generar la matriz Denavit Hartenberg:
from spatialmath import *
from spatialmath.base import *

# Definir los símbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# Matriz RzTzTxRx
TDH = trotz(theta) @ transl(0, 0, d) @ transl(a, 0, 0) @ trotx(alpha)
# Mostrar la matriz Denavit-Hartenberg
sp.pprint(TDH)
print(type(TDH))

#Declarándola explícitamente 
T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),  sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
               [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
               [0,              sp.sin(alpha),               sp.cos(alpha),              d],
                [0,              0,                         0,                        1]])
# Mostrar la matriz Denavit-Hartenberg
sp.pprint(T)
print(type(T))

# Ahora declaramos variables simbólicas para cada joint de un robot de 6 grados de libertad
theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')
#De la tabla DH
T01 = T.subs({d: 0.5, a: 0.25, alpha: sp.pi/2})
T01 = T01.subs({theta: theta1})
sp.pprint(T01)

T12 = T.subs({d: 0, a: 0.89, alpha: 0})
T12 = T12.subs({theta: theta2})
sp.pprint(T12)

T23 = T.subs({d: 0, a: 0.15, alpha: -sp.pi/2})
T23 = T23.subs({theta: theta3})
sp.pprint(T23)

T34 = T.subs({d: 0.88, a: 0.15, alpha: sp.pi/2})
T34 = T34.subs({theta: theta4})
sp.pprint(T34)

T45 = T.subs({d: 0, a: 0, alpha: -sp.pi/2})
T45 = T45.subs({theta: theta5})
sp.pprint(T45)

T56 = T.subs({d: 0.14, a: 0, alpha: 0})
T56 = T56.subs({theta: theta6})
sp.pprint(T56)

# Ahora podemos calcular la transformación total desde la base hasta el efector final
T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_simplified = sp.simplify(T06)
sp.pprint(T06_simplified)

#Ahora podemos evaluar esta matriz para un conjunto de ángulos donde todos son 0, y theta 2 es -90°
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)-sp.pi/2
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06.subs({theta1: joint1, theta2: joint2, theta3: joint3, theta4: joint4, theta5: joint5, theta6: joint6})
sp.pprint(T06_solved)