#AstroFunctions Index: Holds functions that handle the user requests from AstroFunctionsMain

import Planck
import PhasePlot
import Kepler

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

#kepler call handler
def keplerCall():
    print()
    while (1):
        print("Enter the number of what you want to solve for, enter 'quit' to end:")
        print("1. Total mass.")
        print("2. Orbital period.")
        print("3. Semi-major axis.")
        choice = input()
        if (choice.lower() == "quit"):
            return
        elif (choice == "1"):
            print()
            print("Enter period in days and semi-major axis in AU.")
            period = input("Period: ")
            a = input("Semi-major axis: ")
            try:
                print()
                print("Total mass:", Kepler.keplerMass(float(period), float(a)), "solar masses")
                print()
            except:
                print()
                print("Invalid values")
                print()
        elif (choice == "2"):
            print()
            print("Enter mass in solar masses and semi-major axis in AU.")
            mass = input("Enter mass: ")
            a = input("Enter semi-major axis: ")
            try:
                print()
                print("Orbital period:", Kepler.keplerPeriod(float(mass), float(a)), "days")
                print()
            except:
                print()
                print("Invalid values")
                print()
        elif (choice == "3"):
            print()
            print("Enter mass in solar masses and period in days.")
            mass = input("Enter mass: ")
            period = input("Enter period: ")
            try:
                print()
                print("Semi-major axis:", Kepler.keplerAxis(float(mass), float(period)), "AU")
                print()
            except:
                print()
                print("Invalid values")
                print()
        else:
            print()
            continue
        
