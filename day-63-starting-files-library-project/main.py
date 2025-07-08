from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title} by {self.author}, rating: {self.rating}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
# with app.app_context():
#     new_book = Book(title="jk", author="K. K. Test", rating=9.9)
#     db.session.add(new_book)
#     db.session.commit()

# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#
#     for book in all_books:
#         print(book)
#
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()



# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("""
# # CREATE TABLE IF NOT EXISTS books (
# #     id INTEGER PRIMARY KEY,
# #     title varchar(250) NOT NULL UNIQUE,
# #     author varchar(250) NOT NULL,
# #     rating FLOAT NOT NULL
# # )
# # """)
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


all_books = []


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html" , books = all_books)


@app.route("/add" , methods=["GET","POST"])
def add():
   if request.method == "POST":
       new_book = Book(
           title = request.form['title'],
           author = request.form['author'],
           rating = float(request.form['rating'])
       )
       db.session.add(new_book)
       db.session.commit()
       return redirect(url_for('home'))
   return render_template("add.html")

@app.route('/edit/<int:book_id>', methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book,book_id)
    if request.method == "POST":
        book.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book=book)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

