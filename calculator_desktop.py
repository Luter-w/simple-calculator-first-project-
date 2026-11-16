import sys
from PyQt6.QtWidgets import(
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.resize(340, 420)

        self.num1_input = QLineEdit()
        self.num1_input.setPlaceholderText("Первое число")

        self.num2_input = QLineEdit()
        self.num2_input.setPlaceholderText("Второе число")

        row1 = QHBoxLayout()
        for op in ("+", "-", "*", "/"):
            btn = QPushButton(op)
            btn.clicked.connect(lambda checked, symbol=op: self.calculate(symbol))
            row1.addWidget(btn)

        row2 = QHBoxLayout()
        for op in ("//", "%", "^", "sqrt"):
            btn = QPushButton(op)
            btn.clicked.connect(lambda checked, symbol=op: self.calculate(symbol))
            row2.addWidget(btn)


        self.result_label = QLabel("Результат")

        layout = QVBoxLayout()
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_input)
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
        except ValueError:
            self.result_label.setText("Ошибка: введите числа!")
            return

        first_number = num1
        second_number = num2
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
        self.result_label.setText(f"Результат: {res}")

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = Calculator()
    window.show()
    sys.exit(app.exec())