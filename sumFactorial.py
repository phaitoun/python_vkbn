num = int (input("enter factorial : !"))
fact = 1
for i in range(1,num+1):
    fact *= i 
    
print(fact)

result = 0
for n in range(len(str(fact))):
    fact = fact//10
    digit = fact % 10 
    result = result + digit
    
print("sum digit of fact is :",result)