import math

class SimpleCalculator:

    def add(self, a, b):
        """Сложение"""
        return a + b

    def subtract(self, a, b):
        """Вычитание"""
        return a - b

    def multiply(self, a, b):
        """Умножение"""
        return a * b

    def divide(self, a, b):
        """Деление с проверкой деления на ноль"""
        if b == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")  # заменим текст ошибки
        return a / b

    def power(self, base, exponent):
        """Возведение в степень"""
        return base**exponent

    def sqrt(self, a):
        """Квадратный корень"""
        if a < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа!")
        return math.sqrt(a)

    def factorial(self, n):
        """Факториал числа"""
        n_val = int(n) if n.is_integer() else n
        if not isinstance(n_val, int) or n_val < 0:
            raise ValueError("Факториал определен только для целых неотрицательных чисел!")
        return math.factorial(n_val)

    def is_prime(self, n):
        """Проверка на простое число"""
        n_val = int(n) if n.is_integer() else n
        if not isinstance(n_val, int) or n_val <= 1:
            return False
        for i in range(2, int(math.sqrt(n_val)) + 1):
            if n_val % i == 0:
                return False
        return True

    def percentage(self, part, whole):
        """Процент от числа: сколько процентов part составляет от whole"""
        if whole == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю!")
        return (part / whole) * 100


# Консольный интерфейс
if __name__ == "__main__":
    calc = SimpleCalculator()
    print("=== Простой консольный калькулятор ===")
    print("Доступные операции: add, sub, mul, div, pow, sqrt, fact, prime, percent")

    while True:
        cmd = input(
            "\nВведите операцию (или 'exit' для выхода): "
        ).strip().lower()
        if cmd == "exit":
            print("Пока!")
            break

        try:
            if cmd in ["add", "sub", "mul", "div", "pow", "percent"]:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))

                if cmd == "add":
                    print(f"Результат: {calc.add(a, b)}")
                elif cmd == "sub":
                    print(f"Результат: {calc.subtract(a, b)}")
                elif cmd == "mul":
                    print(f"Результат: {calc.multiply(a, b)}")
                elif cmd == "div":
                    print(f"Результат: {calc.divide(a, b)}")
                elif cmd == "pow":
                    print(f"Результат: {calc.power(a, b)}")
                elif cmd == "percent":
                    print(f"Результат: {calc.percentage(a, b)}%")

            elif cmd in ["sqrt", "fact", "prime"]:
                n = float(input("Введите число: "))

                if cmd == "sqrt":
                    print(f"Результат: {calc.sqrt(n)}")
                elif cmd == "fact":
                    print(f"Результат: {calc.factorial(n)}")
                elif cmd == "prime":
                    print(f"Результат: {calc.is_prime(n)}")
            else:
                print("Неизвестная операция, попробуй снова.")
        except Exception as e:
            print(f"Ошибка: {e}")