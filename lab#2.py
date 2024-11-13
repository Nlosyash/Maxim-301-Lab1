def task_if1():
    """If 13. Дано три числа. Знайти середнє з них (тобто число, розташоване між найменшим і найбільшим).
    try:
        # Введення трьох чисел
        a, b, c = map(int, input("Введіть три числа через пробіл: ").split())
        # Логіка для знаходження середнього числа
        numbers = [a, b, c]
        numbers.sort()  # Сортуємо числа
        middle = numbers[1]  # Середнє число - це друге в відсортованому списку

        print("Середнє число: ", middle)
    except ValueError:
        print("INTEGER expected!")  # Помилка, якщо введено некоректні значення
# Виклик функції
task_if1()


def count_points_in_area(points, r):
    """
    Рахує кількість точок, що потрапляють в помаранчеву область.
    :param points: список координат точок [(x1, y1), (x2, y2), ...]
    :param r: радіус (межа по x)
    :return: кількість точок в області
    """
    count = 0
    for x, y in points:
        # Перевірка умов для помаранчевої області
        if 0 < x <= r and y < 0 and y >= -x:
            count += 1
    return count
# Приклад використання
points = [(1, -1), (2, -2), (3, -1), (-1, -1), (1, 1)]
r = 3  # Наприклад, радіус r
result = count_points_in_area(points, r)
print(f"Кількість точок у помаранчевій області: {result}")


import math

def compute_series(epsilon=1e-10):
    """
    Обчислює нескінченний ряд:
    S = Σ (2^n * (2n-1)!) / √(n!) до збіжності з точністю epsilon.
    :param epsilon: точність обчислення
    :return: значення суми ряду
    """
    # Початкові значення
    s = 0  # Сума
    n = 1  # Перший індекс
    term = 2 / math.sqrt(1)  # Початковий член ряду (для n=1)
    while abs(term) > epsilon:
        s += term  # Додаємо поточний член до суми
        # Рекурсивно обчислюємо наступний член ряду
        term *= (2 * (2 * n) * (2 * n - 1)) / ((n + 1) * math.sqrt(n + 1))

        # Переходимо до наступного індексу
        n += 1
        # Перевірка на занадто довге виконання
        if n > 10000:
            print("Досягнуто ліміту ітерацій.")
            break
    return s
# Використання функції
result = compute_series()
print(f"Значення ряду: {result}")

# script-file
import math

def task_if1():
    """
    Задача: визначити кількість точок, які потрапляють в область заданого кольору (варіант 18).
    """
    # Координати точок (xi, yi), можна змінювати
    points = [
        (1, 1),
        (2, -2),
        (-1, 3),
        (0.5, 0.5),
        (-1.5, -1.5),
        (0, -1),
    ]
    # Радіус кола (завдання використовує змінну "r")
    r = 2
    # Геометрична область: коло нижньої половини координатної системи
    def is_in_region(x, y):
        """
        Перевірка, чи потрапляє точка в область.
        Для варіанта 18 це нижня половина жовтої області.
        """
        return x**2 + y**2 <= r**2 and y < 0

    # Підрахунок точок, що потрапляють у задану область
    count = sum(1 for x, y in points if is_in_region(x, y))
    print(f"Кількість точок у жовтій області (варіант 18): {count}")

# Основний цикл
choice = int(input("Please, choose the task 1-3 (0-EXIT): "))
while choice:
    if choice == 1:
        task_if1()

    elif choice == 3:
        # Цей блок можна використовувати для інших завдань
        print("Task 3 placeholder")

    else:
        print("Wrong task number!")

    choice = int(input("Please, choose the task again (0-EXIT): "))

print("Good bye!")
