import math
import matplotlib.pyplot as plt

class Point:
    """Клас, який представляє точку на площині."""
    instance_count = 0  # Лічильник екземплярів класу

    def __init__(self, x=0, y=0):
        """Ініціалізує координати точки та збільшує лічильник екземплярів."""
        self._x = self._validate_coordinate(x)
        self._y = self._validate_coordinate(y)
        Point.instance_count += 1

    def __del__(self):
        """Зменшує лічильник екземплярів при видаленні об'єкта."""
        Point.instance_count -= 1
        print(f"Точка з координатами ({self._x}, {self._y}) видалена.")

    @staticmethod
    def _validate_coordinate(value):
        """Перевірка, чи знаходиться значення в діапазоні [-100, 100]."""
        return value if -100 <= value <= 100 else 0

    @property
    def x(self):
        """Повертає координату x."""
        return self._x

    @x.setter
    def x(self, value):
        """Встановлює координату x з перевіркою."""
        self._x = self._validate_coordinate(value)

    @property
    def y(self):
        """Повертає координату y."""
        return self._y

    @y.setter
    def y(self, value):
        """Встановлює координату y з перевіркою."""
        self._y = self._validate_coordinate(value)

    def move(self, dx, dy):
        """Зміщує координати точки на dx і dy."""
        self._x = self._validate_coordinate(self._x + dx)
        self._y = self._validate_coordinate(self._y + dy)

    def __repr__(self):
        """Рядкове представлення об'єкта."""
        return f"Point(x={self._x}, y={self._y})"

# Створюємо три точки
points = [Point(10, 20), Point(30, 40), Point(-50, -60)]

# Визначаємо відстань між другою і третьою точками
distance = math.sqrt((points[1].x - points[2].x) ** 2 + (points[1].y - points[2].y) ** 2)
print(f"Відстань між другою і третьою точками: {distance:.2f}")

# Список координат точок до переміщення
x_coords_before = [point.x for point in points]
y_coords_before = [point.y for point in points]

# Переміщаємо першу точку на 50 одиниць вгору
points[0].move(0, 50)

# Список координат точок після переміщення
x_coords_after = [point.x for point in points]
y_coords_after = [point.y for point in points]

# Створюємо графік
plt.figure(figsize=(8, 6))

# Малюємо точки до переміщення (зелені)
plt.scatter(x_coords_before, y_coords_before, color="green", label="До зміни")
for i, point in enumerate(points):
    plt.text(x_coords_before[i], y_coords_before[i], f"P{i+1}", color="green")

# Малюємо точки після переміщення (яскраво-розові)
plt.scatter(x_coords_after, y_coords_after, color="hotpink", label="Після зміни")
for i, point in enumerate(points):
    plt.text(x_coords_after[i], y_coords_after[i], f"P{i+1}", color="hotpink")

plt.axhline(0, color="black", linewidth=0.5)  # Горизонтальна лінія
plt.axvline(0, color="black", linewidth=0.5)  # Вертикальна лінія
plt.grid(color="gray", linestyle="--", linewidth=0.5)  # Сітка
plt.legend()
plt.title("Зміна координат точок")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Зберігаємо дані точок у файл
with open("points_data.txt", "w") as file:
    for i, point in enumerate(points, start=1):
        file.write(f"{i} {point.x}:{point.y}\n")

print("Дані точок збережені у файл 'points_data.txt'.")
