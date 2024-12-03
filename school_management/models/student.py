class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def get_details(self):
        return f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}"

    def update_grade(self, new_grade):
        self.grade = new_grade
