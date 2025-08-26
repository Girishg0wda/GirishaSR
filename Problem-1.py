num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
operator = input("Enter the operator (+,-,*,/): ")

class Calculator:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def calculate(self):
        if self.operator == '+':
            return self.a + self.b
        elif self.operator == '-':
            return self.a - self.b
        elif self.operator == '*':
            return self.a * self.b
        elif self.operator == '/':
            if self.b == 0:
                return "Number cannot be divided by 0"
            else:
                return self.a / self.b
        else:
            return "Invalid Operator"

calc = Calculator(num1, num2, operator)
print("Result:", calc.calculate())
