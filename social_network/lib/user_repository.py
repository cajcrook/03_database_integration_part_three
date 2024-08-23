from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email_address"], row["username"])
            users.append(item)
        return users

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["email_address"], row["username"])

    def create(self, user):
        self._connection.execute('INSERT INTO users (email_address, username) VALUES (%s, %s)', [user.email, user.username])
        return None
    
    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None
    
    # def update(self, user): 
    #     self._connection.execute('UPDATE users SET email_address = %s, username = %s WHERE id = %s', [user.id, user.email, user.username])

