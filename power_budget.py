# Program to find power budget
N = [5, 10, 50]
alpha = float(input("Enter attenuation in dB per km: "))
lp = float(input("Enter coupling loss in dB: "))
lth = float(input("Enter coupling throughput in dB: "))
li = float(input("Enter intrinsic coupling loss in dB: "))
lc = float(input("Enter coupler to fiber loss in dB: "))
l = float(input("Enter link length in km: "))

# Fiber loss
Fl = alpha * l

print("Fiber Loss =", Fl, "dB")

# Power budget calculation
for n in N:
    pbudget = n * ((alpha * l + 2 * lc + li + lth) - alpha * l - 2 * lth + 2 * lp)
    print("Power Budget for N =", n, "is", pbudget, "dB")
 
#Enter attenuation in dB per km: 5    
#Enter coupling loss in dB: 10
#Enter coupling throughput in dB: 50
#Enter intrinsic coupling loss in dB: 15
#Enter coupler to fiber loss in dB: 25
#Enter link length in km: 14
