class Temperature:

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


t = Temperature()

print("Celsius to Fahrenheit:", t.celsius_to_fahrenheit(25))
print("Fahrenheit to Celsius:", t.fahrenheit_to_celsius(77))