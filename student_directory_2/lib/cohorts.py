class Cohort:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, start_date, students = []):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.students = students


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Cohort({self.id}, {self.name}, {self.start_date})"
