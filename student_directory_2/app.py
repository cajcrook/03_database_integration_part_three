from lib.database_connection import DatabaseConnection
from lib.cohorts_repository import CohortRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")
# cohort = Cohort(connection)
# student = Student(connection)
cohort_repository = CohortRepository(connection)
cohorts = cohort_repository.find_with_students(2)
print(cohorts)

# List them out
# for cohort in cohorts:
#     print(cohort)

