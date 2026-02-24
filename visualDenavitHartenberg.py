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

#Declarándola explícitamente 
T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),  sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
               [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
               [0,              sp.sin(alpha),               sp.cos(alpha),              d],
                [0,              0,                         0,                        1]])
# Definimos los ángulos para que cada uno sea único
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')
#De la tabla DH
T01 = T.subs({d: 0.68, a: 0.2, alpha: -sp.pi/2})
T01 = T01.subs({theta: theta_1})

T12 = T.subs({d: 0, a: 0.89, alpha: 0})
T12 = T12.subs({theta: theta_2})

T23 = T.subs({d: 0, a: 0.15, alpha: -sp.pi/2})
T23 = T23.subs({theta: theta_3})

T34 = T.subs({d: 0.88, a: 0, alpha: sp.pi/2})
T34 = T34.subs({theta: theta_4})

T45 = T.subs({d: 0, a: 0, alpha: -sp.pi/2})
T45 = T45.subs({theta: theta_5})

T56 = T.subs({d: 0.14, a: 0, alpha: 0})
T56 = T56.subs({theta: theta_6})

# Ahora podemos calcular la transformación total desde la base hasta el efector final
T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_simplified = T06.applyfunc(sp.simplify)

# Y asignamos valores a los ángulos de cada joint
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0) - sp.pi/2
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06_simplified.subs({theta_1: joint1, theta_2: joint2, theta_3: joint3, theta_4: joint4, theta_5: joint5, theta_6: joint6})
# sp.pprint(T06_solved)


#Refefencia TOrigen
T0 = rotz(0, unit = "deg")
trplot(T0, length = 0.7, color = 'k', frame = '0')

T01_n = T01.subs({theta_1: joint1})
T01_n = np.array(T01_n).astype(np.float64)
trplot(T01_n, length = 0.7, color = 'b', frame = '1')

# Luego podemos ir añadiendo cada transformación para mostrar cada frame de referencia
T12_n = T12.subs({theta_2: joint2})
T02_n = T01_n @ T12_n
T02_n = np.array(T02_n).astype(np.float64)
trplot(T02_n, length = 0.7, color = 'r', frame = '2')

T23_n = T23.subs({theta_3: joint3})
T03_n = T02_n @ T23_n
T03_n = np.array(T03_n).astype(np.float64)
trplot(T03_n, length = 0.7, color = 'g', frame = '3')

T34_n = T34.subs({theta_4: joint4})
T04_n = T03_n @ T34_n
T04_n = np.array(T04_n).astype(np.float64)
trplot(T04_n, length = 0.7, color = 'm', frame = '4')

T45_n = T45.subs({theta_5: joint5})
T05_n = T04_n @ T45_n
T05_n = np.array(T05_n).astype(np.float64)
trplot(T05_n, length = 0.7, color = 'y', frame = '5')

T56_n = T56.subs({theta_6: joint6})
T06_n = T05_n @ T56_n
T06_n = np.array(T06_n).astype(np.float64)
trplot(T06_n, length = 0.7, color = 'c', frame = '6')

# Y finalmente mostramos el plot
plt.grid(True)
plt.title('Brazo irB4400')
plt.axis('equal')
plt.show()