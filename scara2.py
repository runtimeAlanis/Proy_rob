import roboticstoolbox as rtb 
import numpy as np 
import matplotlib.pyplot as plt 
from spatialmath import * 
from spatialmath.base import * 
from sympy import *
from sympy import Symbol, Matrix, simplify
from sympy.matrices import rot_axis3
theta = Symbol('theta') 

theta1, L1, theta2, L2 = symbols ('theta1 L1 theta2 L2')

T01 = trotz(theta1) @ transl(L1,0,0)
print(f'Primera transformación: \n{T01}\n')

T12 = trotz(theta2) @ transl(L2,0,0)
print(f'Segunda transformación: \n{T12}\n')

T02 = T01 @ T12
print(f'Transformación completa: \n{T02}\n')
#Ahora se puede obtener la posición del efector final respecto
### a la base, que es el origen del sistema de coordenadas global
M = Matrix(T02) 
M_simplified = simplify(M)

print(print(M_simplified))
print("\n")

#Sustituir con valores numéricos
M_evaluated = M_simplified.subs({theta1: 30, L1: 4, theta2: 45, L2: 3})
print(f'Matriz con valores numéricos: \n{M_evaluated}\n')