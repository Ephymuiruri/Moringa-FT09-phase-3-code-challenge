from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        self._name = name
        self.id = self.add_author_to_db()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if hasattr(self, '_name'):
            raise AttributeError("Author name cannot be changed")
        self._name = name

    def add_author_to_db(self):
        """Create a new Author entry in the database and return the id"""
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
           INSERT INTO authors (name)
           VALUES (?)
           """
        cursor.execute(sql, (self._name,))
        conn.commit()
        author_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return author_id

    @classmethod
    def create_author(cls, name):
        """Create a new Author instance"""
        return cls(name)

    def __repr__(self):
        return f'<Author {self.name}>'
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
           SELECT title
           FROM articles
           WHERE author_id = ?
           """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        titles = [row[0] for row in rows]
        cursor.close()
        return titles
    def magazines(self):
        conn =get_db_connection()
        cursor = conn.cursor()
        sql = """
           SELECT name
           FROM magazines
           WHERE id IN (SELECT magazine_id FROM articles WHERE author_id = ?)
           """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        magazines = [row[0] for row in rows]
        cursor.close()
        return magazines