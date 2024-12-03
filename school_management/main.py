from models.student import Student
from models.teacher import Teacher
from utils.helpers import print_details

# Create instances
student1 = Student("Alice", "S001", "A")
student2 = Student("Bob", "S002", "B")
teacher1 = Teacher("Mr. John", "T001", "Math")

# Print details
print_details(student1)
print_details(student2)
print_details(teacher1)

# Update grade
student1.update_grade("A+")
print("\nAfter grade update:")
print_details(student1)
