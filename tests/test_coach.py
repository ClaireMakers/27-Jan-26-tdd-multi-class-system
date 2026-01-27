from lib.coach import Coach
from lib.student import Student


def test_add_student():
    coach = Coach()
    lea = Student("Lea")

    coach.add_student(lea)
    assert coach.student_roster == [lea]

def test_count_students_submissions_when_1_student_in_roster(): 
    lea = Student("Lea")
    lea.save_submission({"name": "password_manager", "date": "random date"})

    coach = Coach()
    coach.add_student(lea)

    assert coach.count_students_submission() == 1

def test_count_students_submissions_when_multiple_students_in_roster():
    lea = Student("Lea")
    lea.save_submission({"name": "password_manager", "date": "random date"})

    claire = Student("Claire")
    claire.save_submission({"name": "password_manager", "date": "random date"})

    coach = Coach()
    coach.add_student(lea)
    coach.add_student(claire)

    assert coach.count_students_submission() == 2

#Integration test:
#Test requires the use of another class 

#Unit test:
#Testing one class/method in isolation 