from lib.posts import Posts

"""
Test posts are formatted correctly
"""
def test_posts_formatting():
    posts = Posts('title', 'content', 'views', 'user_id')
    assert posts.title == 'title'
    assert posts.content == 'content'
    assert posts.views == 'views'
    assert posts.user_id == 'user_id'

"""
Test format posts to string
"""
def test_posts_to_string():
    posts = Posts('title', 'content', 'views', 'user_id')
    assert str(posts) == "Post(title, content, views, user_id)"

"""
Test to compare two posts and have them be equal
"""
def test_posts_are_equal():
    posts1 = Posts('title', 'content', 'views', 'user_id')
    posts2 = Posts('title', 'content', 'views', 'user_id')
    assert posts1 == posts2




