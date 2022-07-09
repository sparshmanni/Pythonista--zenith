
def pattern(n):
    for i in range(0, n): 
        for j in range(0, i+2): 
            print("* ",end="")
        print("") 
        
  
s=input("TYPE 'YES' TO PRINT PATTERN AND 'NO' TO CLOSE:")
if s=="YES" or s=="yes":
    n = 5
    pattern(n)
elif s=="no"or s=="NO":
    exit()
else:
    print("INVALID ENTRY")
