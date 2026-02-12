import roboticstoolbox as tb
import numpy as np

robot = tb.models.DH.Puma560()

#Variables articulares
q = [0,np.deg2rad(30), -np.deg2rad(160),0,0,0]

robot.teach(q)