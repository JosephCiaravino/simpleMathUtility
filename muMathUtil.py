

import Menus
import InputHandler


def main():
    Menus.printMu()
    quit = False
    issuedCommands = []
    while quit==False:
        command = input("Enter command >>").lower()
        if command == "q":
            print("Good bye!")
            quit=True
        elif command == "hist":
            if len(issuedCommands)>0:
                for cmd in issuedCommands:
                    print("- ",cmd)
            else:
                print("No history to show")

        else:
            issuedCommands.append(command)
            InputHandler.handleInput(command)

        if len(issuedCommands)>=20:
            issuedCommands.pop(0)

if __name__=="__main__": main()