

## function to return weather the number in positive,negetive or zero
def checkNumber(given_Num):
    # checking if the given number is positive number
    if(given_Num > 0):
        print("The given number", given_Num, "is positive")
    # checking if the given number is negative number
    elif(given_Num < 0):
        print("The given number", given_Num, "is negative")
    # if the above conditions are not satisfied then the given number is zero
    else:
        print("The given number", given_Num, "is zero")

# given numbers
# given number 1
given_num1 = 169
# passing the given number to checkNumber Function which prints the type of number(+ve,-ve,0)
checkNumber(given_num1)
# given number 2
given_num1 = -374
# passing the given number to checkNumber Function which prints the type of number(+ve,-ve,0)
checkNumber(given_num1)
# given number 3
given_num1 = 0
# passing the given number to checkNumber Function which prints the type of number(+ve,-ve,0)
checkNumber(given_num1)
