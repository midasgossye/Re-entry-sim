from ISAcalcmod import calcAtmosphere, Altconvert #T,p,Rho, #(ft or m), h
import math as mt
from matplotlib import pyplot as plt

#Mercury space vehicle data:
mlbs = 2662.8 #lbs
m = mlbs * 0.45359237 #kg
S = 2.81 #m^2
Cd = 1.6 #-

#Drogue chute data:
Cddrogue = 1.75
Vdeploykts = 186 #kts
Vdeploy = Vdeploykts * 0.514444444 #m/s
drogue = False
main = False
Vtransfts = 225 #ft/s
Vtrans = Altconvert('m',Vtransfts)
Delta_t_chutes = 47 #s
Sdrogue = 0.724 #m^2

#Main parachute data:
calculated = False
Cdmain = 1.75
Vendfts = 32 #ft/s
Vend = Altconvert('m',Vendfts)
hendft = 9800 #ft
hend = Altconvert('m',hendft)
Delta_t_splash = 331 #s
Smain = 145 #m^2

#Constants:
G = 6.6741e-11 #Nm^2/kg^2
M = 5.972e24 #kg
Re = 6371 #km

#Start conditions:
h0ft = 325000 #ft
h0 = Altconvert('m',h0ft)
V0ft = 22500 #ft/s
V0 = 6858 #m/s
Gamma0 = -1.5 #deg

#Start!
h = h0
Gamma = -Gamma0
V = V0
vx = mt.cos(mt.radians(Gamma)) * V0
vy = -mt.sin(mt.radians(Gamma)) * V0
dt = 0.01
t = 0
x = 0
vylst = []
tlst = []
gravlst = []
hlst = []
hftlst = []
rholst = []
glst = []
aylst = []
xlst = []
Vlst = []
Vftlst = []
hmain2 = 0
while h > 0:
    if (V < Vdeploy) and (drogue == False):
        hdrogue = h
        drogue = True
        tdrogue1 = t
    if (V < Vtrans) and (main == False):
        tdrogue2 = t
        hmain = h
        main = True
    if (h < Altconvert('m',9800)) and (calculated == False):
        Vmain2 = Altconvert('ft',V) 
        calculated = True
    hlst.append(h)
    hft = Altconvert('ft',h)
    hftlst.append(hft/1000)
    vylst.append(vy)
    tlst.append(t/60)
    T,p,Rho = calcAtmosphere(h)
    rholst.append(Rho)
    Fdrag = Cd * 0.5 * Rho * (V**2) * S
    if drogue == True:
        
        Fdrogue = Cddrogue * 0.5 * Rho * (V**2) * Sdrogue
        
    else:
        
        Fdrogue = 0
        
    if main == True:

        Fmain = Cdmain * 0.5 * Rho * (V**2) * Smain

    else:

        Fmain = 0
       
    Fgrav = (G*M*m)/((Re*1000+h)**2)
    Frx = -mt.cos(mt.radians(Gamma))*(Fdrag + Fdrogue + Fmain)
    Fry = mt.sin(mt.radians(Gamma)) * (Fdrag + Fdrogue + Fmain) - Fgrav
    ax = Frx /m
    ay = Fry/m
    a = ((ax**2+ay**2)**0.5)
    glst.append((a/9.80665)+1)
    vx = ax*dt + vx
    vy = ay*dt + vy
    V = ((vx**2+vy**2)**0.5)
    Vft = Altconvert('ft',V)
    Vlst.append(V)
    Vftlst.append(Vft)
    Gamma = mt.degrees(mt.acos(vx/V))
    h = h + vy*dt
    x = x + vx*dt
    xlst.append(x/1000)
    t = t + dt
rangelst = []    
impact_x = xlst[-1]
for i in xrange(len(xlst)):
    rangelst.append(impact_x - xlst[i])
print "Drogue deploy h.=",hdrogue,"\t Delta t=", tdrogue2-tdrogue1, "\t Main h.=",Altconvert("ft",hmain)
print "V speed crit h.=",Vmain2
print "V splash =",Altconvert('ft',Vlst[-1])
print "Delta t main-splash =",tlst[-1]*60-tdrogue2
plt.subplot(221)
plt.grid()
plt.xlabel("time (min.)")
plt.ylabel("G force (-)")

plt.plot(tlst,glst)

plt.subplot(222)
plt.grid()
plt.xlabel("Altitude (kft)")
plt.ylabel("Speed (ft/s)")

plt.plot(hftlst,Vftlst)

plt.subplot(223)
plt.grid()
plt.xlabel("Range (km)")
plt.ylabel("Altitude (kft)")

plt.plot(rangelst,hftlst)

plt.subplot(224)
plt.grid()
plt.xlabel("Time (min.)")
plt.ylabel("Altitude (kft)")

plt.plot(tlst,hftlst)

plt.show()






