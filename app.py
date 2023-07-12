from calculator import *

class main():
    calculator.ask(calculator)
    total = calculator.math(calculator)
    additional_adding = calculator.cont_calc(calculator)



    while additional_adding == "Y":
        calculator.num1 = total
        print(f'Last value {total}')
        calculator.ask(calculator)
        total = calculator.math(calculator)
        additional_adding = calculator.cont_calc(calculator)


    print("Program End")

