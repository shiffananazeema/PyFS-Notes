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
    

