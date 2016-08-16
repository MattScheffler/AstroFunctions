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
        print()
        print("Invalid values")
        return


#phase plot call handler
def phaseCall():
    print()
    while (1):
        choice = input("Plot with errors? Yes or no: ")
        if (choice.lower() == "yes"):
            filename = input("Enter the filename to be plotted: ")
            title = input("Enter the plot title: ")
            try:
                PhasePlot.phasePlotError(filename, title)
                return
            except:
                print()
                print("Invalid file")
                return
        elif (choice.lower() == "no"):
            filename = input("Enter the filename to be plotted: ")
            title = input("Enter the plot title: ")
            try:
                PhasePlot.phasePlot(filename, title)
                return
            except:
                print()
                print("Invalid file")
                return
        else:
            continue

