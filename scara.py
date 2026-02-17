import roboticstoolbox as rtb 
import numpy as np 
import matplotlib.pyplot as plt 
from spatialmath import * 
from spatialmath.base import * 
from sympy import Symbol, Matrix 
theta = Symbol('theta') 

T0 = transl2(0,0) #Referencia
trplot2(T0, frame = "0", color = "k")

#Rotación de seguida de traslación, repecto a T0
TA = trot2(30,"deg")
trplot2(TA,frame="A", color ="b")
plot_circle(4,(0,0),'b--')

#Para que la transformación sea respecto a TA
TBA = TA @ transl2(4,0) @ trot2(0,"deg")
trplot2(TBA, frame = "B", color = 'g')
origin_TBA = TBA[:2,2]
plot_circle(3, (origin_TBA[0], origin_TBA[1]), 'g--')

#Para que la transformación sea respecto a TBA, este es el gripper
TCBA = TBA @ transl2(3,0)
trplot2(TCBA, frame = "C", color = 'y')
print(TCBA)

origin_TCBA = TCBA[:2,2]
P = np.array([origin_TCBA[0], origin_TCBA[1]])
plot_point(P,"ko",text="p")
print("Coordenadas en T0: {:.4f},{:.4f}".format(P[0],P[1]))
print("Coordenadas en TBA: {:.4f},{:.4f}".format(origin_TBA[0],origin_TBA[1]))
print("Coordenadas en TCBA: {:.4f},{:.4f}".format(origin_TCBA[0],origin_TCBA[1]))


plt.axis('equal') 
plt.grid(True) 
plt.xlabel('X') 
plt.ylabel('Y') 
plt.title('Joints del SCARA') 
plt.show() #Mostrar ventanas