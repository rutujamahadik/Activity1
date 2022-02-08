n = int(input("Enter a number"))
sum = 0

for i in range(1,n+1):
    sum = sum+i
fact = 1

for i in range(1,n+1):
    fact = fact * i
print("Sum of the no is:",sum)
