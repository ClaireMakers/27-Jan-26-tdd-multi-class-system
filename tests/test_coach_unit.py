from lib.coach import Coach
from unittest.mock import Mock


def test_add_student():
    #Fake student
    mock_student = Mock(name="mock_student")
    mock_student.name = "mock_student"

    #Real coach:
    coach = Coach()

    coach.add_student(mock_student)
    assert coach.student_roster == [mock_student]

def test_count_submissions():
    #Fake student
    mock_student = Mock()
    mock_student.name = "mock_student"

    mock_student.count_submissions.return_value = 1

    #Real coach:
    coach = Coach()
    coach.add_student(mock_student)

    assert coach.count_students_submission() == 1