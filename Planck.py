import matplotlib.pyplot as plt
import math

def planck(wave, temp):
    'Gives intensity of radiation as a function of wavelength and temperature for a blackbody'
    'Intenstiy is in Watts per sr per m^3, wave is in nanometers, and temp is in kelvin'
    
    #initial condition, wavelength must be positive
    if wave <= 0:
        return 

    #constants
    h = 6.62607041*(10**-34) #Joules per second
    c = 299792458 #meters per second
    k = 1.38064853*(10**-23) #Joules per Kelvin

    #convert wavelength to meters
    wave_m = (wave * (10**-9))

    #break the function up into two parts, B1 and B2
    B1 = ((2 * h * (c**2))/(wave_m**5))
    B2 = (math.exp((h * c)/(wave_m * k * temp)) - 1)

    #final intensity B, converting wave back to nanometers
    B = (B1 * (1/B2)) / (10**9)

    return B

#breaks for higher energy wavelengths, with 4nm being the breakpoint 
#so have your range of some form: waves = range(x > 3, y)
#where x is the higher energy and y is the lower energy
def Blackbody(waves, temp):
    'Plots blackbody distribution for some temperature over a wavelength range'
    
    #use Wien's law to get peak wavelength in nm
    peak_w = ((2.898*(10**6))/temp)
    
    #calculate list of intensities for wavelength range
    intensities = []
    for value in waves:
        intensities.append(planck(value,temp))

    #get peak intentsity
    peak_i = max(intensities)

    #the rest formats the plot and displays it
    s = "peak intensity: %d\npeak wavelength: %d" %(peak_i, peak_w)
    
    plt.plot(waves,intensities)
    plt.axis([min(waves),max(waves),0,(peak_i + (peak_i*0.2))])
    plt.title("Blackbody radiation for t = %dk" %(temp))
    plt.xlabel("$Wavelength (nm)$")
    plt.ylabel(r"$B_\lambda$ ($W$ $sr^{-1}$ $m^{-2}$ $nm^{-1}$)")
    plt.text(peak_w, peak_i + (peak_i*0.05), s) #displays the peak intensity and wavelength
    plt.show()

    return

    
