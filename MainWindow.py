import tkinter as tk

from LoginWindow import LoginWindow
from RegistrationWindow import RegistrationWindow


class MainWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')

        # создаем Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='pink')

        self.draw_walls()
        self.create_buttons()
        self.root.mainloop()

    def draw_walls(self):
        # размер отступа от края окна
        padding = 20
        # координаты угловых точек
        x1, y1 = padding, padding
        x2, y2 = self.width - padding, self.height - padding
        # верхняя горизонтальная линия
        self.canvas.create_text((x1 + x2) // 2, y1 - 10, text="═" * (x2 - x1), font=("Courier New", 12), fill="white")
        # нижняя горизонтальная линия
        self.canvas.create_text((x1 + x2) // 2, y2 + 10, text="═" * (x2 - x1), font=("Courier New", 12), fill="white")
        # левая вертикальная линия
        self.canvas.create_text(x1 - 10, (y1 + y2) // 2, text="\n".join(["║"] * (y2 - y1)), font=("Courier New", 12),
                                fill="white")
        # правая вертикальная линия
        self.canvas.create_text(x2 + 10, (y1 + y2) // 2, text="\n".join(["║"] * (y2 - y1)), font=("Courier New", 12),
                                fill="white")

    def create_buttons(self):
        # создаем кнопки
        button1 = tk.Button(self.root, text="Login", width=20, height=3, font=("Arial", 13),
                            command=self.open_login_window)
        button2 = tk.Button(self.root, text="Registration", width=20, height=3, font=("Arial", 13),
                            command=self.open_registration_window)
        button3 = tk.Button(self.root, text="Exit", width=8, height=2, command=self.close_window, font=("Arial", 10))

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width // 2, self.height // 2 - 100, window=button1)
        self.canvas.create_window(self.width // 2, self.height // 2, window=button2)
        self.canvas.create_window(self.width // 2 + 300, self.height // 2 + 300, window=button3)

    def close_window(self):
        self.root.destroy()

    def open_login_window(self):
        # создаем экземпляр класса AddWindow
        LoginWindow()

    def open_registration_window(self):
        # создаем экземпляр класса AddWindow
        RegistrationWindow()