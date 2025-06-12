#Unit Converter:
def unit_converter():
    conversion={
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001
    }

    print("Unit Conversion:")
    print("Avaiblale Units: km, m, cm, mm")
    value = float(input("Enter the value to convert: "))
    from_unit = input("Convert from (mm/cm/m/km): ").lower()
    to_unit = input("Convert to (mm/cm/m/km): ").lower()

    if from_unit not in conversion or to_unit not in conversion:
        print("Invalid unit")

    else:
        meters = value * conversion[from_unit]
        converted_value = meters / conversion[to_unit]

        print(f"{value} {from_unit} is {converted_value} {to_unit} ")

unit_converter()