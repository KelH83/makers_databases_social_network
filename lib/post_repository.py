from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s)', [
                                post.title, post.content, post.views, post.account_id])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["title"], row["content"], row["views"], row["account_id"])
            posts.append(item)
        return posts
    

    def find(self, title):
        rows = self._connection.execute(
            'SELECT * from posts WHERE title = %s', [title])
        row = rows[0]
        return Post(row["title"], row["content"], row["views"], row["account_id"])
    
    # UPDATE
    def update(self, title, views):
        self._connection.execute('UPDATE posts SET views = %s WHERE title = %s', [views, title])
        rows = self._connection.execute('SELECT * FROM posts WHERE title = %s', [title])
        row = rows[0]
        return Post(row["title"], row["content"], row["views"], row["account_id"])
    
    # DELETE
    def delete(self, title):
        self._connection.execute(
            'DELETE FROM posts WHERE title = %s', [title])
        return None