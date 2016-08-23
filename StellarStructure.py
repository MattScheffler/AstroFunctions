#Plots the density and mass of a star as a function of radius for a given density distribution.
from math import pow, pi
import matplotlib.pyplot as plt

#current density form, used in AstroFunctionsIndex
densityFormula = "central_density*(1 - (r/R)^2)"

#density for a radius value r, with the star's total mass M and total radius R
def density(r, R, M):
    #central density
    rho_c = ((15*M)/(8*pi*pow(R,3)))

    rho = rho_c*(1 - pow(r/R,2))

    return rho

#mass for a radius value r, with the star's total mass M and total radius R
def mass(r, R, M):
    #central density
    rho_c = (15*M)/(8*pi*pow(R,3))

    mass = 4*pi*rho_c*((pow(r,3)/3)-(pow(r,5)/(5*pow(R,2))))

    return mass

#plotting functions, input the range of radii that you want to plot, and the star's radius/mass
def densityPlot(radii, R, M):
    if (M < 0):
        return
    densities = []
    for radius in radii:
        if (radius < 0):
            continue
        else:
            densities.append(density(radius, R, M))

    plt.plot(radii, densities)
    plt.axis([0,R,0,max(densities)])
    plt.title(r"Density vs. Radius for $\rho$ = $\rho_c$$(1-(\frac{r}{R})^2)$")
    plt.xlabel("Radius")
    plt.ylabel("Density")
    plt.show()

    return

def massPlot(radii, R, M):
    if (M < 0):
        return
    masses = []
    for radius in radii:
        if (radius < 0):
            continue
        else:
            masses.append(mass(radius, R, M))

    plt.plot(radii, masses)
    plt.axis([0,R,0,M])
    plt.title("Mass vs. Radius")
    plt.xlabel("Radius")
    plt.ylabel("Mass")
    plt.show()

    return
