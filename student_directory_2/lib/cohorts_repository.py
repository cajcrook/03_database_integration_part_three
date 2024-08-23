from lib.cohorts import Cohort
from lib.students import Student

class CohortRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    # Find a single cohort by their id
    def find(self, cohort_id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [
                                 cohort.name, cohort.start_date])
        return None

    # Delete an artist by their id
    def delete(self, cohort_id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [cohort_id])
        return None


    def find_with_students(self, cohort_id):
        rows = self._connection.execute("SELECT cohorts.id AS cohort_id, cohorts.name AS cohort_name, cohorts.starting_date, students.id AS student_id, students.name AS student_name FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohorts.id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["starting_date"], "HELLO")

