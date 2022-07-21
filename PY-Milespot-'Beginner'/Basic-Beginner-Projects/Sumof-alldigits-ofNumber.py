# Python program to find the 
# sum of all digits of a number

# function definition
def sumDigits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sumDigits(int(num / 10))

# main code
x = 0
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()

x = 12345
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()

x = 5678379
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()
