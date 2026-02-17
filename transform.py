import roboticstoolbox as rtb 
import numpy as np 
import matplotlib.pyplot as plt 
from spatialmath import * 
from spatialmath.base import * 
from sympy import Symbol, Matrix 
theta = Symbol('theta') 


T0 = transl2(0,0) #Referencia del sistema de coordenadas global
trplot2(T0, frame = "0", color = 'k') 

#Traslación de la 1 a 2 seguida de rotación 30 grados
TA = transl2(1,2) @ trot2(30,"deg")
print(TA)
trplot2(TA, frame = "A", color = 'b')

P = np.array([4,3])
plot_point(P, "ko", text = "P")

P1 = homtrans(np.linalg.inv(TA),P)
print(P1)


plt.axis('equal') 
plt.grid(True) 
plt.xlabel('X') 
plt.ylabel('Y') 
plt.title('Transformación 2D') 
plt.show() #Mostrar ventanas