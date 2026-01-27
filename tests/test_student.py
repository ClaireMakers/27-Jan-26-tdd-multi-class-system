from lib.student import Student



def test_submissions_list_is_empty_on_initialization_and_student_has_name():
    student = Student("Lea") 

    assert len(student.submissions) == 0
    assert student.name == "Lea"

def test_save_submissions(): 
    submission = { "name": "password_validator", "date": "11/06/2030" }
    student = Student("Lea") 

    student.save_submission(submission)
    assert len(student.submissions) == 1
    assert student.submissions == [{ "name": "password_validator", "date": "11/06/2030" }]

def test_count_submissions(): 
    submission = { "name": "password_validator", "date": "11/06/2030" }
    student = Student("Lea") 

    student.save_submission(submission)
    assert student.count_submissions() == 1
