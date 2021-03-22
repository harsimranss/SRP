#setting initial variables
    #Wavelength in meters
lambda_1=1

    #Angular resolution in arcsec
import math
Theta_res=1
Theta_resr=(Theta_res/3600)*(math.pi/180)
print(Theta_resr)
# tapering constant
b_tap=1.22 #for circular aperture

# alpha
alpha=5.93 # for circular aperture

# beam efficiency
n_b=0.9

# total main beam angle Omega_m
Omega_m=(alpha*(Theta_resr)**2)/(b_tap**2)

# Main beam solid Angle Omega_mb
Omega_mb=n_b*1.13*((Theta_resr)**2)
print("Beam solid Angle is {:.2f} x 10^(-9)".format(Omega_mb*(10**9)))
# source size in units of 10^(-9)steradian
size_source1=input("enter size of source in units of 10^(-9) steradians")
size_source=float(size_source1)*(10**(-9))

# beam filling factor
beam_factor=size_source/Omega_mb

if beam_factor>=1:
    beam_factor=1

print("Beam filling factor is {:.3f}".format(beam_factor))
# calculating brightness temperature
S_v=float(input("enter flux density in mili jansky"))
T_b= ((lambda_1**2)*(3.62*(10**(-7))*S_v))/(Omega_m*beam_factor)

print("brightness temperature is {:.4f} k".format(T_b))
