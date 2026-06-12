from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "price": 12.99},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear", "year": 2018, "price": 15.99},
    {"id": 3, "title": "Clean Code", "author": "Robert Martin", "year": 2008, "price": 35.00},
    {"id": 4, "title": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999, "price": 40.00},
    {"id": 5, "title": "Deep Work", "author": "Cal Newport", "year": 2016, "price": 14.99}
]
next_id = 6

@app.route('/books', methods = ['GET'])
def get_books():
    if len(books) == 0:
        return jsonify({"message": "No books found"}), 200
    else:
        return jsonify(books), 200

@app.route('/add-book', methods = ['POST'])
def add_books():
    global next_id
    data = request.get_json()
    if "title" not in data or "author" not in data or "year" not in data or "price" not in data:
        return jsonify({"message": "All fields are required"}), 400
    new_book = {
        "id": next_id,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "price": data["price"]
    }
    books.append(new_book)
    next_id += 1
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

@app.route('/search-book/<title>', methods = ['GET'])
def search_books(title):
    results = []
    for book in books:
        if book["title"].lower() == title.lower():
            results.append(book)
    if len(results) == 0:
        return jsonify({"message": "nothing matches your value"}), 404
    else:
        return jsonify(results), 200
        

if __name__ == '__main__':
    app.run(debug=True)