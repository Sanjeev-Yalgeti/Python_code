import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x850")
        self.title("Employee Management System")

        self.employee_db = {}

        self.title_label = ctk.CTkLabel(self, text="Employee CRUD System", font=("Arial", 22, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=(20, 20))

        self.id_label = ctk.CTkLabel(self, text="Employee ID:")
        self.id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.id_entry = ctk.CTkEntry(self, placeholder_text="e.g. 101")
        self.id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.name_label = ctk.CTkLabel(self, text="Name:")
        self.name_label.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter Name")
        self.name_entry.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.dept_label = ctk.CTkLabel(self, text="Department:")
        self.dept_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.dept_entry = ctk.CTkEntry(self, placeholder_text="Enter Dept")
        self.dept_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.salary_label = ctk.CTkLabel(self, text="Salary:")
        self.salary_label.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.salary_entry = ctk.CTkEntry(self, placeholder_text="Enter Salary")
        self.salary_entry.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        self.add_btn = ctk.CTkButton(self, text="Add", fg_color="#28a745", hover_color="#218838", command=self.add_employee)
        self.add_btn.grid(row=3, column=0, padx=10, pady=20)

        self.view_btn = ctk.CTkButton(self, text="View All", fg_color="#17a2b8", hover_color="#138496", command=self.view_employees)
        self.view_btn.grid(row=3, column=1, padx=10, pady=20)

        self.update_btn = ctk.CTkButton(self, text="Update", fg_color="#ffc107", text_color="black", hover_color="#e0a800", command=self.update_employee)
        self.update_btn.grid(row=3, column=2, padx=10, pady=20)

        self.delete_btn = ctk.CTkButton(self, text="Delete", fg_color="#dc3545", hover_color="#c82333", command=self.delete_employee)
        self.delete_btn.grid(row=3, column=3, padx=10, pady=20)

        self.clear_btn = ctk.CTkButton(self, text="Clear Fields", fg_color="gray", command=self.clear_fields)
        self.clear_btn.grid(row=4, column=0, columnspan=4, pady=5)

        self.display_box = ctk.CTkTextbox(self, width=550, height=200)
        self.display_box.grid(row=5, column=0, columnspan=4, padx=20, pady=20)
        self.display_box.insert(ctk.END, "Employee records will appear here...\n")
        self.display_box.configure(state="disabled")

    def validate_inputs(self):
        if not all([self.id_entry.get().strip(), self.name_entry.get().strip(), self.dept_entry.get().strip(), self.salary_entry.get().strip()]):
            messagebox.showwarning("Warning", "All fields are required!")
            return False
        return True

    def add_employee(self):
        emp_id = self.id_entry.get().strip()
        if not self.validate_inputs():
            return
        
        if emp_id in self.employee_db:
            messagebox.showerror("Error", f"Employee ID {emp_id} already exists!")
        else:
            self.employee_db[emp_id] = {
                "Name": self.name_entry.get().strip(),
                "Department": self.dept_entry.get().strip(),
                "Salary": self.salary_entry.get().strip()
            }
            messagebox.showinfo("Success", "Employee added successfully!")
            self.clear_fields()
            self.view_employees()

    def view_employees(self):
        self.display_box.configure(state="normal")
        self.display_box.delete("1.0", ctk.END)
        
        if not self.employee_db:
            self.display_box.insert(ctk.END, "No records found.")
        else:
            header = f"{'ID':<10} | {'Name':<20} | {'Department':<15} | {'Salary':<10}\n"
            self.display_box.insert(ctk.END, header)
            self.display_box.insert(ctk.END, "-" * 65 + "\n")
            for emp_id, details in self.employee_db.items():
                row = f"{emp_id:<10} | {details['Name']:<20} | {details['Department']:<15} | {details['Salary']:<10}\n"
                self.display_box.insert(ctk.END, row)
                
        self.display_box.configure(state="disabled")

    def update_employee(self):
        emp_id = self.id_entry.get().strip()
        if not emp_id:
            messagebox.showwarning("Warning", "Please enter an Employee ID to update.")
            return

        if emp_id in self.employee_db:
            if not self.validate_inputs():
                return
            self.employee_db[emp_id] = {
                "Name": self.name_entry.get().strip(),
                "Department": self.dept_entry.get().strip(),
                "Salary": self.salary_entry.get().strip()
            }
            messagebox.showinfo("Success", f"Employee ID {emp_id} updated successfully!")
            self.clear_fields()
            self.view_employees()
        else:
            messagebox.showerror("Error", f"Employee ID {emp_id} not found!")

    def delete_employee(self):
        emp_id = self.id_entry.get().strip()
        if not emp_id:
            messagebox.showwarning("Warning", "Please enter an Employee ID to delete.")
            return

        if emp_id in self.employee_db:
            del self.employee_db[emp_id]
            messagebox.showinfo("Success", f"Employee ID {emp_id} deleted successfully!")
            self.clear_fields()
            self.view_employees()
        else:
            messagebox.showerror("Error", f"Employee ID {emp_id} not found!")

    def clear_fields(self):
        self.id_entry.delete(0, ctk.END)
        self.name_entry.delete(0, ctk.END)
        self.dept_entry.delete(0, ctk.END)
        self.salary_entry.delete(0, ctk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()