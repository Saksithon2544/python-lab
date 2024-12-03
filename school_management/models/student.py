class Student:
    # Constructor method ใช้สำหรับกำหนดค่าเริ่มต้นให้กับอ็อบเจ็กต์เมื่อมีการสร้างวัตถุจากคลาสนี้
    def __init__(self, name, student_id, grade):
        self.name = name  # ชื่อของนักเรียน (Attribute)
        self.student_id = student_id  # รหัสประจำตัวนักเรียน (Attribute)
        self.grade = grade  # เกรดของนักเรียน (Attribute)

    # เมธอดสำหรับดึงข้อมูลนักเรียนในรูปแบบข้อความที่อ่านง่าย
    def get_details(self):
        return f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}"
        # คืนค่าข้อมูลชื่อ รหัส และเกรดในรูปแบบข้อความ

    # เมธอดสำหรับอัปเดตเกรดของนักเรียน
    def update_grade(self, new_grade):
        self.grade = new_grade  # เปลี่ยนค่าเกรดของนักเรียนให้เป็นค่าที่ส่งมาใน new_grade
