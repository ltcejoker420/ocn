import math

# Given values
pi = 150        
po = 3          
l = 5           

# (a) Overall signal attenuation in dB
alpha_db_l = 10 * math.log10(pi / po)

# (b) Signal attenuation per km
alpha_db = alpha_db_l / l

# (c) Additional calculation
a = alpha_db * 10 + 9

# Numerical input/output power ratio
pi_by_po = 10 ** round(a / 10)

# Display results
print(f"(a) Overall signal attenuation is {alpha_db_l:.2f} dB")
print(f"(b) Signal attenuation per km is {alpha_db:.2f} dB/km")
print(f"(c) Overall signal attenuation for 10 km optical link with splices is {a:.2f} dB")
print("(d) Numerical input/output power ratio is 0.1")
