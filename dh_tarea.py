import sympy as sp
from sympy.matrices import rot_axis3
# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np
#Para usar el DH
import roboticstoolbox as rtb

# Definimos variables simbólicas para cada parámetro del DH
theta,d,a,alpha= sp.symbols('theta,d,a,alpha')

# Construimos la matriz de transformación homogénea de DH
TDH = sp.Matrix(trotz(theta) @ transl(0,0,d) @ transl(a,0,0) @ trotx(alpha))

# También declaramos variables simbólicas para cada joint de un robot de 6 grados de libertad
theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1, theta2, theta3, theta4, theta5, theta6')

# Y comenzamos a armar las matrices de transformación para cada joint usando la tabla DH dada
T01 = TDH.subs({d: 0.4865, a:0.15, alpha: sp.pi/2, theta: theta1})

T12 = TDH.subs({d:0, a:0.7 , alpha:0, theta: theta2})

T23 = TDH.subs({d:0, a:0.11, alpha: sp.pi/2, theta: theta3})

T34 = TDH.subs({d:0.678, a:0, alpha: -sp.pi/2, theta: theta4})

T45 = TDH.subs({d:0, a:0, alpha: sp.pi/2, theta: theta5})

T56 = TDH.subs({d:0.135, a:0, alpha: 0, theta: theta6})

#Obtenemos la matriz de transformación total desde la base hasta el mounting point, es decir, T06
T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
# sp.pprint(T06)

# Ahora podemos evaluar esta matriz para un conjunto de ángulos donde todos son 0, y theta 2 es 90°
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0) + sp.pi/2
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)



# Ahora resolvemos la matriz de transformación total para estos ángulos específicos
T06_solved = T06.subs({theta1: joint1, theta2: joint2, theta3: joint3, theta4: joint4, theta5: joint5, theta6: joint6})
sp.pprint(T06_solved)

# Ahora podemos graficar el robot usando la función trplot de spatialmath
# Primero graficamos el sistema de coordenadas de la base
T0 = rotz(0, unit = "deg")
trplot(T0, length = 0.7, color = 'k', frame = '0')

# Luego graficamos cada una de las transformaciones desde la base hasta el mounting point
T01_n = np.array(T01.subs({theta1: joint1})).astype(np.float64)
trplot(T01_n, length = 0.7, color = 'r', frame = '1')

T12_n = np.array(T12.subs({theta2:joint2})).astype(np.float64)
T02_n = T01_n @ T12_n
trplot(T02_n, length = 0.7, color = 'g', frame = '2')

T23_n = np.array(T23.subs({theta3: joint3})).astype(np.float64)
T03_n = T02_n @ T23_n
trplot(T03_n, length = 0.7, color = 'b', frame = '3')

T34_n = np.array(T34.subs({theta4: joint4})).astype(np.float64)
T04_n = T03_n @ T34_n
trplot(T04_n, length = 0.7, color = 'm', frame = '4')

T45_n = np.array(T45.subs({theta5: joint5})).astype(np.float64)
T05_n = T04_n @ T45_n
trplot(T05_n, length = 0.7, color = 'y', frame = '5')

T56_n = np.array(T56.subs({theta6:joint6})).astype(np.float64)
T06_n = T05_n @ T56_n
trplot(T06_n, length = 0.7, color = 'c', frame = '6')

# Y por último mostramos el plot
plt.grid(True)
plt.title('Brazo irb1660-4/1.55')
plt.axis('equal')
plt.show()