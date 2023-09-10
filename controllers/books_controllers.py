from flask import render_template, Blueprint, redirect, request
from models.books import books, add_new_book, remove_book
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    return render_template("index.jinja", title="Book List", books=books)

# version_1
@books_blueprint.route("/books/<index>")
def show(index):
    selected_book = books[int(index)]
    return render_template("summary.jinja", book=selected_book)
    
#version_2 (attributes are nonvisible)
# @books_blueprint.route('/books/<title>')
# def show(title):
#   selected_book = title
#   return render_template('summary.jinja', book=selected_book)



@books_blueprint.route("/books", methods=["POST"])
def new_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    book_summary = request.form["summary"]
    new_book = Book(book_title, book_author, book_genre, book_summary)
    add_new_book(new_book)
    return redirect('/books')


#remove book by title
# @books_blueprint.route("/books/delete/<title>", methods=["POST"])
# def remove_book(title):
#     remove_book_by_title(title)
#     return redirect("/books")


@books_blueprint.route("/books/delete/<index>", methods=["POST"])
def trash_book(index):
    remove_book(index)
    return redirect("/books")

    