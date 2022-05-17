import numpy as np


A = np.array([
    [1,0,0,1],
    [1,0,0,-1],
    [0,1,1,0],
    [0,-1.0j, 1.0j,0],
])

def Jones_to_Muller(J):
    return np.real(np.dot(A, np.dot( np.kron( J, np.conjugate(J) ), np.linalg.inv(A))))

def Evec_to_Stokes(E):
    oneD = len(np.shape(E))==1
    if oneD:
        E = np.atleast_2d(E)
    row = np.shape(E)[1] == 2
    col = np.shape(E)[1] == 1
    if row:
        Ex = E[0,0]
        Ey = E[0,1]
    if col:
        Ex = E[0,0]
        Ey = E[1,0]
    
    stokes = np.array([[
        np.abs(Ex)**2 + np.abs(Ey)**2,
        np.abs(Ex)**2 - np.abs(Ey)**2,
        2*np.real( Ex*np.conjugate(Ey)),
        np.real(1.0j*(Ex*np.conjugate(Ey) - np.conjugate(Ex)*Ey))
    ]])
    
    if col:
        return np.transpose(stokes)
    if oneD:
        return stokes[0]
    return stokes
