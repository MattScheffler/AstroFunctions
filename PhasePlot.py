#Phase diagram plot program
#file format should be .csv or .txt
#with desired columns labeled 'phase' and 'magnitude' and 'error' unless the code is changed.

import matplotlib.pyplot as plt
import csv

def phasePlot(filename, title=""):
    'Plot a phase diagram from a file'
    #make empty lists to store the relevant data
    phases = []
    magnitudes = []

    #read in the values from the file and store data in the lists
    with open(filename) as file:
        for row in csv.DictReader(file):
            phases.append(float(row["phase"]))
            magnitudes.append(float(row["magnitude"]))

    #To make the plot show the system over two phases,
    #append each phase and then (phase + 1) to a new phase list
    #and append each magnitude to a new magnitude list twice
    plotMags = []
    plotPhases = []
    for value in phases:
        plotPhases.append(value)
    for value in phases:
        plotPhases.append(value+1)
    for value in magnitudes:
        plotMags.append(value)
    for value in magnitudes:
        plotMags.append(value)
        
    #set up the plot
    plt.plot(plotPhases, plotMags, 'r')
    plt.axis([0.0,2.0,max(magnitudes)+1,min(magnitudes)-1])
    plt.title(title)
    plt.xlabel("Phase")
    plt.ylabel("Magnitude")
    plt.show()

    return

def phasePlotError(filename, title=""):
    'Plot a phase diagram from a file with errors'
    #make empty lists to store the relevant data
    phases = []
    magnitudes = []
    errors = []

    #read in the values from the file and store data in the lists
    with open(filename) as file:
        for row in csv.DictReader(file):
            phases.append(float(row["phase"]))
            magnitudes.append(float(row["magnitude"]))
            errors.append(float(row["error"]))

    #To make the plot show the system over two phases,
    #append each phase and then (phase + 1) to a new phase list
    #and append each magnitude to a new magnitude list twice
    #and append errors twice
    plotMags = []
    plotPhases = []
    plotErrors= []
    for value in phases:
        plotPhases.append(value)
    for value in phases:
        plotPhases.append(value+1)
    for value in magnitudes:
        plotMags.append(value)
    for value in magnitudes:
        plotMags.append(value)
    for value in errors:
        plotErrors.append(value)
    for value in errors:
        plotErrors.append(value)
        
    #set up the plot
    plt.errorbar(plotPhases, plotMags, yerr = plotErrors, xerr = None, fmt='r', ecolor='b')
    plt.axis([0.0,2.0,max(magnitudes)+1,min(magnitudes)-1])
    plt.title(title)
    plt.xlabel("Phase")
    plt.ylabel("Magnitude")
    plt.show()

    return
