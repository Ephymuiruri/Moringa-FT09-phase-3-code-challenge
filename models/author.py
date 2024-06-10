from database.connection import get_db_connection
conn=get_db_connection()
cursor= conn.cursor()
class Author:
    def __init__(self, name):
        self._name = name
        self.id = None
        Author.add_Author(self)
    @property
    def name(self):
        return self.id
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
    @classmethod
    def add_Author(self):
        """create a new Author entry in the table"""
        sql="""
           INSERT INTO authors (name)
           VALUES (?)
           """
        cursor.execute(sql,(self._name,))
        self.id = cursor.lastrowid # Use this to fetch the id of the newly created author
        conn.commit()

    def __repr__(self):
        return f'<Author {self.name}>'
