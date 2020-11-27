import Menus
import math
import cmath

commands = {"hypot":2, "leg":2, "qroots":3, "dist":4, "slope":4}
precision = 2


def removeAlpha(string):
    str = ""
    for char in string:
        if char.isdigit() or char=="." or char=="-":
            str += char
    return str

def handleInput(command):
    if command.strip() == "help":
        Menus.printHelp()

# print details on a function
    elif command.strip().rfind("detail")==0:
        print("detail command detected")

# set Precision
    elif command.strip().rfind("set precision")==0:
        global precision
        precision = int(input("How many decimal places should we round to? (0-16) >>"))
        print("Precision set to " + str(precision) + ".\n")


# print functions
    elif command.strip().rfind("funcs")==0:
        Menus.printFuncs(commands)

# find the hypotenuse
    elif command.strip().rfind("hypot:")==0:
        vals = command.replace("hypot:","")
        vals = vals.split(", ")

        cleanedVals = []

        if len(vals) != commands["hypot"]:
            print("Please enter a valid number of arguments.\n")
            return
        else:
            for item in vals:
                item = removeAlpha(item)
                cleanedVals.append(float(item.strip()))

            #print(cleanedVals)
            print( round( math.hypot(float(cleanedVals[0]), float(cleanedVals[1])), precision) )
            print()

#find the leg of a right triangle
    elif command.strip().rfind("leg:")==0:
        vals = command.replace("leg:", "")
        vals = vals.split(", ")

        cleanedVals = []

        if len(vals) != commands["leg"]:
            print("Please enter a valid number of arguments.\n")
            return
        else:
            for item in vals:
                item = removeAlpha(item)
                cleanedVals.append(float(item.strip()))

        print(round( math.sqrt( (max(cleanedVals))**2 - (min(cleanedVals)**2) ), precision ) )
        print()

#find the distance between two points
    elif command.strip().rfind("dist:")==0:
        vals = command.replace("dist:", "")
        vals = vals.split(", ")

        cleanedVals = []

        if len(vals) != commands["dist"]:
            print("Please enter a valid number of arguments.\n")
            return
        else:
            for item in vals:
                item = removeAlpha(item)
                cleanedVals.append(float(item.strip()))

            print( round( math.sqrt(((cleanedVals[0]-cleanedVals[2])**2) + ((cleanedVals[1]-cleanedVals[3])**2)),precision))
            print()

#find the quadratic roots of an equation given the coefficients
    elif command.strip().rfind("qroots:")==0:
        vals = command.replace("qroots:", "")
        vals = vals.split(", ")

        cleanedVals = []

        if len(vals) != commands["qroots"]:
            print("Please enter a valid number of arguments.\n")
            return
        else:
            for item in vals:
                item = removeAlpha(item)
                cleanedVals.append(float(item.strip()))

            a = cleanedVals[0]
            b = cleanedVals[1]
            c = cleanedVals[2]

            discriminant = (b**2)-4*a*c
            if discriminant >= 0:
                root_1 = round( ( (-1)*b+math.sqrt(discriminant))/(2*a) ,precision)
                root_2 = round( ( (-1)*b-math.sqrt(discriminant))/(2*a) ,precision)

                print("roots: [{}, {}]\n".format(root_1, root_2))
            else:
                root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
                root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
                print( "roots: [{}, {}]".format(root_1, root_2) )

#find the slope given two points
    elif command.strip().rfind("slope:")==0:
        vals = command.replace("slope:", "")
        vals = vals.split(", ")

        cleanedVals = []

        if len(vals) != commands["slope"]:
            print("Please enter a valid number of arguments.\n")
            return
        else:
            for item in vals:
                item = removeAlpha(item)
                cleanedVals.append(float(item.strip()))

            slope = round((cleanedVals[0]-cleanedVals[2])/(cleanedVals[1]-cleanedVals[3]),precision)
            print("The slope between({},{}) and ({},{}) is {}\n".format(cleanedVals[0],cleanedVals[1],cleanedVals[2],cleanedVals[3],slope) )

    elif command.strip().rfind("avg:")==0:
        vals = command.replace("avg:","")
        vals = vals.split(", ")
        sum = 0;
        cleanedVals = []
        for item in vals:
            item = removeAlpha(item)
            cleanedVals.append(float(item.strip()))

        for item in cleanedVals:
            sum+=item

        print(round(sum/len(cleanedVals),precision))


    else:
        print("Please enter a valid command\n")

