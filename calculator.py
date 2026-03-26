# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b

if __name__ == "__main__":
    print("Простой калькулятор")
    print("Результат сложения 5 и 3 равен:", add(5, 3))
    print("Результат вычитания 10 - 4 =", subtract(10, 4))
    print("Результат умножения 6 * 7 =", multiply(6, 7))
    print("Результат деления 15 / 3 =", divide(15, 3))