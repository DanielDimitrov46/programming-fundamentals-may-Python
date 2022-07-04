class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students)<22:
            Class.__students_count-=1
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self):
        average_grade = sum(self.grades)/len(self.grades)
        for_return = f"{average_grade:.2f}"
        return float(for_return)
    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"