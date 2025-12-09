"""
Небольшой модуль с утилитами:
- factorial: вычисление факториала числа
- convert_rub_to_currency: конвертация рублей в другую валюту
- average_grade: расчёт средней оценки
- простое консольное меню для демонстрации
"""

from typing import List


def factorial(n: int) -> int:
    """
    Вычисляет факториал целого неотрицательного числа n.
    0! = 1, 1! = 1, 2! = 2, ...

    :param n: целое неотрицательное число
    :return: факториал n
    :raises ValueError: если n < 0
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def convert_rub_to_currency(amount_rub: float, currency: str) -> float:
    """
    Конвертирует сумму в рублях в указанную валюту по фиксированному курсу.

    Курсы условные, для демонстрации:
    - USD: 1 USD = 90 RUB
    - EUR: 1 EUR = 100 RUB

    :param amount_rub: сумма в рублях
    :param currency: строка 'USD' или 'EUR'
    :return: сумма в целевой валюте
    :raises ValueError: если валюта не поддерживается или сумма отрицательная
    """
    if amount_rub < 0:
        raise ValueError("Сумма не может быть отрицательной")

    rates = {
        "USD": 90.0,
        "EUR": 100.0,
    }

    currency = currency.upper()
    if currency not in rates:
        raise ValueError(f"Валюта {currency} не поддерживается")

    return amount_rub / rates[currency]


def average_grade(grades: List[float]) -> float:
    """
    Считает средний балл по списку оценок.

    :param grades: список чисел (оценок)
    :return: среднее значение
    :raises ValueError: если список пуст
    """
    if not grades:
        raise ValueError("Список оценок не может быть пустым")

    return sum(grades) / len(grades)


def main() -> None:
    """
    Простое консольное меню для демонстрации работы функций.
    Не используется в тестах напрямую, но показывает, как модуль может работать как приложение.
    """
    print("Демонстрационное приложение утилит")
    print("1) Факториал числа")
    print("2) Конвертация рублей в валюту")
    print("3) Средняя оценка")
    print("0) Выход")

    choice = input("Выберите действие: ").strip()

    if choice == "1":
        value = int(input("Введите целое неотрицательное число: "))
        print(f"Факториал {value} = {factorial(value)}")

    elif choice == "2":
        amount = float(input("Введите сумму в рублях: "))
        currency = input("Введите валюту (USD/EUR): ")
        converted = convert_rub_to_currency(amount, currency)
        print(f"{amount} RUB = {converted:.2f} {currency.upper()}")

    elif choice == "3":
        raw = input("Введите оценки через пробел: ")
        grades = [float(x) for x in raw.split()]
        avg = average_grade(grades)
        print(f"Средняя оценка: {avg:.2f}")

    elif choice == "0":
        print("Выход из программы.")
    else:
        print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
