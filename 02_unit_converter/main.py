from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

def Con_Selection():
    option = [
        "Length",
        "Area",
        "Volume",
        "Weight",
        "Temperature",
        "Speed",
        "Exit"
    ]
    print()
    while True:    
        Selected_Converter = inquirer.select(
            message = "Select type of Converter (Space to toggle select, and Enter to confirm):- ",
            choices = option,
        ).execute()

        if Selected_Converter=="Exit":
            print("Closing Converter App")
            break

        functions = {
            "Length": Length_Con,
            "Area": Area_Con,
            "Volume": Volume_Con,
            "Weight": Weight_Con,
            "Temperature": Temperature_Con,
            "Speed": Speed_Con
        }
        functions[Selected_Converter]()

def getUserInput(options):
    print()
    options2 = list(options)
    options2.append("Exit")
    fromUnit = inquirer.select(
        message = "Pick 1st Pair of Unit:- ",
        choices = options2
    ).execute()

    if fromUnit == "Exit":
        return "Exit", None, None

    options2.remove(fromUnit)
    options2.remove("Exit")

    toUnit = inquirer.select(
        message = "Pick 2nd Pair of Unit:- ",
        choices = options2
    ).execute()

    userInput = inquirer.number(
        message = f"Enter values in {fromUnit}:- ",
        float_allowed = True,
        validate = EmptyInputValidator()
    ).execute()

    return fromUnit, toUnit, userInput

def linearConversion(fromUnit, toUnit, userInput, base, scale_mapping):
    if fromUnit == base:
        result = float(userInput) / float(scale_mapping[toUnit])
    
    elif toUnit == base:
        result = float(userInput) * float(scale_mapping[fromUnit])
    else:
        temp = float(userInput) * float(scale_mapping[fromUnit])
        result = float(temp) / float(scale_mapping[toUnit])
    
    return result

def Length_Con():
    
    options = ["Meter", "Centimeter", "Decimeter", "Millimeter", "Kilometer", "Micrometer", "Nanometer", "Picometer", "Inch", "Foot", "Yard", "Mile","Nautical Mile", "Astronomical Unit", "Light Year" ]

    scale_mapping = {  # unit to meter conversion s
        "Meter": 1, 
        "Centimeter": 0.01, 
        "Decimeter": 0.1, 
        "Millimeter": 10**-3, 
        "Kilometer": 10**3, 
        "Micrometer": 10**-6, 
        "Nanometer": 10**-9, 
        "Picometer": 10**-12, 
        "Inch": 0.0254, 
        "Foot": 0.3048, 
        "Yard": 0.9144, 
        "Mile": 1609.2634, 
        "Nautical Mile": 1851.8519, 
        "Astronomical Unit": int(1.49598e11), 
        "Light Year": int(9.4607e15)
    }
    
    while True:

        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        result = linearConversion(fromUnit, toUnit, userInput, "Meter", scale_mapping)
            
        print(f"{result:6g} {toUnit}")

def Area_Con():
    options = ["Square Meter", "Square Centimeter", "Square Decimeter", "Square Millimeter", "Square Kilometer", "Are", "Hectare", "Square Inch", "Square Foot", "Square Yard", "Square Mile" "Acre" ]

    scale_mapping = {
        "Square Meter" : 1, 
        "Square Centimeter" : 10**-4, 
        "Square Decimeter" : 10**-2, 
        "Square Millimeter" : 10**-6, 
        "Square Kilometer" : 10**6, 
        "Are" : 10**4, 
        "Hectare" : 10**2, 
        "Square Inch" : float(6.4516e-4), 
        "Square Foot" : float(9.2903e-2), 
        "Square Yard" : 0.8361, 
        "Square Mile" : int(2.59e6) ,
        "Acre" : 4046.94456
    }

    while True:
        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        result = linearConversion(fromUnit, toUnit, userInput, "Square Meter", scale_mapping)
        print(f"{result:6g} {toUnit}")

