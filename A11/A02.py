import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x350")
        self.title("GUI Calculator")

        self.title_label = ctk.CTkLabel(self, text="Basic Calculator", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

        self.num1_label = ctk.CTkLabel(self, text="Enter First Number:")
        self.num1_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="e")
        self.num1_entry = ctk.CTkEntry(self, placeholder_text="Num 1")
        self.num1_entry.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="w")

        self.num2_label = ctk.CTkLabel(self, text="Enter Second Number:")
        self.num2_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")
        self.num2_entry = ctk.CTkEntry(self, placeholder_text="Num 2")
        self.num2_entry.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky="w")

        self.add_btn = ctk.CTkButton(self, text="+", width=50, command=lambda: self.calculate("+"))
        self.add_btn.grid(row=3, column=0, padx=10, pady=20)

        self.sub_btn = ctk.CTkButton(self, text="-", width=50, command=lambda: self.calculate("-"))
        self.sub_btn.grid(row=3, column=1, padx=10, pady=20)

        self.mul_btn = ctk.CTkButton(self, text="*", width=50, command=lambda: self.calculate("*"))
        self.mul_btn.grid(row=3, column=2, padx=10, pady=20)

        self.div_btn = ctk.CTkButton(self, text="/", width=50, command=lambda: self.calculate("/"))
        self.div_btn.grid(row=3, column=3, padx=10, pady=20)

        self.result_label = ctk.CTkLabel(self, text="Result: ", font=("Arial", 16, "bold"), text_color="#28a745")
        self.result_label.grid(row=4, column=0, columnspan=4, pady=10)

        self.clear_btn = ctk.CTkButton(self, text="Clear", fg_color="#dc3545", hover_color="#c82333", command=self.clear_form)
        self.clear_btn.grid(row=5, column=0, columnspan=4, pady=10)

    def calculate(self, operation):
        try:
            # 4. Handle invalid input (Will throw ValueError if user types letters)
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = 0

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":

                if num2 == 0:
                    messagebox.showerror("Math Error", "Cannot divide by zero!")
                    return
                result = num1 / num2

            self.result_label.configure(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values!")


    def clear_form(self):
        self.num1_entry.delete(0, ctk.END)
        self.num2_entry.delete(0, ctk.END)
        self.result_label.configure(text="Result: ")

if __name__ == "__main__":
    app = App()
    app.mainloop()