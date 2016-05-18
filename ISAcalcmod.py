#ISA Module
#Midas Gossye (c) 2016

import math as mt

# Troposphere parameters:
a_tropo = -0.0065 #K/m
T_tropo = 288.15 #K
p_tropo = 101325 #Pa
Rho_tropo = 1.225 #kg/m^3

# Tropopause parameters:
a_tropop = 0 #K/m
T_tropop = 216.650 #K
p_tropop = 22625.79 #Pa
Rho_tropop = 0.363817 #kg/m^3

# Stratosphere 1 parameters:
a_strato = 0.001 #K/m
T_strato = 216.650 #K
p_strato = 5471.935 #Pa
Rho_strato = 0.087945 #kg/m^3

# Stratosphere 2 parameters:
a_strato2 = 0.0028 #K/m
T_strato2 = 228.65 #K
p_strato2 = 867.255 #Pa
Rho_strato2 = 0.01321 #kg/m^3

# Stratopause parameters:
a_stratop = 0 #K/m
T_stratop = 270.65 #K
p_stratop = 110.767 #Pa
Rho_stratop = 0.00142537 #kg/m^3

# Mesosphere parameters:
a_meso = -0.0028 #K/m
T_meso = 270.65 #K
p_meso = 66.849 #Pa
Rho_meso = 0.00086007 #kg/m^3

# Mesosphere2 parameters:
a_meso2 = -0.002 #K/m
T_meso2 = 214.65 #K
p_meso2 = 3.9490 #Pa
Rho_meso2 = 6.406308156295668e-05 #kg/m^3

# Mesopause parameters:
a_mesop = 0 #K/m
T_mesop = 186.946#K
p_mesop = 0.372521#Pa
Rho_mesop = 6.938822244547459e-06 #kg/m^3


def calcAtmosphere(h):
    if h < 11000:
        T = T_tropo + a_tropo*h
        p = p_tropo * ((T/T_tropo)**(-9.80665/(a_tropo*287)))
        Rho = Rho_tropo *((T/T_tropo)**((-9.80665/(a_tropo*287))-1))


    elif h < 20000:
        T = T_tropop
        p = p_tropop*mt.exp((-9.80665/(287*T))*(h-11000))
        Rho = Rho_tropop*mt.exp((-9.81/(287*T))*(h-11000))

    elif h < 32000:
        T = T_strato + a_strato*(h-20000)
        p = p_strato * ((T/T_strato)**(-9.80665/(a_strato*287)))
        Rho = Rho_strato*((T/T_strato)**((-9.80665/(a_strato*287))-1))

    elif h < 47000:
        T = T_strato2 + a_strato2*(h-32000)
        p = p_strato2 * ((T/T_strato2)**(-9.80665/(a_strato2*287)))
        Rho = Rho_strato2*((T/T_strato2)**((-9.80665/(a_strato2*287))-1))

    elif h < 51000:
        T = T_stratop
        p = p_stratop*mt.exp((-9.80665/(287*T))*(h-47000))
        Rho = Rho_stratop*mt.exp((-9.81/(287*T))*(h-47000))

    elif h < 71000:
        T = T_meso + a_meso*(h-51000)
        p = p_meso * ((T/T_meso)**(-9.80665/(a_meso*287)))
        Rho = Rho_meso*((T/T_meso)**((-9.80665/(a_meso*287))-1))

    elif h < 84852:
        T = T_meso2 + a_meso2*(h-71000)
        p = p_meso2 * ((T/T_meso2)**(-9.80665/(a_meso2*287)))
        Rho = Rho_meso2*((T/T_meso2)**((-9.80665/(a_meso2*287))-1))

    elif h <= 100000:
        T = T_mesop
        p = p_mesop
        Rho = Rho_mesop

    else:
        T = T_mesop - 0.001*(h-100000)
        if T < 0:
            T = 0
        p = 0
        Rho = 0
        

    return T,p,Rho

def Altconvert(conversion, h):

    if conversion == 'ft':
        result = h*3.2808399
    elif conversion == 'm':
        result = h*0.3048
    else :
        result = 0

    return result

