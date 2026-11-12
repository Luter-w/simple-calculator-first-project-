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
    second_number = get_number("Введите второе число: ")
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
    choice = input("Нажмите Enter, чтобы продолжить, или введите 'Exit' для выхода: ")
    if choice.strip().lower() == "exit":
        break