class Student:
    def __init__(self, name):
        self.submissions = []
        self.name = name

    def save_submission(self, submission):
        self.submissions.append(submission)

    def count_submissions(self):
        return len(self.submissions)
    