def Volume_Con():
    options = ["Cubic Meter", "Cubic Centimeter", "Cubic Decimeter", "Cubic Millimeter", "Litre", "Milliliter", "Centiliter", "Deciliter", "HectoLiter", "Cubic Inches", "Cubic Foot", "Cubic Yard", "UK Gallon", "US Gallon", "UK Fluid Ounce", "US Fluid Ounce" ]
    scale_mapping = {
        "Cubic Meter": 1, 
        "Cubic Centimeter": 10**-6, 
        "Cubic Decimeter": 10**-3, 
        "Cubic Millimeter": 10**-9, 
        "Litre": 10**-3, 
        "Milliliter": 10**-6, 
        "Centiliter": 10**-5, 
        "Deciliter": 10**-4, 
        "HectoLiter": 0.1, 
        "Cubic Inches": float(1.6387e-5), 
        "Cubic Foot": float(2.83168e-2), 
        "Cubic Yard": float(0.76455), 
        "UK Gallon": float(4.546e-3), 
        "US Gallon": float(3.7854e-3), 
        "UK Fluid Ounce": float(2.841e-5), 
        "US Fluid Ounce": float(2.927e-5)
    }

    while True:    
        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        result = linearConversion(fromUnit, toUnit, userInput, "Cubic Meter", scale_mapping)

        print(f"{result:6g} {toUnit}")

def Weight_Con():
    options = ["Kilogram", "Microgram", "Milligram", "Gram", "Carat", "Quintal", "Ton" ]

    scale_mapping = {
        "Kilogram": 1, 
        "Microgram": 10**-9, 
        "Milligram": 10**-6, 
        "Gram": 10**-3, 
        "Carat": 2e-4, 
        "Quintal": 10**2, 
        "Ton": 10**3
    }

    while True:
        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        result = linearConversion(fromUnit, toUnit, userInput, "Kilogram", scale_mapping)
        print(f"{result:6g} {toUnit}")

def Temperature_Con():

    fahrenheit_family = ["Fahrenheit", "Rankine"]
    celsius_family = ["Celsius", "Kelvin"]

    options = fahrenheit_family + celsius_family

    scale_mapping = {
        "Fahrenheit": 459.67,
        "Rankine": -459.67,
        "Celsius": 273.15,
        "Kelvin": -273.15,
    }

    while True:
        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        fahrenExchange = lambda a, b: float(a) - float(scale_mapping[b])
        celsiusExchange = lambda a, b: float(a) - float(scale_mapping[b])
        crossExchange = lambda a, b: float((a-32)/1.8) if b == "Celsius" else float((a*1.8)+32)

        if fromUnit in fahrenheit_family:
            if toUnit in fahrenheit_family:
                result = fahrenExchange(userInput, toUnit)
            else:
                temp = fahrenExchange(userInput, "Fahrenheit") if fromUnit!= "Fahrenheit" else userInput
                temp = crossExchange(float(temp), "Celsius")
                result = celsiusExchange(temp, toUnit) if toUnit != "Celsius" else temp
            
        elif fromUnit in celsius_family:
            if toUnit in celsius_family:
                result = celsiusExchange(userInput, toUnit)
            else:
                temp = celsiusExchange(userInput, "Celsius") if fromUnit!= "Celsius" else userInput
                temp = crossExchange(float(temp), "Fahrenheit")
                result = fahrenExchange(temp, toUnit) if toUnit != "Fahrenheit" else temp

        print(f"{result:6g} {toUnit}")

def Speed_Con():
    options = ["Kilometer/Hour", "Meter/Seconds", "Inches./Seconds", "Miles/Hour", "Mach", "Kilometer/Second"]

    scale_mapping = {
        "Kilometer/Hour": 1,
        "Meter/Seconds": 3.6,
        "Inches./Seconds": 9.144e-2,
        "Miles/Hour": 1.6093,
        "Mach": 1225.007316,
        "Kilometer/Second": 3600,
    }

    while True:
        fromUnit, toUnit, userInput = getUserInput(options)

        if fromUnit == "Exit":
            print("Returning to main menu...\n")
            break

        result = linearConversion(fromUnit, toUnit, userInput, "Kilometer/Hour", scale_mapping)
        print(f"{result:6g} {toUnit}")


if __name__ == "__main__":
    Con_Selection()