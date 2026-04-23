import math

# Given values
lambda_val = 0.85e-6      # wavelength (m)
c = 3e8                   # speed of light (m/s)
d2n = 0.025               # second derivative
sigma_lambda = 20e-9      # spectral width (m)
L = 1                     # distance (km)

# Material dispersion parameter
M = (lambda_val / c) * d2n   # in sec/m

# Convert to ps/nm·km
M_ps = M * 1e12 * 1e-9 * 1e3

# Pulse broadening
sigma_m = sigma_lambda * L * M_ps

print("Material Dispersion Parameter =", M_ps, "ps/nm·km")
print("Pulse Broadening =", sigma_m, "ns/km")
