

def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return 1


arr = ['t','u','t','o','r','i','a','l']
print( "INDEX IS =('t','u','c','o','r','i','a','l')")
x =input("enter the element :")
print("element found at index "+str(linearsearch(arr,x)))



ans=input("DO YOU WANT TO RUN AGAIN ?? (y/n)")
while ans=="y" or ans=="Y":
    x =input("enter the element :")
    print("element found at index "+str(linearsearch(arr,x)))
    
