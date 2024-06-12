from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self,author,magazine,title,content):
        if not isinstance(author,Article) and not isinstance(magazine,Magazine):
            raise TypeError("Author and Magazine must be of type Author and Magazine")
        self._title = title
        self.content = content
        self.author_id = author.id
        self.magazine_id = magazine.id
        self.id =self.add_Article()
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Article title cannot be changed")
        if not isinstance(title,str) and len(title) >= 5 and len(title) <= 50:
            raise AttributeError('title must be a string and between 5 and 50 characters')
        self._title = title

    def __repr__(self):
        return f'<Article {self.title}>'

    def add_Article(self):
        conn=get_db_connection()
        cursor= conn.cursor()
        """create a new Article entry in the table"""
        sql="""
           INSERT INTO articles (title, content, author_id, magazine_id)
           VALUES (?,?, ?, ?)
           """
        cursor.execute(sql,(self._title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        article_id= cursor.lastrowid
        cursor.close()
        conn.close()
        return article_id
    def get_Author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        """get the author of the Article"""
        sql="""
           SELECT name
           FROM authors
           WHERE id = ?
           """
        cursor.execute(sql,(self.author_id,))
        return cursor.fetchone()[0]
    def get_magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        """get the magazine of the Article"""
        sql="""
           SELECT name
           FROM magazines
           WHERE id = ?
           """
        cursor.execute(sql,(self.magazine_id,))
        return cursor.fetchone()[0]
    @classmethod
    def create_article(cls,author,magazine,title,content):
        """Create a new Article instance"""
        return cls(author,magazine,title,content)
    