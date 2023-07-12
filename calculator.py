import operator

class calculator:
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod,
           '^': operator.xor, }

    num1 = "C"
    num2 = "C"

    def __init__(self, math_type = "+"):

        self.math_type = math_type


    def math(self):
        result = calculator.ops[self.math_type](self.num1, self.num2)
        calculator.num1 = result
        print(result)
        return result


    def ask(self):
        if self.num1 == "C":
            self.num1 = int(input("Whats the first number? "))
            self.num2 = int(input("Whats the second number? "))
            self.math_type = input("What are we doing? ")
        else:
            self.num2 = int(input("Whats the second number? "))
            self.math_type = input("What are we doing? ")


    def cont_calc(self):
        additional_adding = input("Continue? ")
        return additional_adding







