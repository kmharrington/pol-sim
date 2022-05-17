"""Angle units are always in radians
"""
import numpy as np

from .utils import *

def get_M_rot(angle):
    """Get the Mueller Rotation Matrix
    """
    M_rot = np.array([
        [1, 0, 0, 0],
        [0, np.cos(2*angle), np.sin(2*angle), 0],
        [0,-np.sin(2*angle), np.cos(2*angle), 0],
        [0, 0, 0, 1]
    ])
    return M_rot


def get_M_LinPol(theta):
    """
    Get a perfect linear polarizer that allows transmission along 
    theta
    """
    M_pol = 0.5*np.array([
        [ 1, 1, 0, 0],
        [ 1, 1, 0, 0],
        [ 0, 0, 0, 0],
        [ 0, 0, 0, 0],
    ])

    m_rot = get_M_rot(theta)
    return np.dot( m_rot.transpose(), np.dot(M_pol, m_rot))

def get_M_instrument_polarization(lambda_P, phi_P):
    """
    Return one sort of instrument polarization where the induced polarization is
    along phi_P. 
    """
    a = np.sqrt(1-np.abs(2*lambda_P))
    M_IP = 0.5*np.array([
        [1+a**2, 1-a**2, 0, 0],
        [1-a**2, 1+a**2, 0, 0],
        [0, 0, 2*a, 0],
        [0, 0, 0, 2*a]
    ])
    m_rot = get_M_rot(phi_P)
    return np.dot( m_rot.transpose(), np.dot(M_IP, m_rot))

def get_M_grid(theta, eta_grid=1):
    """
    Return the Mueller matrix for an imperfect wire grid.
    """
    M_grid = 0.5*np.array([
         [1, eta_grid, 0, 0],
         [eta_grid, 1, 0, 0],
         [0, 0, 1-eta_grid**2, -np.sqrt(1-eta_grid**2)],
         [0, 0, np.sqrt(1-eta_grid**2), 1-eta_grid**2],
    ])
    m_rot = get_M_rot(theta)
    return np.dot( m_rot.transpose(), np.dot(M_grid, m_rot))

def get_M_det(phi, chi=0):
    """Get a Stokes row vector that can be used as a detector
    aligned along an angle phi with cross-pol chi
    """
    eps = np.sqrt(chi)
    M = Jones_to_Muller(
        np.array([
            [1,0],
            [0,eps]
        ])
    )
    M = np.dot( M, get_M_rot(phi))
    return np.dot( np.array([[1,0,0,0]]), M)

