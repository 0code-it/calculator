#python
import os
os.system("clear")

print("\033[1;32;40m CALCULATOR PROGRAM MADE BY Code._it \n")
print("\033[1;33;40m THIS TOOL WILL HELP IN SOLVING BASIC MATHEMATICAL OPERATIONS FOR EDUCATIONAL PURPOSES\n")

print("""  


               
                       🄲🄾🄳🄴._🄸🅃
                       
                       
                       
             ==================Beta Version 2.0==============""")

print("\033[96m  :::::::::::::: CALCULATOR IS NOW WORKING.:::::::::::::\n")
print("\033[95m Follow Me On Github: https://github.com/0code-it/ ") 
print(" Follow Me On Facebook: https://m.facebook.com/qvaibhav/?ref=bookmarks ")
print("\033[1;37;40m  Follow me on Instagram: https://www.instagram.com/code._it/")

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
Type + for addition
Type - for subtraction
Type * for multiplication
Type / for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("\033[1;31;40m You Have Not Typed A Valid Operator, Please Again Run The Program\n.")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print("\033[2;37;40m THANKS FOR USING THIS CALCULATOR SEE YOU LATER, FOLLOW ME ON INSTAGRAM: @code._it \n")
    else:
        again()

calculate()
