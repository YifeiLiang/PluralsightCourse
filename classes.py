students = []
class Student:
    school_name = "Springfield Elementary"
    def __init__(self, name,lastname, student_id = 332):
        self.name = name
        self.last_name = lastname
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitaliza(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a high school Student"
    def get_name_capitaliza(self):
        original_value=super().get_name_capitaliza()
        return original_value + "--HS"


