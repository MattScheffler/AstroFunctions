#AstroFunctions Index: Holds functions that handle the user requests from AstroFunctionsMain

import Planck
import PhasePlot

#planck fucntion handler
#this currently only uses integer values due to the limitaions of range()
def planckCall():
    print()
    print("Enter wavelength range (in nanometers) and temperature (in Kelvin) or 'quit' to end.")
    initialWave = input("Shortest wavelength: ")
    if (initialWave.lower() == "quit"):
        print()
        return
    finalWave = input("Longest wavelength: ")
    if (finalWave.lower() == "quit"):
        print()
        return
    temp = input("Temperature: ")
    if (temp.lower() == "quit"):
        print()
        return

    try:
        #int(float()) conversion used if user enters a float, range() requires int
        Planck.Blackbody(range(int(float(initialWave)),int(float(finalWave)+1)),int(float(temp)))
        return
    except:
        print("Invalid values")
        return


#phase plot call handler
def phaseCall():
    print()
    filename = input("Enter the filename to be plotted: ")
    try:
        PhasePlot.phasePlot(filename)
        return
    except:
        print("Invalid file")
        return

