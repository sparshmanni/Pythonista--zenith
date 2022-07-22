

# Python Program to Check if a Number is Odd or Even
# Function which prints whether the given number
# is even number ,odd number

def checkNumber(given_Num):
    # checking if the given number is even number
    if(given_Num % 2 == 0):
        print("The given number", given_Num, "is even number")
    # checking if the given number is odd number that is if given number is not even then it is odd number
    else:
        print("The given number", given_Num, "is odd number")


# given numbers
# given number 1
given_num1 = 169
# passing the given number to checkNumber Function which
# prints the type of number(even number or odd number)
checkNumber(given_num1)
# given number 2
given_num1 = 26
# passing the given number to checkNumber Function which
# prints the type of number(even number or odd number)
checkNumber(given_num1)
