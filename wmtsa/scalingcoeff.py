"""
This module contains functions returning the coefficients for
different wavelet scaling filters
"""
import numpy as np

def haar():
    """
    Return the coefficients for the Haar wavelet
    """
    return np.array([0.7071067811865475, \
                     0.7071067811865475])
