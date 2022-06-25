# Creating a Dictionary
Dict = {'Name': 'Sparsh', 'Roll': 21}

print("Our Dictionary ->",Dict)
  
# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['Name']) 
  
# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get('Roll')) 
  
# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
