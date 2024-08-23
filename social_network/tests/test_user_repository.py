from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository #all
We get a list of all users
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection) 
    users = repository.all() 
    assert users == [
        User(1,'test@test.com', 'test'),
        User(2,'trial@trial.com', 'trial'),
        User(3,'tony_hawks@skate.com', 'sk8'),
        User(4,'matt_hoffman@bmx.com', 'bmx')
    ]

"""
When we call UserRepository #find
We receieve a single user based on user_id
"""
def test_get_users_posts(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection) 
    user = repository.find(3)
    assert user == User(3,'tony_hawks@skate.com', 'sk8') 

"""
When we call UserRepository #create
We add a new record(user) to the database
"""
def test_create_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    repository.create(User(None, 'tompidcock@gbcycling.co.uk', "roadcyclist"))
    result = repository.all()
    assert result == [
        User(1,'test@test.com', 'test'),
        User(2,'trial@trial.com', 'trial'),
        User(3,'tony_hawks@skate.com', 'sk8'),
        User(4,'matt_hoffman@bmx.com', 'bmx'),
        User(5, 'tompidcock@gbcycling.co.uk', "roadcyclist")
    ]
"""
When we call UserRepository #delete
We remove a record(user) from the database based on user_id
"""
def test_delete_user(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        User(1,'test@test.com', 'test'),
        User(2,'trial@trial.com', 'trial'),
        User(4,'matt_hoffman@bmx.com', 'bmx'),
    ]

# """When we call UserRepository #update
# We update a record(user)
# """
# def test_update_user(db_connection):
#     db_connection.seed("seeds/social_network.sql") 
#     repository = UserRepository(db_connection)
#     user = repository.find(1)
#     user.email = 'testtest@testtest.com'
#     assert repository.update(user) is None
#     assert repository.all() == [
#         User(1,'testtest@testtest.com', 'test'),
#         User(2,'trial@trial.com', 'trial'),
#         User(3,'tony_hawks@skate.com', 'sk8'),
#         User(4,'matt_hoffman@bmx.com', 'bmx')
# ]             
