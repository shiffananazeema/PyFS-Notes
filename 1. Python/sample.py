n = int(input("Enter a total number: "))
A = []  # list to store numbers

for i in range(n):
    num = int(input("Enter the number: "))
    A.append(num)

p = 1  # initialize product
for num in A:
    p *= num

print("The product is:", p)
