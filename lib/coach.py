class Coach:
    def __init__(self):
        self.student_roster = []

    def add_student(self, student):
        self.student_roster.append(student)

    def count_students_submission(self):
        total = 0

        for student in self.student_roster:
            total += student.count_submissions()
        
        return total
        