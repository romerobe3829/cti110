# This program is created to convert Celsius temperatures to Fahrenheit temperatures.
# 09/22/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter
# Eric Romero Barranco
#
# Pseudocode:
# Assign the Celsius temperature to a floating variable
# Calculate the convertion witht the formula F = 9/5 + 32
# Display the Fahrenheit Temperature. I wanted to do in format by rounding up using format(Fahrenheit, '.0f') but this was not part of the instruction.

Celsius = float(input('Enter the Temperature in Celsius to convert to Fahrenheit Temperature: '))
Fahrenheit = (9 / 5) * Celsius + 32
print ('The Fahrenheit Temperature is:', Fahrenheit)
