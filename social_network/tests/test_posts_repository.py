from lib.posts_repository import PostsRepository
from lib.posts import Posts
from lib.user import User

"""
When we call PostsRepository #all
We get a list of all users
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection) 
    posts = repository.all() 
    assert posts == [
        Posts('Blog_1', 'My first blog', 63, 1),
        Posts('Blog_2', 'My sk8 blog', 77, 3),
        Posts('BmxBlog', 'I bmx blog', 99, 4),
        Posts('Blog_trial', 'Blog trial', 20, 2),
    ]

"""
When we call PostsRepository #find
We receieve all posts based on user_id
"""
def test_get_users_posts(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection) 
    posts = repository.find(3)
    assert posts == Posts('Blog_2', 'My sk8 blog', 77, 3)

"""
When we call PostsRepository #create
We add a new record(post) to the database
"""
def test_create_new_post(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection)
    repository.create(Posts('Bikes', 'Lots of bikes', 23, 4));
    result = repository.all()
    assert result == [
        Posts('Blog_1', 'My first blog', 63, 1),
        Posts('Blog_2', 'My sk8 blog', 77, 3),
        Posts('BmxBlog', 'I bmx blog', 99, 4),
        Posts('Blog_trial', 'Blog trial', 20, 2),
        Posts('Bikes', 'Lots of bikes', 23, 4)
    ]

"""
# When we call PostsRepository #delete
# We remove a record(posts) from the database based on user_id
# """
def test_delete_post(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result == [
        Posts('Blog_2', 'My sk8 blog', 77, 3),
        Posts('BmxBlog', 'I bmx blog', 99, 4),
        Posts('Blog_trial', 'Blog trial', 20, 2),
    ]

def test_update_posts(db_connection):
    pass