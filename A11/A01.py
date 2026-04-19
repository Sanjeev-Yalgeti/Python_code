import customtkinter as ctk
from tkinter import messagebox

# Optional: Set appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("Student Registration Form")

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Student Registration Form", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 20))

        # 1. Labels and textboxes for Student Name and Roll Number
        self.name_label = ctk.CTkLabel(self, text="Student Name:")
        self.name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter Name")
        self.name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.roll_label = ctk.CTkLabel(self, text="Roll Number:")
        self.roll_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.roll_entry = ctk.CTkEntry(self, placeholder_text="Enter Roll Number")
        self.roll_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # 2. Radio buttons for Gender
        self.gender_label = ctk.CTkLabel(self, text="Gender:")
        self.gender_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        self.gender_var = ctk.StringVar(value="Not Selected")
        self.male_radio = ctk.CTkRadioButton(self, text="Male", variable=self.gender_var, value="Male")
        self.male_radio.grid(row=3, column=1, padx=20, pady=5, sticky="w")
        
        self.female_radio = ctk.CTkRadioButton(self, text="Female", variable=self.gender_var, value="Female")
        self.female_radio.grid(row=4, column=1, padx=20, pady=5, sticky="w")

        # 3. Checkboxes for Hobbies
        self.hobbies_label = ctk.CTkLabel(self, text="Hobbies:")
        self.hobbies_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        self.hobby1_var = ctk.StringVar(value="")
        self.hobby1_check = ctk.CTkCheckBox(self, text="Reading", variable=self.hobby1_var, onvalue="Reading", offvalue="")
        self.hobby1_check.grid(row=5, column=1, padx=20, pady=5, sticky="w")

        self.hobby2_var = ctk.StringVar(value="")
        self.hobby2_check = ctk.CTkCheckBox(self, text="Sports", variable=self.hobby2_var, onvalue="Sports", offvalue="")
        self.hobby2_check.grid(row=6, column=1, padx=20, pady=5, sticky="w")

        self.hobby3_var = ctk.StringVar(value="")
        self.hobby3_check = ctk.CTkCheckBox(self, text="Coding", variable=self.hobby3_var, onvalue="Coding", offvalue="")
        self.hobby3_check.grid(row=7, column=1, padx=20, pady=5, sticky="w")

        # 4. Combo box for Branch selection
        self.branch_label = ctk.CTkLabel(self, text="Branch:")
        self.branch_label.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        
        self.branch_combo = ctk.CTkComboBox(self, values=["Computer Engineering", "IT", "Mechanical", "Civil"])
        self.branch_combo.grid(row=8, column=1, padx=20, pady=10, sticky="ew")
        self.branch_combo.set("Computer Engineering") # Sets the default value

        # 5 & 6. Submit and Clear Buttons
        self.submit_btn = ctk.CTkButton(self, text="Submit", command=self.submit_form, fg_color="#28a745", hover_color="#218838")
        self.submit_btn.grid(row=9, column=0, padx=20, pady=30)

        self.clear_btn = ctk.CTkButton(self, text="Clear", command=self.clear_form, fg_color="#dc3545", hover_color="#c82333")
        self.clear_btn.grid(row=9, column=1, padx=20, pady=30)

    # Function to handle Submit button click
    def submit_form(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()
        gender = self.gender_var.get()
        branch = self.branch_combo.get()
        
        # Gather selected hobbies into a list
        hobbies = []
        if self.hobby1_var.get(): hobbies.append(self.hobby1_var.get())
        if self.hobby2_var.get(): hobbies.append(self.hobby2_var.get())
        if self.hobby3_var.get(): hobbies.append(self.hobby3_var.get())
        
        # Format hobbies for the message box
        hobbies_str = ", ".join(hobbies) if hobbies else "None"

        # Construct the final message string and display it
        details = f"Registration Successful!\n\nName: {name}\nRoll Number: {roll}\nGender: {gender}\nBranch: {branch}\nHobbies: {hobbies_str}"
        messagebox.showinfo("Student Details", details)

    # Function to handle Clear button click
    def clear_form(self):
        self.name_entry.delete(0, ctk.END)
        self.roll_entry.delete(0, ctk.END)
        self.gender_var.set("Not Selected")
        self.hobby1_var.set("")
        self.hobby2_var.set("")
        self.hobby3_var.set("")
        self.branch_combo.set("Computer Engineering")

if __name__ == "__main__":
    app = App()
    app.mainloop()