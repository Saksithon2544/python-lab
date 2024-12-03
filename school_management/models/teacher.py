class Teacher:
    # Constructor method ใช้สำหรับกำหนดค่าเริ่มต้นให้กับอ็อบเจ็กต์เมื่อมีการสร้างวัตถุจากคลาสนี้
    def __init__(self, name, teacher_id, subject):
        self.name = name  # ชื่อของครู (Attribute)
        self.teacher_id = teacher_id  # รหัสประจำตัวครู (Attribute)
        self.subject = subject  # วิชาที่ครูสอน (Attribute)

    # เมธอดสำหรับดึงข้อมูลครูในรูปแบบข้อความที่อ่านง่าย
    def get_details(self):
        return f"Teacher: {self.name}, ID: {self.teacher_id}, Subject: {self.subject}"
        # คืนค่าข้อมูลชื่อ รหัส และวิชาที่สอนในรูปแบบข้อความ
