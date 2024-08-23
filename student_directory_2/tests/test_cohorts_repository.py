from lib.cohorts_repository import CohortRepository
from lib.cohorts import Cohort
from lib.students import Student

"""
When we call CohortRepository #all
We get a list of Cohorts objects reflecting the seed data.
"""
def test_get_all(db_connection): 
    db_connection.seed("seeds/student_directory_2.sql") 
    repository = CohortRepository(db_connection) 
    cohorts = repository.all() 
    assert cohorts == [
        Cohort(1, 'Cohort 1', '01/01/2023'),
        Cohort(2, 'Cohort 2', '01/06/2023'),
        Cohort(3, 'Cohort 3', '01/01/2024'),
        Cohort(4, 'Cohort 4', '01/06/2024')
    ]

"""
When we call CohortRepository #find
"""
def test_get_single_student(db_connection):
    db_connection.seed("seeds/student_directory_2.sql") 
    repository = CohortRepository(db_connection) 
    cohorts = repository.find(2) 
    assert cohorts == Cohort(2, 'Cohort 2', '01/06/2023')


"""
When we call CohortRepository #create
We get a new record in the database.
"""
def test_create(db_connection):
    db_connection.seed("seeds/student_directory_2.sql") 
    repository = CohortRepository(db_connection) 
    repository.create(Cohort(None, 'Cohort 5', '01/01/2025'))
    result = repository.all()
    assert result == [
        Cohort(1, 'Cohort 1', '01/01/2023'),
        Cohort(2, 'Cohort 2', '01/06/2023'),
        Cohort(3, 'Cohort 3', '01/01/2024'),
        Cohort(4, 'Cohort 4', '01/06/2024'),
        Cohort(5, 'Cohort 5', '01/01/2025')
    ]

"""
When we call CohortRepository #delete
We remove a record from the database.
"""
def test_delete(db_connection):
    db_connection.seed("seeds/student_directory_2.sql") 
    repository = CohortRepository(db_connection) 
    repository.delete(3)

    result = repository.all()
    assert result == [
        Cohort(1, 'Cohort 1', '01/01/2023'),
        Cohort(2, 'Cohort 2', '01/06/2023'),
        Cohort(4, 'Cohort 4', '01/06/2024')
    ]

"""
Test to see a single cohort and all students within
"""
def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql") 
    repository = CohortRepository(db_connection) 
    student = repository.find_with_students(1)
    assert student == Cohort(1, 'Cohort 1', '01/01/2023', [Student(1, 'Chris', 1)])


