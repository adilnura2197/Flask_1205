from flask import Flask, render_template

app = Flask(__name__)


title = "Kitoblar olami"
book_name = "Python"
author_name = "Aliyev"
year = 2025


@app.route('/')
def home():
    return render_template('index.html', title=title)

@app.route('/books')
def books():
    return render_template('books.html', book_name=book_name, year=year)

@app.route('/author')
def muallif():
    return render_template('author.html', author_name=author_name)



if __name__ == '__main__':
    app.run(debug=True)
