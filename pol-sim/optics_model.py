import numpy as np

from .utils import *
from . import mueller

def get_optics_model(thetas, params, source, norm=False):
    det_angle, grid_eff, lambda_P, phi_P, cross_pol = params
    outs = np.nan*np.zeros( (len(thetas),))

    M_OT = mueller.get_M_instrument_polarization(lambda_P, phi_P)
    det_stokes = mueller.get_M_det(det_angle, cross_pol) 
    
    for t, theta in enumerate(thetas):
        M_grid = mueller.get_M_grid(theta, eta_grid=grid_eff)
        S_at_det = np.dot( M_OT, np.dot(M_grid, source))
        
        outs[t] = np.dot( det_stokes, S_at_det)
    
    if norm:
        return outs/np.max(outs)
    return outs