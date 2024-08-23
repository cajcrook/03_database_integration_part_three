from lib.cohorts import Cohort

"""
Cohort constructs with an id, name and genre
"""
def test_constructs():
    cohort = Cohort(1, "Name", "Start Date")
    assert cohort.id == 1
    assert cohort.name == "Name"
    assert cohort.start_date == "Start Date"

"""
We can format to strings nicely
"""
def test_format_nicely():
    cohort = Cohort(1, "Name", "Start Date")
    assert str(cohort) == "Cohort(1, Name, Start Date)"
    

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Name", "Start Date")
    cohort2= Cohort(1, "Name", "Start Date")
    assert cohort1 == cohort2