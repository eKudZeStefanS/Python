def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def ymnogenie(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Ошибка: деление на ноль")
        return None
    else:
        return a / b


def quit():
    return 0
def main():
    while True:
        print("Введите +, -, *, / для соответствующей операции")
        print("Введите 0 для выхода из программы")
        operation = input("Операция: ")
        if operation == '0':
            break

        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Неизвестная операция")
            continue

        if result is not None:
            print("Результат: ", result)
        else:
            continue

    quit()


main()