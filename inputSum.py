# input_string = input("Enter a list element separated by space ")
# list  = input_string.split()
# print("Calculating sum of element of input list")
# sum = 0
# for num in list:
#     sum += int (num)
# print("Sum = ",sum)

num = int(input("Enter number "))
result = 0 
for i in range(len(str(num))):
    degit = num % 10 
    num = num //10
    result +=  degit #result = result +degit
print(result)
