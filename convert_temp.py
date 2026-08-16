# Create a class named Solution.
# LeetCode uses this class to run our solution.
class Solution(object):

    # Create a function named convertTemperature.
    # 'self' refers to the current object of the Solution class.
    # 'celsius' is the temperature given as input.
    def convertTemperature(self, celsius):

        # Convert Celsius to Kelvin.
        # Formula:
        # Kelvin = Celsius + 273.15
        kelvin = celsius + 273.15

        # Convert Celsius to Fahrenheit.
        # Formula:
        # Fahrenheit = Celsius × 1.80 + 32.00
        fahrenheit = celsius * 1.80 + 32.00

        # Return both answers.
        # The first value is Kelvin.
        # The second value is Fahrenheit.
        return (kelvin, fahrenheit)
