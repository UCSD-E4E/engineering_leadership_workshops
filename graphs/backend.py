'''Lighting Power Models
'''
import numpy as np


def exposure_model(
        phi_sigma,
        z_sigma,
        theta_sigma,
        N_c,
        omega_c,
        I_c,
        z_c,
        z_s,
        r_s,
        E_vA,
        z_d,
        k=10.,
        q=0.65):
    a_sigma = np.pi * np.power(z_sigma * np.arctan2(theta_sigma, 2), 2)
    e_vssigma = phi_sigma / a_sigma * np.exp(-1.7/z_d * z_sigma)
    e_vsA = E_vA * np.exp(-1.7 / z_d * z_s)
    return k / q * np.power(N_c, 2) * omega_c / I_c / r_s * np.exp(1.7 * z_c / z_d) / (e_vssigma + e_vsA)


def solid_camera_angle(
        w_c,
        h_c,
        f_c):
    return 4 * np.arctan2(w_c * h_c, 2 * f_c * np.sqrt(4 * np.power(f_c, 2) + np.power(w_c, 2) + np.power(h_c, 2)))
