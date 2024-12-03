# นำเข้าคลาส Student และ Teacher จากไฟล์ models และฟังก์ชัน print_details จากไฟล์ utils
from models.student import Student
from models.teacher import Teacher
from utils.helpers import print_details

# สร้างอ็อบเจ็กต์ของนักเรียนและครู
student1 = Student("Alice", "S001", "A")  # สร้างนักเรียน Alice รหัส S001 เกรด A
student2 = Student("Bob", "S002", "B")    # สร้างนักเรียน Bob รหัส S002 เกรด B
teacher1 = Teacher("Mr. John", "T001", "Math")  # สร้างครู Mr. John รหัส T001 สอนวิชา Math

# แสดงข้อมูลของนักเรียนและครู
print_details(student1)  # แสดงข้อมูลของ Alice
print_details(student2)  # แสดงข้อมูลของ Bob
print_details(teacher1)  # แสดงข้อมูลของ Mr. John

# อัปเดตเกรดของ Alice
student1.update_grade("A+")  # เปลี่ยนเกรดของ Alice จาก A เป็น A+

# แสดงข้อมูลของ Alice อีกครั้งหลังอัปเดตเกรด
print("\nAfter grade update:")  # เพิ่มบรรทัดว่างและข้อความเพื่อแสดงส่วนใหม่
print_details(student1)  # แสดงข้อมูลของ Alice หลังเปลี่ยนเกรด
