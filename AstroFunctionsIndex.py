#AstroFunctions Index: Holds functions that handle the user requests from AstroFunctionsMain

import Planck
import PhasePlot

#planck fucntion handler
def planckCall():
    print()
    print("Enter wavelength range (in meters) and temperature (in Kelvin) or 'quit' to end.")
    initialWave = input("Initial wavelength: ")
    if (initialWave.lower() == "quit"):
        print()
        return
    finalWave = input("Final wavelength: ")
    if (finalWave.lower() == "quit"):
        print()
        return
    temp = input("Temperature: ")
    if (temp.lower() == "quit"):
        print()
        return

    try:
        Planck.Blackbody(range(int(initialWave),int(finalWave)+1),int(temp))
        return
    except:
        print("Invalid values")
        return


#phase plot call handler
def phaseCall():
    filename = input("Enter the filename to be plotted: ")
    try:
        PhasePlot.phasePlot(filename)
        return
    except:
        print("Invalid file")
        return

