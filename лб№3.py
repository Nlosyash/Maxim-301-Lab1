#Для 1 завдання#
def RootCount(A, B, C):
    """
    Функція для визначення кількості коренів квадратного рівняння A * x^2 + B * x + C = 0
    Параметри:
    A, B, C - коефіцієнти рівняння (A ≠ 0)
    Повертає:
    Кількість коренів рівняння (0, 1, або 2)
    """
    if A == 0:
        raise ValueError("Коефіцієнт A не може дорівнювати 0")
    D = B**2 - 4 * A * C  # Дискримінант
    if D > 0:
        return 2  # Два корені
    elif D == 0:
        return 1  # Один корінь
    else:
        return 0  # Немає коренів
def ProcessEquations(equations):
    """
    Функція для обробки списку квадратних рівнянь.
    Параметри:
    equations - список кортежів, де кожний кортеж містить коефіцієнти (A, B, C)
    Повертає:
    Список з кількістю коренів для кожного рівняння
    """
    results = []
    for A, B, C in equations:
        count = RootCount(A, B, C)
        results.append(count)
    return results
def MainFunction():
    """
    Головна функція для введення даних, виклику функцій та виведення результатів
    """
    # Введення даних
    equations = [
        (1, -3, 2),  # D > 0
        (1, -2, 1),  # D == 0
        (1, 0, -1),  # D > 0
        (1, 2, 5)    # D < 0
    ]  # Приклад даних: список рівнянь у форматі (A, B, C)
    # Виклик функції для обробки списку рівнянь
    results = ProcessEquations(equations)
    # Виведення результатів
    print("\nРезультати:")
    for i, count in enumerate(results):
        print(f"Рівняння {i+1} ({equations[i][0]}x^2 + {equations[i][1]}x + {equations[i][2]} = 0): Кількість коренів = {count}")
# Виклик головної функції
if __name__ == "__main__":
    MainFunction()


#Для другого задання#
import numpy as np

def calculate_matrix(matrix):
    # Обчислюємо суму елементів по рядках
    row_sums = np.sum(matrix, axis=1)
    # Обчислюємо добуток елементів по рядках
    row_products = np.prod(matrix, axis=1)
    
    print("Суми елементів рядків:", row_sums)
    print("Добутки елементів рядків:", row_products)
    
    # Створюємо випадкову матрицю того ж розміру
    random_matrix = np.random.randint(1, 10, size=matrix.shape)
    
    # Обчислюємо різницю між початковою і випадковою матрицями
    result_matrix = matrix - random_matrix
    print("Різниця початкової і випадкової матриць:\n", result_matrix)
    
    return row_sums, row_products, result_matrix

def process_matrix():
    def read_and_process_matrix(file_name=None):
        if file_name:
            # Завантажуємо матрицю з файлу
            try:
                matrix = np.loadtxt(file_name, dtype=int)
            except Exception as e:
                print(f"Помилка при завантаженні файлу: {e}")
                return None, None, None
        else:
            try:
                rows = int(input("Введіть кількість рядків матриці: "))
                cols = int(input("Введіть кількість стовпців матриці: "))
                matrix = []
                print("Введіть елементи матриці:")
                for i in range(rows):
                    row = list(map(int, input(f"Рядок {i + 1}: ").split()))
                    if len(row) != cols:
                        print("Кількість елементів у рядку не відповідає вказаній кількості стовпців.")
                        return None, None, None
                    matrix.append(row)
                matrix = np.array(matrix)
            except ValueError:
                print("Помилка: введіть коректні цілі числа.")
                return None, None, None

        # Виклик функції обчислення параметрів
        return calculate_matrix(matrix)

    choice = input("Оберіть метод введення матриці (1 - з файлу, 2 - вручну): ")
    if choice == "1":
        filename = input("Введіть шлях до файлу з матрицею: ")
        row_sums, row_products, result_matrix = read_and_process_matrix(filename)
    elif choice == "2":
        row_sums, row_products, result_matrix = read_and_process_matrix()
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
        return
    
    if row_sums is not None:
        # Виведення результатів
        print(f"Суми елементів рядків: {row_sums}")
        print(f"Добутки елементів рядків: {row_products}")
        print(f"Різниця початкової і випадкової матриць:\n{result_matrix}")
# Виконуємо основну функцію
if __name__ == "__main__":
    process_matrix()
