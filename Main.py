## Reading libraries to use 
from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

@app.route('/health', methods=['GET'])
def health():
    # Return a simple health status
    return jsonify(status="UP"), 200

@app.route('/books', methods=['POST'])
def add_book():
    request_json = request.get_json()
    title = request_json.get('title')
    
    # if not title:
    #     return jsonify({"error": "Title is required"}), 400
    
    book = {'id': len(books) + 1, 'title': title}
    books.append(book)
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def get_books():
    # Return all books as a JSON response
    return jsonify(books), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000)
