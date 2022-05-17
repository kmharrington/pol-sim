import numpy as np

def get_J_rot(angle):
    J_rot = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)],
    ], dtype='complex')
    return J_rot

def get_J_LinPol(theta):
    J_pol = np.array([
        [1,0],
        [0,0]
    ], dtype='complex')
    J_rot = get_J_rot(theta)
    return np.dot( J_rot.transpose(), np.dot(J_pol, J_rot))

def get_J_LinPol_gridEff(theta, eta_grid=0.98):
    ## ignoring phase effects
    tx = np.sqrt((1+eta_grid)/2)
    ty = np.sqrt((1-eta_grid)/2)
    
    J_pol = np.array([
        [tx,0],
        [0,ty]
    ], dtype='complex')
    J_rot = get_J_rot(theta)
    return np.dot( J_rot.transpose(), np.dot(J_pol, J_rot))

## don't actually use this
#def get_J_det(phi):
#    return np.array([[np.cos(phi), -np.sin(phi)]], dtype='complex')
