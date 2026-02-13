class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
calc = Calculator()
print(calc.add(2, 3))  # This will raise an error because the first add method is overridden by the second one. 
print(calc.add(2, 3, 4))  # This will work and return 9.    