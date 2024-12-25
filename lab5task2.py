import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

# Глобальні змінні для даних
data_x = []
data_y = []

# Функція для обчислення y[k]
def calculate_values():
    try:
        # Отримуємо вхідні дані з полів
        T = float(entry_T.get())
        K = float(entry_K.get())
        xi = float(entry_xi.get())
        U0 = float(entry_U0.get())
        y0 = 0  # Початкове значення y[0]
        y1 = 0  # Початкове значення y[1]
        N = 100  # Кількість ітерацій

        if T <= 0:
            raise ValueError("T має бути більше нуля.")

        global data_x, data_y
        data_x = list(range(N))
        data_y = [y0, y1]

        # Коефіцієнти рівняння
        a1 = 2 - 2 * xi * T
        a2 = 2 * xi * T - 1 - T**2
        b = K * T**2

        # Обчислюємо y[k+2] за формулою
        for k in range(2, N):
            y_next = a1 * data_y[k - 1] + a2 * data_y[k - 2] + b * U0
            data_y.append(y_next)
        
        messagebox.showinfo("Успіх", "Обчислення завершено.")
    except ValueError as e:
        messagebox.showerror("Помилка", f"Помилка в обчисленнях: {e}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Неочікувана помилка: {e}")

# Функція для обчислення мінімуму та максимуму
def calculate_min_max():
    try:
        if not data_x or not data_y:  # Перевірка на порожні масиви
            raise ValueError("Масиви даних порожні.")
        min_x, max_x = min(data_x), max(data_x)
        min_y, max_y = min(data_y), max(data_y)
        messagebox.showinfo("Результати", f"Мінімум X: {min_x}\nМаксимум X: {max_x}\nМінімум Y: {min_y}\nМаксимум Y: {max_y}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для запису даних у файл
def save_to_file():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        
        delimiter = ';'
        
        with open(file_path, "w") as f:
            for x, y in zip(data_x, data_y):
                f.write(f"{x}{delimiter} {y}\n")
        
        messagebox.showinfo("Успіх", "Дані успішно записано у файл.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для зчитування даних з файлу
def load_from_file():
    global data_x, data_y
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        
        with open(file_path, "r") as f:
            lines = f.readlines()

        delimiter = ";" if ";" in lines[0] else "#"
        data_x, data_y = [], []
        for line in lines:
            x, y = map(float, line.strip().split(delimiter))
            data_x.append(x)
            data_y.append(y)
        
        messagebox.showinfo("Успіх", "Дані успішно зчитано.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для побудови графіка
def plot_graph():
    try:
        if not data_x or not data_y:
            raise ValueError("Дані для графіка порожні.")
        
        plt.figure()
        plt.plot(data_x, data_y, label="y[k]")
        plt.title("Графік функції y[k]")
        plt.xlabel("k (індекс)")
        plt.ylabel("y[k]")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Основна функція для побудови GUI
def main():
    root = tk.Tk()
    root.title("Розв’язання рівняння різницевого оператора")

    tk.Label(root, text="T (період):").grid(row=0, column=0, padx=5, pady=5)
    global entry_T
    entry_T = tk.Entry(root)
    entry_T.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="K (коефіцієнт):").grid(row=1, column=0, padx=5, pady=5)
    global entry_K
    entry_K = tk.Entry(root)
    entry_K.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="ξ (демпфування):").grid(row=2, column=0, padx=5, pady=5)
    global entry_xi
    entry_xi = tk.Entry(root)
    entry_xi.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="U[0] (початкове значення):").grid(row=3, column=0, padx=5, pady=5)
    global entry_U0
    entry_U0 = tk.Entry(root)
    entry_U0.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(root, text="Обчислити y[k]", command=calculate_values).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Зберегти у файл", command=save_to_file).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Зчитати з файлу", command=load_from_file).grid(row=6, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Обчислити min/max", command=calculate_min_max).grid(row=7, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Побудувати графік", command=plot_graph).grid(row=8, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
