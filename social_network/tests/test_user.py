from lib.user import User

"""
Test user constructs correctly
"""

def test_user_constructs_correctly():
    user = User(1, "My Email", "My Username")
    assert user.id == 1
    assert user.email == "My Email"
    assert user.username == "My Username"

"""
Test format user to a string nicely
"""
def test_user_formats_to_string():
    user = User(1, "My Email", "My Username")
    assert str(user) == "User(1, My Email, My Username)"

"""
Test to compare two users and have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "My Email", "My Username")
    user2 = User(1, "My Email", "My Username")
    assert user1 == user2   
