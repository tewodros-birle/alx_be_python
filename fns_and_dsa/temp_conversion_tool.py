# Global conversion factors - defined exactly as required
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature_input():
    """Gets and validates temperature input"""
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """Gets and validates unit input"""
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit in ['C', 'F']:
            return unit
        print("Invalid unit. Please enter either C or F.")

def main():
    temperature = get_temperature_input()
    unit = get_unit_input()
    
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

if __name__ == "__main__":
    main()
