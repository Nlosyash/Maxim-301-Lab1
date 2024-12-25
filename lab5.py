import tkinter as tk
from tkinter import messagebox


def Swap(X, I, J):
    """Змінює місцями елементи XI та XJ у списку X."""
    if I < 0 or J < 0 or I >= len(X) or J >= len(X):
        raise ValueError("Індекси мають бути в межах довжини списку!")
    X[I], X[J] = X[J], X[I]


class SwapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сwap елементів списку")

        # Елементи інтерфейсу
        self.label = tk.Label(root, text="Введіть список із 4 елементів через кому:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Поміняти місцями", command=self.swap_elements)
        self.calculate_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Результат відобразиться тут.")
        self.result_label.pack(pady=5)

    def swap_elements(self):
        try:
            # Зчитування введеного списку
            input_data = self.entry.get()
            elements = list(map(float, input_data.split(",")))

            if len(elements) != 4:
                raise ValueError("Список повинен містити рівно 4 елементи!")

            # Використання функції Swap
            Swap(elements, 0, 1)  # Заміна перших двох елементів
            Swap(elements, 2, 3)  # Заміна останніх двох елементів
            Swap(elements, 1, 2)  # Заміна двох середніх елементів

            # Відображення результату
            result_text = f"Новий список: {elements}"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Помилка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SwapApp(root)
    root.mainloop()
