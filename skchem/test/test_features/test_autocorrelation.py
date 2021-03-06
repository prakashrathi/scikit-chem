#! /usr/bin/env python
#
# Copyright (C) 2016 Rich Lewis <rl403@cam.ac.uk>
# License: 3-clause BSD

"""
# skchem.test.test_features.test_autocorrelation

Tests for autocorrelation descriptors.
"""


import pytest
import numpy as np

from . import phenethylamine

from ...features.descriptors.autocorrelation import (
    moreau_broto_autocorrelation,
    moran_coefficient,
    geary_coefficient
)

ats_data = [(('H', 'H'), [2.952, 3.313, 3.473, 3.554]),
        (('H', 'F'), [3.032, 3.422, 3.567, 3.598]),
        (('H', 'Cl'), [3.096, 3.508, 3.641, 3.635]),
        (('H', 'Br'), [3.251, 3.708, 3.819, 3.728]),
        (('H', 'I'), [3.392, 3.884, 3.977, 3.818]),
        (('H', 'C'), [3.003, 3.383, 3.533, 3.582]),
        (('F', 'H'), [3.032, 3.422, 3.567, 3.64]),
        (('Cl', 'H'), [3.096, 3.508, 3.641, 3.71]),
        (('Br', 'H'), [3.251, 3.708, 3.819, 3.876]),
        (('I', 'H'), [3.392, 3.884, 3.977, 4.027]),
        (('C', 'H'), [3.003, 3.383, 3.533, 3.609]),
        (('Cl', 'F'), [3.165, 3.598, 3.828, 3.748]),
        (('Br', 'F'), [3.31, 3.783, 4.081, 3.909]),
        (('C', 'F'), [3.079, 3.485, 3.663, 3.651]),
        (('Cl', 'Cl'), [3.221, 3.671, 3.966, 3.78]),
        (('Br', 'Cl'), [3.359, 3.843, 4.264, 3.936]),
        (('C', 'Cl'), [3.14, 3.566, 3.763, 3.686]),
        (('Cl', 'Br'), [3.359, 3.843, 4.264, 3.861]),
        (('Br', 'Br'), [3.48, 3.991, 4.636, 4.006]),
        (('C', 'Br'), [3.289, 3.756, 3.993, 3.775]),
        (('C', 'C'), [3.052, 3.449, 3.617, 3.636]),
        (('Br', 'C'), [3.289, 3.756, 3.993, 3.897])]


@pytest.mark.parametrize('atoms, expected', ats_data)
def test_ats(atoms, expected):
    mol = phenethylamine(*atoms)
    ans = np.log(moreau_broto_autocorrelation(mol, prop_name='atomic_mass',
                                        c_scaled=True, ks=range(1, 5)))
    assert np.allclose(ans, expected, atol=0.075)  # quite high tolerance


moran_data = [(('H', 'H'), [-0.006, -0.056, -0.139, -0.319]),
              (('H', 'F'), [-0.006, -0.055, -0.134, -0.322]),
              (('H', 'Cl'), [-0.006, -0.077, -0.177, -0.368]),
              (('H', 'Br'), [-0.005, -0.098, -0.203, -0.32]),
              (('H', 'I'), [-0.004, -0.09, -0.174, -0.223]),
              (('H', 'C'), [-0.005, -0.045, -0.112, -0.29]),
              (('F', 'H'), [-0.006, -0.055, -0.134, -0.299]),
              (('Cl', 'H'), [-0.006, -0.077, -0.177, -0.366]),
              (('Br', 'H'), [-0.005, -0.098, -0.203, -0.374]),
              (('I', 'H'), [-0.004, -0.09, -0.174, -0.3]),
              (('C', 'H'), [-0.005, -0.045, -0.112, -0.261]),
              (('Cl', 'F'), [-0.006, -0.073, -0.159, -0.365]),
              (('Br', 'F'), [-0.005, -0.089, -0.194, -0.364]),
              (('C', 'F'), [-0.005, -0.045, -0.106, -0.266]),
              (('Cl', 'Cl'), [-0.007, -0.095, -0.159, -0.403]),
              (('Br', 'Cl'), [-0.006, -0.109, -0.141, -0.398]),
              (('C', 'Cl'), [-0.006, -0.063, -0.157, -0.302]),
              (('Cl', 'Br'), [-0.006, -0.109, -0.141, -0.333]),
              (('Br', 'Br'), [-0.005, -0.13, -0.029, -0.372]),
              (('C', 'Br'), [-0.005, -0.08, -0.214, -0.257]),
              (('C', 'C'), [-0.005, -0.037, -0.083, -0.241]),
              (('Br', 'C'), [-0.005, -0.08, -0.214, -0.342])]


@pytest.mark.parametrize('atoms, expected', moran_data)
def test_moran(atoms, expected):
    mol = phenethylamine(*atoms)
    ans = moran_coefficient(mol, prop_name='atomic_mass',
                            c_scaled=False, ks=range(1, 5))
    assert np.allclose(ans, expected, atol=0.05)


geary_data = [(('H', 'H'), [0.504, 0.804, 1.364, 2.193]),
              (('H', 'F'), [0.512, 0.782, 1.299, 2.198]),
              (('H', 'Cl'), [0.531, 0.811, 1.306, 2.114]),
              (('H', 'Br'), [0.549, 0.838, 1.174, 1.485]),
              (('H', 'I'), [0.542, 0.828, 1.053, 1.042]),
              (('H', 'C'), [0.503, 0.768, 1.28, 2.176]),
              (('F', 'H'), [0.512, 0.782, 1.299, 2.034]),
              (('Cl', 'H'), [0.531, 0.811, 1.306, 2.008]),
              (('Br', 'H'), [0.549, 0.838, 1.174, 1.645]),
              (('I', 'H'), [0.542, 0.828, 1.053, 1.363]),
              (('C', 'H'), [0.503, 0.768, 1.28, 2.009]),
              (('Cl', 'F'), [0.539, 0.793, 1.208, 2.025]),
              (('Br', 'F'), [0.554, 0.816, 1.235, 1.655]),
              (('C', 'F'), [0.511, 0.752, 1.168, 2.025]),
              (('Cl', 'Cl'), [0.561, 0.825, 1.201, 1.969]),
              (('Br', 'Cl'), [0.574, 0.845, 1.18, 1.655]),
              (('C', 'Cl'), [0.529, 0.778, 1.21, 1.942]),
              (('Cl', 'Br'), [0.574, 0.845, 1.18, 1.417]),
              (('Br', 'Br'), [0.594, 0.875, 1.069, 1.386]),
              (('C', 'Br'), [0.545, 0.802, 1.257, 1.361]),
              (('C', 'C'), [0.503, 0.74, 1.149, 2.008]),
              (('Br', 'C'), [0.545, 0.802, 1.257, 1.633])]


@pytest.mark.parametrize('atoms, expected', geary_data)
def test_geary(atoms, expected):
    mol = phenethylamine(*atoms)
    ans = geary_coefficient(mol, prop_name='atomic_mass',
                            c_scaled=False, ks=range(1, 5))
    assert np.allclose(ans, expected, atol=0.05)

