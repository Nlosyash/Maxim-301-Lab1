

def task_integer8():
    """
    Дано двозначне число.
    Вивести число, отримане при перестановці цифр вихідного числа.
    """
    try:  # перевірка на помилки
        number = int(input("Введіть двозначне число: "))
        
        # Перевірка, чи є введене число двозначним
        if number < 10 or number > 99:
            raise ValueError("Це не двозначне число!")
        
    except ValueError as e:  # якщо помилка
        print(e)
        input("Натисніть Enter для виходу...")
        
    else:  # якщо немає помилки
        tens = number // 10  # десятки
        ones = number % 10   # одиниці
        swapped_number = ones * 10 + tens  # перестановка цифр
        print("Число після перестановки цифр:", swapped_number)

# Виклик функції
task_integer8()


import math

def task2_0():
    """
    Обчислення математичного виразу:
    y = tg(|2 * x^2 + 5 * x - 31.15| + log5|x - 2.5|) /
        (корінь кубічний з (sin^2(x^3) + 1/3 * log5|x^2 - 2.5|))
    """
    try:
        # Введення значення змінної
        x = float(input("Введіть значення x (x > 2.5): "))
        
        if x <= 2.5:
            raise ValueError("x має бути більше 2.5")
    
    except ValueError as e:
        print("Помилка:", e)
        input("Натисніть Enter для виходу...")
    
    else:
        try:
            # Чисельник виразу
            numerator = math.tan(abs(2 * x**2 + 5 * x - 31.15) + math.log(abs(x - 2.5), 5))
            
            # Знаменник виразу
            denominator = (math.sin(x**3)**2 + (1/3) * math.log(abs(x**2 - 2.5), 5)) ** (1/3)
            
            # Обчислення y
            y = numerator / denominator
            
        except Exception as e:
            print("Помилка в обчисленнях:", e)
            input("Натисніть Enter для виходу...")
        else:
            print(f"Результат: y = {y}")

# Виклик функції
task2_0()



def check_opposite_pair(a, b, c):
  """
  Перевіряє, чи є серед трьох цілих чисел хоча б одна пара взаємно протилежних.

  Параметри:
  a (int): Перше ціле число.
  b (int): Друге ціле число.
  c (int): Третє ціле число.

  Повертає:
  bool: True, якщо є хоча б одна пара взаємно протилежних чисел, інакше False.
  """
  if a == -b or a == -c or b == -c:
      return True
  else:
      return False

# Приклад використання
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

result = check_opposite_pair(a, b, c)
print(f"Чи є хоча б одна пара взаємно протилежних чисел? {result}")