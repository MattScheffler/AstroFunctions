#AstroFunctions main page

import AstroFunctionsIndex as index

#make a main menu
def mainMenu():
    print("Enter the number of the function you want to use:")
    print("1. Blackbody distribution plot.")
    print("2. Phase plot.")
    print("Enter 'quit' to end.")

#make a switch case function that calls whatever the user wants from the index
def functionCaller(userInput):
    functions = {
        "1": index.planckCall,
        "2": index.phaseCall,
        }
    if (userInput in functions.keys()):
        return functions[userInput]()
    else:
        return

#main function to pass user input to the functionCaller that passes to the index
if __name__ == "__main__":
    #make the main loop for the program
    while (1):
        
        mainMenu()
        userInput = input("")
        if (userInput.lower() == "quit"):
            break
        else:
            try:
                functionCaller(userInput)
                print()
            except:
                #some message about choosing a proper value, or nothing and just looping again
                print()
