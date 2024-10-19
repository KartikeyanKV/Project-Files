# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:47:43 2024

@author: admin
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # You may need to install Pillow library

def save_info():
    messagebox.showinfo("Saved", "Student information has been saved successfully!")

def update_info():
    messagebox.showinfo("Update", "Student information updated successfully!")

def delete_info():
    messagebox.showinfo("Delete", "Student information deleted successfully!")

def reset_info():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    # Reset other fields...

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("900x600")

# Header with images (can be loaded using PIL for multiple images)
header_frame = tk.Frame(root, bg="lightblue", height=100)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 20, "bold"), bg="lightblue")
header_label.pack(pady=10)

# Frame for Student Information
info_frame = tk.Frame(root, bd=2, relief=tk.SOLID, padx=10, pady=10)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tk.Label(info_frame, text="Student Information", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)

# Labels and Entry widgets for student information
tk.Label(info_frame, text="Name").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_name = tk.Entry(info_frame)
entry_name.grid(row=1, column=1)

tk.Label(info_frame, text="Roll No").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_roll = tk.Entry(info_frame)
entry_roll.grid(row=2, column=1)

tk.Label(info_frame, text="Email").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_email = tk.Entry(info_frame)
entry_email.grid(row=3, column=1)

tk.Label(info_frame, text="Phone").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_phone = tk.Entry(info_frame)
entry_phone.grid(row=4, column=1)

tk.Label(info_frame, text="Class Division").grid(row=5, column=0, sticky=tk.W, pady=5)
combo_division = ttk.Combobox(info_frame, values=["A", "B", "C"])
combo_division.grid(row=5, column=1)

tk.Label(info_frame, text="Department").grid(row=6, column=0, sticky=tk.W, pady=5)
combo_department = ttk.Combobox(info_frame, values=["Computer", "Electronics", "Mechanical"])
combo_department.grid(row=6, column=1)

# Buttons (Save, Update, Delete, Reset)
button_frame = tk.Frame(info_frame)
button_frame.grid(row=7, columnspan=2, pady=10)

btn_save = tk.Button(button_frame, text="Save", command=save_info, width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Update", command=update_info, width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Delete", command=delete_info, width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_reset = tk.Button(button_frame, text="Reset", command=reset_info, width=10)
btn_reset.pack(side=tk.LEFT, padx=5)

# Frame for Student Search and Table View
search_frame = tk.Frame(root, bd=2, relief=tk.SOLID, padx=10, pady=10)
search_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(search_frame, text="Search Student", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)

search_option = ttk.Combobox(search_frame, values=["Reference No", "Department", "Course", "Year", "Semester"])
search_option.grid(row=1, column=0, padx=5)

search_entry = tk.Entry(search_frame)
search_entry.grid(row=1, column=1, padx=5)

btn_search = tk.Button(search_frame, text="Search", width=10)
btn_search.grid(row=1, column=2, padx=5)

# Student Details Table
columns = ("ref_no", "department", "course", "year", "semester", "student_id", "student_name", "division")
student_table = ttk.Treeview(search_frame, columns=columns, show="headings")
student_table.grid(row=2, column=0, columnspan=3, pady=10)

# Define column headings
for col in columns:
    student_table.heading(col, text=col.replace("_", " ").title())

# Sample data for the table (can be fetched from a database or file)
sample_data = [
    ("1", "Computer", "BE", "2020-2021", "Semester-2", "DSE1425", "Mandhana", "A"),
    ("2", "Computer", "BE", "2020-2021", "Semester-2", "DSE1426", "Pooja", "A"),
    ("3", "Computer", "BE", "2020-2021", "Semester-2", "DSE1427", "Nisha", "A")
]

# Insert sample data into the table
for data in sample_data:
    student_table.insert("", tk.END, values=data)

root.mainloop()

