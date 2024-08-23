from lib.posts import Posts

class PostsRepository():
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Posts(row["title"], row["content"], row["views"], row["user_id"])
            posts.append(item)
        return posts

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE user_id = %s', [user_id])
        row = rows[0]
        return Posts(row["title"], row["content"], row["views"], row["user_id"])

    def create(self, posts):
        self._connection.execute('INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)', [posts.title, posts.content, posts.views, posts.user_id])
        return None
    
    def delete(self, user_id):
        self._connection.execute('DELETE FROM posts WHERE user_id = %s', [user_id])
        return None
    
    def update(self,):
        pass
