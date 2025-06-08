# Global conversion factors - must be exactly these names
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    # Get temperature input
    temp_input = input("Enter the temperature to convert: ")
    
    # Validate numeric input - must use ValueError exactly
    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    # Get unit input - must be exactly C/F
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    # Perform conversion - must match output format exactly
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter either C or F.")

if __name__ == "__main__":
    main()
