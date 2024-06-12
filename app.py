from database.setup import create_tables
from database.setup import drop_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine


def main():
    # Initialize the database and create tables
    drop_tables()
    create_tables()
    Author1=Author.create_author("Joan")
    Author2=Author.create_author("Emily")
    magazine1=Magazine.create_magazine("National Geographic","Science")
    magazine2=Magazine.create_magazine("Vogue","Fashion")
    article1 =Article.create_article(Author1,magazine1,"The Secrets of the Ocean Trench","The ocean trenches are some of the most mysterious and least explored places on Earth.")
    article2 =Article.create_article(Author2,magazine1,"TThe Latest Trends in Sustainable Fashion","ustainability is becoming an increasingly important concern in the fashion industry.")
    print(article1.get_Author(),article1.get_magazine())
    print(article2.get_Author(),article2.get_magazine())
    print(Author1.articles())
    print(magazine1)
    print(Author1.magazines())
    print(magazine1.articles())
    print(magazine1.contributers())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())

if __name__ == "__main__":
    main()
