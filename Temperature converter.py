# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Prompt the user to input a temperature value and the original unit of measurement
original_unit = input("Enter the original unit of measurement (C, F, or K): ").upper()
temperature = float(input("Enter the temperature value: "))

# Convert the temperature to the other two units and display the converted values to the user
if original_unit == "C":
    print(f"{temperature} degrees Celsius is equal to {celsius_to_fahrenheit(temperature):.2f} degrees Fahrenheit and {celsius_to_kelvin(temperature):.2f} degrees Kelvin.")
elif original_unit == "F":
    print(f"{temperature} degrees Fahrenheit is equal to {fahrenheit_to_celsius(temperature):.2f} degrees Celsius and {fahrenheit_to_kelvin(temperature):.2f} degrees Kelvin.")
elif original_unit == "K":
    print(f"{temperature} degrees Kelvin is equal to {kelvin_to_celsius(temperature):.2f} degrees Celsius and {kelvin_to_fahrenheit(temperature):.2f} degrees Fahrenheit.")
else:
    print("Invalid unit of measurement. Please enter C, F, or K.")
