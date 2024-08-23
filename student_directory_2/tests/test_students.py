from lib.students import Student

"""
Student constructs with an id, name and cohort_id
"""
def test_student_constructs():
    student = Student(1, "Name", "Cohort_ID")
    assert student.id == 1
    assert student.name == "Name"
    assert student.cohort_id == "Cohort_ID"

"""
We can format artists to strings nicely
"""
def test_format_nicely():
    student = Student(1, "Name", "Cohort_ID")
    assert str(student) == "Student(1, Name, Cohort_ID)"

"""
We can compare two identical artists
And have them be equal
"""
def test_student_are_equal():
    student1 = Student(1, "Name", "Cohort_ID")
    student2 = Student(1, "Name", "Cohort_ID")
    assert student1 == student2