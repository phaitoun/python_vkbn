def kaprekarRec(n, prev):
 
    if (n == 0):
        return 0
    prev = n
    digits = [0] * 4
    for i in range(4):
        digits[i] = n % 10
        n = int(n / 10)
    digits.sort()
    asc = 0
    for i in range(4):
        asc = asc * 10 + digits[i]
    digits.sort()
    desc = 0
    for i in range(3, -1, -1):
        desc = desc * 10 + digits[i]
    diff = abs(asc - desc)
    print(desc,"-",asc,"=",diff)
    if (diff == prev):
        return diff
    return kaprekarRec(diff, prev)
def kaprekar(n):
 
    rev = 0
    return kaprekarRec(n, rev)



n =int(input("Enter number: "))
print(kaprekar(n))