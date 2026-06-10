from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/student')
def student():
    return jsonify({
        "name": "James"
    })


@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    return jsonify({
        "message": "Student Added Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)