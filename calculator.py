def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Ошибка: нужно ввести именно число!")
    return number

while True:
    first_number = get_number("Введите первое число: ")
    second_number = get_number("Введите второе число (степень для sqrt,^): ")
    operation = input("Выберите доступную операцию: [+, -, *, /, //, %, ^, sqrt]: ")
    operation = operation.strip()
    if operation in ('+', '-', '*', '/', '//', '%', '^', 'sqrt'):
        if operation == '+':
            res = first_number + second_number
        elif operation == "-":
            res = first_number - second_number
        elif operation == "*":
            res = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                print("На ноль делить нельзя!")
                res = "Попробуйте снова"
            else:
                res = first_number / second_number
        elif operation == "//":
            if second_number == 0:
                print("На ноль делить нельзя!")
                res = "Попробуйте снова"
            else:
                res = first_number // second_number
        elif operation == "%":
            if second_number == 0:
                res = "Нельзя делить на ноль!"
            else:
                res = first_number % second_number
        elif operation == "^":
            try:
                if first_number == 0 and second_number < 0:
                    res = "Нельзя возвести ноль в отрицательную степень"
                else:
                    res = first_number**second_number
            except OverflowError:
                res = "Слишком большое число для типа float"
        elif operation == "sqrt":
            try:
                if second_number == 0:
                    res = "Нельзя возвести в нулевую степень корня"
                elif first_number < 0:
                    res = "Нельзя извлечь корень отрицательного числа"
                else: 
                    res = first_number**(1/second_number)
            except OverflowError:
                res = "Слишком большое число для типа float"
        print(res)
    else:
        print("Неверная форма ввода!")
    choice = input("Нажмите Enter, чтобы продолжить, или введите 'Exit' для выхода: ")
    if choice.strip().lower() == "exit":
        break