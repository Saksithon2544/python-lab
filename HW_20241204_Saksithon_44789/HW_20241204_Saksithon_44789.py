import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import os
import csv

# ชื่อไฟล์ CSV
CSV_FILE = "employee_data.csv"

try:
    df = pd.read_csv(CSV_FILE)
    print(df.head())  # แสดงข้อมูล 5 แถวแรก
except Exception as e:
    print(f"Error reading CSV file: {e}")


# ฟังก์ชันตรวจสอบและสร้างไฟล์ CSV
def initialize_csv():
    if not os.path.isfile(CSV_FILE):
        # สร้างไฟล์ใหม่พร้อม header หากยังไม่มี
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Full Name", "Nickname", "Telephone"])
    else:
        # ตรวจสอบว่าไฟล์ CSV มี header ที่ถูกต้อง
        df = pd.read_csv(CSV_FILE)
        required_columns = ["Employee ID", "Full Name", "Nickname", "Telephone"]
        if not all(col in df.columns for col in required_columns):
            # เขียน header ใหม่หากไม่ถูกต้อง
            with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID", "Full Name", "Nickname", "Telephone"])

# ฟังก์ชันโหลดข้อมูลจาก CSV
def load_data():
    if os.path.isfile(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            return df
        except Exception as e:
            messagebox.showerror("Error", f"Error loading CSV: {e}")
            return pd.DataFrame(columns=["Employee ID", "Full Name", "Nickname", "Telephone"])
    else:
        return pd.DataFrame(columns=["Employee ID", "Full Name", "Nickname", "Telephone"])

# ฟังก์ชันบันทึกข้อมูลลง CSV
def save_data(df):
    try:
        df.to_csv(CSV_FILE, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Error saving CSV: {e}")

# ฟังก์ชันเพิ่มข้อมูล
def insert_data():
    def save_insert_data():
        emp_id = emp_id_entry.get()
        full_name = full_name_entry.get()
        nickname = nickname_entry.get()
        telephone = telephone_entry.get()

        if emp_id and full_name and nickname and telephone:
            df = load_data()
            df = pd.concat([df, pd.DataFrame([[emp_id, full_name, nickname, telephone]], columns=df.columns)])
            save_data(df)
            refresh_listbox()
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    # สร้างหน้าต่างใหม่สำหรับการเพิ่มข้อมูล
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")
    add_window.geometry("300x250")

    # สร้างฟอร์ม
    tk.Label(add_window, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
    emp_id_entry = tk.Entry(add_window)
    emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Full Name").grid(row=1, column=0, padx=10, pady=5)
    full_name_entry = tk.Entry(add_window)
    full_name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Nickname").grid(row=2, column=0, padx=10, pady=5)
    nickname_entry = tk.Entry(add_window)
    nickname_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Telephone").grid(row=3, column=0, padx=10, pady=5)
    telephone_entry = tk.Entry(add_window)
    telephone_entry.grid(row=3, column=1, padx=10, pady=5)

    # ปุ่มบันทึก
    save_button = tk.Button(add_window, text="Save", command=save_insert_data)
    save_button.grid(row=4, columnspan=2, pady=10)

# ฟังก์ชันแก้ไขข้อมูล
def edit_data():
    def save_edit_data():
        emp_id = emp_id_entry.get()
        full_name = full_name_entry.get()
        nickname = nickname_entry.get()
        telephone = telephone_entry.get()

        if emp_id and full_name and nickname and telephone:
            df = pd.read_csv(CSV_FILE)
            df['Employee ID'] = df['Employee ID'].astype(str)

            # อัพเดตข้อมูล
            df.loc[df['Employee ID'] == emp_id, 'Full Name'] = full_name
            df.loc[df['Employee ID'] == emp_id, 'Nickname'] = nickname
            df.loc[df['Employee ID'] == emp_id, 'Telephone'] = telephone

            # บันทึกข้อมูลกลับลงไฟล์
            df.to_csv(CSV_FILE, index=False)
            messagebox.showinfo("Success", "Data updated successfully.")
            refresh_listbox()
            edit_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    emp_id = simpledialog.askstring("Edit", "Enter Employee ID to edit:")
    if not emp_id:
        messagebox.showinfo("Error", "No Employee ID entered.")
        return

    try:
        df = pd.read_csv(CSV_FILE)
        df['Employee ID'] = df['Employee ID'].astype(str)

        result = df[df['Employee ID'] == emp_id]
        if not result.empty:
            # ดึงข้อมูลเดิมจาก result
            current_full_name = result.iloc[0]['Full Name']
            current_nickname = result.iloc[0]['Nickname']
            current_telephone = result.iloc[0]['Telephone']

            # สร้างหน้าต่างใหม่สำหรับการแก้ไขข้อมูล
            edit_window = tk.Toplevel(root)
            edit_window.title("Edit Employee")
            edit_window.geometry("300x250")

            # สร้างฟอร์ม
            tk.Label(edit_window, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
            emp_id_entry = tk.Entry(edit_window)
            emp_id_entry.insert(0, emp_id)
            emp_id_entry.config(state="disabled")  # ไม่ให้แก้ไข Employee ID
            emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(edit_window, text="Full Name").grid(row=1, column=0, padx=10, pady=5)
            full_name_entry = tk.Entry(edit_window)
            full_name_entry.insert(0, current_full_name)
            full_name_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(edit_window, text="Nickname").grid(row=2, column=0, padx=10, pady=5)
            nickname_entry = tk.Entry(edit_window)
            nickname_entry.insert(0, current_nickname)
            nickname_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(edit_window, text="Telephone").grid(row=3, column=0, padx=10, pady=5)
            telephone_entry = tk.Entry(edit_window)
            telephone_entry.insert(0, current_telephone)
            telephone_entry.grid(row=3, column=1, padx=10, pady=5)

            # ปุ่มบันทึก
            save_button = tk.Button(edit_window, text="Save", command=save_edit_data)
            save_button.grid(row=4, columnspan=2, pady=10)
        else:
            messagebox.showinfo("Error", "Employee ID not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to edit data: {e}")
        
# ฟังก์ชันลบข้อมูล
def delete_data():
    # ขอรหัสพนักงานจากผู้ใช้
    emp_id = simpledialog.askstring("Delete", "Enter Employee ID to delete:")
    if not emp_id:
        messagebox.showinfo("Error", "No Employee ID entered.")
        return

    # อ่านข้อมูลจากไฟล์ CSV
    try:
        df = pd.read_csv(CSV_FILE)
        df['Employee ID'] = df['Employee ID'].astype(str)

        # ค้นหาข้อมูลพนักงานที่ตรงกับรหัสที่ป้อน
        result = df[df['Employee ID'] == emp_id]
        if not result.empty:
            # ลบข้อมูลพนักงานที่ตรงกับรหัสพนักงาน
            df = df[df['Employee ID'] != emp_id]
            df.to_csv(CSV_FILE, index=False)
            messagebox.showinfo("Success", f"Employee {emp_id} deleted successfully.")
            refresh_listbox()
        else:
            messagebox.showinfo("Error", "Employee ID not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete data: {e}")

    
# ฟังก์ชันค้นหาข้อมูลพนักงาน
def search_data():
    # ขอรหัสพนักงานจากผู้ใช้
    emp_id = simpledialog.askstring("Search", "Enter Employee ID to search:")
    if not emp_id:
        messagebox.showinfo("Error", "No Employee ID entered.")
        return

    # อ่านข้อมูลจากไฟล์ CSV
    try:
        df = pd.read_csv(CSV_FILE)
        df['Employee ID'] = df['Employee ID'].astype(str)

        # ค้นหาข้อมูลพนักงานที่ตรงกับรหัสที่ป้อน
        result = df[df['Employee ID'] == emp_id]
        if not result.empty:
            # แสดงข้อมูลพนักงานที่ค้นพบ
            result_str = result.to_string(index=False)
            messagebox.showinfo("Search Result", f"Employee Data Found:\n{result_str}")
        else:
            messagebox.showinfo("Error", "Employee ID not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to search data: {e}")


# ฟังก์ชันอัปเดตข้อมูลใน Listbox
def refresh_listbox():
    lb.delete(0, tk.END)
    df = load_data()
    for _, row in df.iterrows():
        # แปลงเบอร์โทรเป็น string ก่อนแสดง
        telephone = str(row['Telephone'])
        lb.insert(tk.END, f"{row['Employee ID']} - {row['Full Name']} ({row['Nickname']}) - {telephone}")

# สร้างหน้าต่าง GUI หลัก
root = tk.Tk()
root.geometry("500x300")
root.title("Employee Management System")

# เริ่มต้นไฟล์ CSV
initialize_csv()

# สร้าง Listbox
lb = tk.Listbox(root)
lb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# สร้างปุ่ม
btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, padx=10, pady=5)

btn_add = tk.Button(btn_frame, text="Add", command=insert_data, bg="lightgreen")
btn_add.pack(side=tk.LEFT, padx=5)

btn_edit = tk.Button(btn_frame, text="Edit", command=edit_data, bg="lightblue")
btn_edit.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete", command=delete_data, bg="red")
btn_delete.pack(side=tk.LEFT, padx=5)

btn_search = tk.Button(btn_frame, text="Search", command=search_data, bg="yellow")
btn_search.pack(side=tk.LEFT, padx=5)

refresh_listbox()

root.mainloop()
