

def printTopSeparator():
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def printBottomSeparator():
    print("-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def printMu():
    printTopSeparator()
    print("\nMMMM          MMMM")
    print("MMMM          MMMM                 Welcome To Mu")
    print("MMMM          MMMM          Your new favorite math utility!")
    print("MMMM          MMMM                -=-=-=-=-=-=-=-")
    print("MMMMM        MMMMM          Enter 'help' for the help menu")
    print("MMMMMMM   MMMMMMMM")
    print("MMM  MMMMMM  MMMMM    M")
    print("MM    MMMM     MMM  MM  ")
    print("MM              MMMM")
    print("MM")
    print("MM")
    printBottomSeparator()

def printHelp():
    printTopSeparator()
    print("help menu".upper())
    print("\tTo see available functions enter 'funcs'")
    print("\tTo quit the program enter 'q'")
    print("\tTo retrieve details on a function type 'detail' followed by the function name")
    print("\tTo veiw recent commands enter 'hist'")
    print("\tTo set precision enter 'set precision' and follow the prompt")
    printBottomSeparator()

def printDetails(func):
    print("This will be logic that explains functions and notation")

def printFuncs(dict):
    printTopSeparator()
    print("functions menu".upper())
    for k, v in dict.items():

        instruction = "\tThe {} argument takes {} values in the form \n\t\t< {}: ".format(k.upper(),int(v),k, )
        for i in range(v+1):
            if i == 0:
                continue
            elif i<v:
                instruction += str(i)+", "
            else:
                instruction += str(i)+" > followed by [ENTER]."

        print( instruction  )
    print( "\t The avg function takes as many values as you enter.")
    print("\t\t <avg: 1, 2, 3, 4, 5... ,n> followed by [ENTER]")
    printBottomSeparator()