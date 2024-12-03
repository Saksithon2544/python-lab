class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    def get_details(self):
        return f"Teacher: {self.name}, ID: {self.teacher_id}, Subject: {self.subject}"
