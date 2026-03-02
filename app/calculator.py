def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Ошибка: деление на ноль"

print("--- Простой Калькулятор ---")
try:
    num1 = float(input("Введите первое число: "))
    op = input("Выберите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    if op in operations:
        result = operations[op](num1, num2)
        print(f"Результат: {result}")
    else:
        print("Неверная операция!")
except ValueError:
    print("Ошибка: вводите только числа")