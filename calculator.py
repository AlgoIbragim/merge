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
    print(f"Сложение 5 + 3 = {add(5, 3)}")
    print(f"Вычитание 10 - 4 = {subtract(10, 4)}")
    print(f"Умножение 6 * 7 = {multiply(6, 7)}")
    print(f"Деление 15 / 3 = {divide(15, 3)}")