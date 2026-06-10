from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json
    name = data['name']
    college = data['college']

    return jsonify({
        "Message": "Student added succesfully"
    })

if __name__ == '__main__':
    app.run(debug=True)