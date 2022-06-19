#creating text file
file = open("test.txt", "x")


#Writing to file
file = open("test.txt", "w")
file.write("Welcome to PythonPlanet")
file.close()


#Reading a file
file = open('test.txt', 'r')
text = file.read()
print(text)
file.close()

            
