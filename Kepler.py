#Kepler's third law calculations
#Get total mass of a system, semimajor axis, or period or orbit

import math

#Day in seconds
Day = 86400
#gravitational constant, units Nm^2/kg^2
G = 6.67428*(math.pow(10, -11))
#astronomical unit in meters
AU = 1.495979*math.pow(10,11)
#solar mass in kilograms
Solar = 1.9891*math.pow(10, 30)

def keplerPeriod(mass, a):
    'Calculates the period of a system in days, given total mass and semimajor axis "a"'
    'mass should be in solar masses and a should be in AU'
    #calculate period squared first
    pSquared = ((4*math.pow(math.pi,2)*math.pow((a*AU),3))/(G*(mass*Solar)))

    #get period, in seconds
    pSeconds = math.pow(pSquared,0.5)
    
    #convert to days
    period = (pSeconds/Day)

    return period

def keplerAxis(mass, period):
    'Calculates the semimajor axis of a system in AU, given total mass and orbital period'
    'mass should be in solar masses and period should be in days'
    #get cube of axis first
    aCubed = ((math.pow((period*Day),2)*G*(mass*Solar))/(4*math.pow(math.pi,2)))

    #get axis in meters
    aMeters = math.pow(aCubed, (1/3))

    #convert to AU
    a = (aMeters/AU)
    
    return a

def keplerMass(period, a):
    'Calculates the total mass of a system in Solar masses, given a period and semimajor axis "a"'
    'period should be in days and a should be in AU'
    #get mass in kilograms
    mKg = ((4*math.pow(math.pi,2)*math.pow(a*AU,3))/(G*math.pow(period*Day,2)))

    #convert to solar mass
    mass = (mKg/Solar)

    return mass
    
