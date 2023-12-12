# written by: justin balbuena
# file name: conversion_calvulator.py
#description: this file converts numbers
#from binary to decimal and decimal to binary
#the code verifies that the user has given
#a valid binary or decimal input.
#code begins below
###############################################################################

#needed for clear_screen function
from os import system, name
def get_digits():
# used for number conversion
    num_dict = {
            "0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
            "6":6, "7":7, "8":8, "9":9, "A":10,"B":11,
            "C":12,"D":13,"E":14,"F":15
    }
    return num_dict
def get_menu():
# used as the primary display menu
    menu_dict = {
     '1':'decimal_to_binary',
     '2':'binary_to_decimal',
     'x':'exit_program'
     }
    return menu_dict
#########################################
def display_menu():
    menu_dict = get_menu()
    for items, values in menu_dict.items():
        print(items+". "+ values.capitalize())
    menu_selection = input("enter selection")

    return menu_selection
#################################################
def get_user_selection(ans) :
    menu_list = list(get_menu())
    if ans in menu_list:
        return ans
    else:
        print("try again")
        return False
######################################################
def check_user_selection(items, dict):
# if user sends a blank entry
    if len(items) < 1:
        input("missing number. Try again!")
        return True
# obtain dictionary keys and place in list
    display_list = list(dict)
#loop through each key in list
    for item in items:
# check if selection in key
       if item in display_list:
           continue
       else:
           input("invalid selection!")
           return True
# if it gets to return item that means the number is good
    return items
##########################################################
def execute_selection(menu_selection):
# after the input is put  in the menu selection will be
#executed back to the lens input
#if menu selection is true then the use has given us a blank
# entry. we want to ignore blank entries and continue
    if menu_selection is True:
        return menu_selection, None
# this function assumes that error checking occurs elsewhere
    selection = get_menu()[menu_selection]
    return eval(selection+"()")
##################################################################
def exit_program():
    print("adios_amigo!")
    return False, None
#######################################
def decimal_to_binary():
    return True, "Binary number"
######################################
def binary_to_decimal():
    return True, "Decimal number"
###############################################
def binary_to_decimal():
# The function will convert binary to decimal depending on the users
#answer it converts their binary number to decimal
    convert_from = 2
    valid_numbers = list(get_digits())[0:convert_from]
    print("Binary Digits:", valid_numbers)
    num = input("Enter a binary number: ")
    num = check_user_selection(num, valid_numbers)
    results = convert_to_decimal(num, convert_from)
    return results, "Decimal number"
###############################################################
def convert_to_decimal(ans, conversion_number):
# if the answer is true it converts their number to decimal
# Exit the program if user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
        return ans
    else:
        result = 0
        if ans is True:
            return ans
        if len(ans) > 0:
# determine greatest power
            power = len(str(ans)) - 1
# start from the largest number and move to the right
            for num in str(ans):
                calc_num = get_digits()[num]
                result += calc_num * conversion_number ** power
                power -= 1      # decrease by 1

            return result
############################################################################
def decimal_to_binary():
#This line of code correctly takes the decimal number and converts it to binary
#depending on the users answer it correctly converts the number
    convert_from = 10
    convert_to = 2
    valid_numbers = list(get_digits())[0:convert_from]
    print("Decimal Digits:", valid_numbers)
    num = input("Enter a decimal number: ")
    num = check_user_selection(num, valid_numbers)
    result = convert_from_decimal(num, convert_to)
    return result, "Binary number"
############################################################################
def convert_from_decimal(ans, conversion_number):
# Exit the program if user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
        return(ans)
    else:
        result = ""
        if ans is True:
            return ans
        int_ans = int(ans)
        while int_ans > 0:
            remainder = int_ans % conversion_number
            int_ans = int_ans // conversion_number
            result = (list(get_digits().items())[remainder])[0] + result
        return(result)
############################################################################
def display_selection(display, conversion_type):
    if display is False:

        return display

    elif conversion_type is None:
        return True
    else:
        if display is not True:
            input(conversion_type+': '+str(display))
    return True
    ####################################################################
def main():
    menu_selection = True
    while menu_selection :
        clear_screen()
        menu_selection = display_menu()
        menu_selection = check_user_selection(menu_selection, get_menu())
        menu_selection, conversion_type = execute_selection(menu_selection)
        menu_selection = display_selection(menu_selection, conversion_type)
################################################################################################
def clear_screen():
     if name == 'nt':
         _= system('cls')
     else:
         _ = system('clear')

if __name__ == '__main__':
    main()
