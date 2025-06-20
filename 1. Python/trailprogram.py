# Ctrl+/ -> Comment/Uncomment

# # 1. Unit Converter:
# def unit_converter():
#     conversion={
#         'km': 1000,
#         'm': 1,
#         'cm': 0.01,
#         'mm': 0.001
#     }

#     print("Unit Conversion:")
#     print("Avaiblale Units: km, m, cm, mm")
#     value = float(input("Enter the value to convert: "))
#     from_unit = input("Convert from (mm/cm/m/km): ").lower()
#     to_unit = input("Convert to (mm/cm/m/km): ").lower()

#     if from_unit not in conversion or to_unit not in conversion:
#         print("Invalid unit")

#     else:
#         meters = value * conversion[from_unit]
#         converted_value = meters / conversion[to_unit]

#         print(f"{value} {from_unit} is {converted_value} {to_unit} ")

# unit_converter()

# 2. Check for keywords

# import keyword
    
# print("\nType '/' to exit the program")

# while True:

#     word = input("\nEnter the word: ")
#     if word == '/':
#         print("\nSee u soon")
#         break
#     elif keyword.iskeyword(word):
#         print(f"\n'{word}' is a keyword")
#     else:
#         print(f"\n'{word}' is not a keyword")

# 3. Calculator

# fn = float(input("Enter first number: "))
# sn = float(input("Enter second number: "))
# op = input("Enter Operator(+,-,*,/,//,%,** or all): ")
# if op == '+':
#     result = fn + sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == "-":
#     result = fn - sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == '*':
#     result = fn * sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == "/":
#     result = fn / sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == '//':
#     result = fn // sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == "%":
#     result = fn % sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == "**":
#     result = fn ** sn
#     print(f"{fn} {op} {sn} = {result}")
# elif op == "all":
#     print(f"{fn} + {sn} = {fn + sn}")
#     print(f"{fn} - {sn} = {fn - sn}")
#     print(f"{fn} * {sn} = {fn * sn}")
#     print(f"{fn} / {sn} = {fn / sn}")
#     print(f"{fn} // {sn} = {fn // sn}")
#     print(f"{fn} % {sn} = {fn % sn}")
#     print(f"{fn} ** {sn} = {fn ** sn}")
# else:
#     print("Enter valid value")
    
# 4. Fruit basket

# basket = []
# print("Options: add, remove, show, clear, exit")

# while True:
#     command = input("Enter command: ")
#     if command == 'exit':
#         print("\nThanks for using the basket!\n")
#         break
#     elif command == 'add':
#         f_add = input("Enter fruit name: ").lower()
#         if f_add in basket:
#             print(f"'{f_add}' is already in the basket")
#         else:
#             basket.append(f_add)
#             print(f"'{f_add}' is added.")
#     elif command == 'show':
#         print(f"Current basket: {basket}")
#     elif command == 'remove':
#         f_remove = input("Enter fruit name: ").lower()
#         if f_remove in basket:
#             basket.remove(f_remove)
#             print(f"'{f_remove}' is removed from the basket.")
#         else:
#             print(f"'{f_remove}' is not in the basket.")
#     elif command == 'clear':
#         basket.clear()
#         print("The basket is empty")
#     else:
#         print("Enter valid command")

# 5. 5 Fruit

# fruits = []

# for i in range(5):
#     fruit = input(f"Enter fruit {i+1}: ").lower()
#     fruits.append(fruit)

# for fruit in fruits:
#     if fruits.count(fruit) > 1:
#         print(f"\n{fruit} is repeated!.\n")
#         break
# else:
#     print("\nAll fruits are unique.\n")

# 6. Missing number

# length = int(input("Enter the length: "))
# values = []

# for i in range(length):
#     value=int(input(f"Enter value {i+1}: "))
#     values.append(value)

# n = len(values) + 1
# expected = n * (n + 1) // 2
# actual= sum(values)

# missing = expected - actual

# print(f"Missing number is {missing}")

# 7. Largest number

# values = [int(i) for i in input("Enter values: ").split()]
# unique = list(set(values))
# unique.sort(reverse=True)
# print(unique[1])

# values = [int(i) for i in input("Enter values: ").split()]

# first = second = float('-inf')  # set to very low

# for num in values:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num

# print("Second largest:", second)

# 8. frequent number in list

# from collections import Counter

# values = [int(i) for i in input("Enter value: ").split()]
# counts = Counter(values)

# num , c = counts.most_common(1)[0]

# print(f"{num} is repeated {c} times")

# for num, c in counts.items():
#     if c > 1:
#         print(f"{num} is repeated {c} times")

# values = [int(i) for i in input("Enter value: ").split()]

# frequency = {}

# for i in values:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# max_count = 0
# most_frequent = None

# for key, value in frequency.items():
#     if value > max_count:
#         max_count = value
#         most_frequent = key
# print(f"{most_frequent} is repeated {max_count} times")

n = int(input())
for i in range (0,n+1):
    print("*" * i)