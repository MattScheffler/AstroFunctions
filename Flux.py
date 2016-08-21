#Flux/Luminosity calculator
import math

def flux(L, d):
    'Calculates flux of a star at distance d from the center with luminosity L'
    'units of flux returned depend on input units'
    flux = (L/(4*math.pi*math.pow(d,2)))

    return flux

def luminosity(F, d):
    'Calculates the luminosity of a star with flux F at a distance d'
    'Units of luminosity will depend on input units'

    L = F*4*math.pi*math.pow(d, 2)

    return L
