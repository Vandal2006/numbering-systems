# Author: Henry Gilson
# Class: cpsc-20000

# Constants
INTRODUCTION = '''
******************************************************
                    Numbering Systemn 2.0
          
                         GilsoSoft
******************************************************

This program will give you your inputed interger, as an itnput, as a number and as a hex.
If you did not input a interger you will be told you need to input an int to get the value.
It will alsom welcome you for useing it.
'''

import sys
print(INTRODUCTION)
numberOfArgs = len(sys.argv)
print("Total arguments passed: "  + str(numberOfArgs))
print("Argument 1: " + sys.argv[0])

if numberOfArgs == 2:
    print("Argument 2: " + sys.argv[1])
    try:
        numberAsAString = sys.argv[1]
        numberAsAnInt = int(numberAsAString, base=10)
        numberAsHex = hex(numberAsAnInt)
    
        print("Input: " + numberAsAString)
        print("Number: " + str(numberAsAnInt))
        print("Hex: " + numberAsHex)
        print("Your Welcome User ('.')")
    except ValueError:
     print("you did not enter an interger, to get the values you must enter an interger")
print("")