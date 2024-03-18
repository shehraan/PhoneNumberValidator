#Input - Takes in the user's phone number

import random

#Area code checker - Checks if user entered a valid area code
def area(number):
    for characters in areaCodes:
        if (number[:3] in areaCodes)==True:
            return True
        else:
            return False

#Symbolchecker - checks for symbols in an input
def symbol(word):
    for characters in word:
        if (characters in symbols)==True:
            return True
    return False

#Numberchecker - checks for numbers in an input
def number(word):
    for characters in word:
        if (characters in numbers)==True:
            return True
    return False

areaCodes = ["343", "519", "705", "226", "437", "548", "647", "905", "289", "365", "416", "742", "249", "613", "683", "753", "807"]
symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"," ","-","."]
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]
redo = "y"

while True:
    areaCodeWrong = 0
    phoneNumberWrong = 0
    correct="y"
    areaCode = input("Please enter your area code without hyphens: ")
    
    #Process - Validates the phone number inputted by the user
    while (symbol(areaCode)==True or any(i.isalpha() for i in areaCode)==True or number(areaCode)==True) and areaCodeWrong!=3:
        if symbol(areaCode)==True and areaCodeWrong!=3:
            areaCodeWrong=areaCodeWrong+1
            if areaCodeWrong!=3:
                print("Error, you entered a symbol which is an invalid input. Please only enter numbers.")
                areaCode = input("Please enter your area code without hyphens: ")
        elif any(i.isalpha() for i in areaCode)==True and areaCodeWrong!=3:
            areaCodeWrong=areaCodeWrong+1
            if areaCodeWrong!=3:
                print("Error, you entered a letter which is an invalid input. Please only enter numbers.")
                areaCode = input("Please enter your area code without hyphens: ")
        elif number(areaCode)==True and areaCodeWrong!=3:
            if len(areaCode)!=3:
                areaCodeWrong=areaCodeWrong+1
                if areaCodeWrong!=3:
                    print("Error, a valid area code only has 3 digits. Please enter a 3-digit area code.")
                    areaCode = input("Please enter your area code without hyphens: ")
            elif area(areaCode)!=True and areaCodeWrong!=3:
                areaCodeWrong=areaCodeWrong+1
                if areaCodeWrong!=3:
                    print("Please enter an area code that is valid in Ontario, Canada")
                    areaCode = input("Please enter your area code without hyphens: ")
            else:
                break
    if areaCodeWrong==3:
        print("\nError, you have entered the area code wrong, 3 times. The program will now generate an area code for you.")
        randomIndex = random.randint(0,16)
        areaCode = areaCodes[randomIndex]
        print("Your area code is now: "+str(areaCode))
        
    digit = input("\nPlease enter the rest of your phone number without hyphens: ")
    while (symbol(digit)==True or any(i.isalpha() for i in digit)==True or number(digit)==True) and phoneNumberWrong != 3:
        if symbol(digit)==True:
            phoneNumberWrong = phoneNumberWrong + 1
            if phoneNumberWrong != 3:
                print("Error, you entered a symbol which is an invalid input. Please only enter numbers.")
                digit = input("Please enter the rest of your phone number without hyphens: ")
            phoneNumberWrong = phoneNumberWrong + 1
        elif any(i.isalpha() for i in digit)==True:
            phoneNumberWrong = phoneNumberWrong + 1
            if phoneNumberWrong != 3:
                print("Error, you entered a letter which is an invalid input. Please only enter numbers.")
                digit = input("Please enter the rest of your phone number without hyphens: ")
        elif number(digit)==True:
            if len(digit)!=7:
                phoneNumberWrong = phoneNumberWrong + 1
                if phoneNumberWrong != 3:
                    print("Error, a valid phone number only has 7 digits after the area code. Please only enter the 7 digits")
                    digit = input("Please enter the rest of your phone number without hyphens: ")
            elif phoneNumberWrong != 3 or areaCodeWrong !=3:
                print("\nThe number was entered is: "+str(areaCode)+"-"+str(digit))
                correct = input("Is this the correct phone number?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                while correct!="y" and correct!="n":
                    print("\nError, please enter one of the given options\n")
                    print("The number was entered is: "+str(areaCode)+"-"+str(digit))
                    correct = input("Is this the correct phone number?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                if correct=="n":
                    print("\nPlease try again\n")
                    break
                else:
                    break
    if phoneNumberWrong == 3:
        print("\nError, you have entered your phone number wrong, 3 times. The program will now generate the rest of your phone number for you.")
        digit = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        print("Your phone number after the area code is now: "+str(digit))
        
        
    #Output - Lets the user know if their phone number is valid.
    if (phoneNumberWrong!=3 or areaCode!=3) and correct!="n": 
        if phoneNumberWrong == 3:
            print("\nYour full phone number is: "+str(areaCode)+"-"+str(digit))
        print("\nCongratulations, your phone number is valid!")
    
        redo = (input("\nIf you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
        while redo!="y" and redo!="n":
            print("\nError, please enter one of the given options")
            redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
        if redo=="n":
            break
        else:
            print("\nRestarting program\n")
            
    
