first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Выберите доступную операцию: [+, -, *, /]: ")
operation = operation.strip()
if operation in ('+', '-', '*', '/'):
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
    print(res)
else:
    print("Неверная форма ввода!")