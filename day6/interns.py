from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/interns')
def interns():
    intern_list = [
        {
            "name": "Student 1",
            "college": "ABC College"
        },
        {
            "name": "Student 2",
            "college": "XYZ College"
        }
    ]

    return jsonify(intern_list)

if __name__ == '__main__':
    app.run(debug=True)