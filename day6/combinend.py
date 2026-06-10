from flask import Flask, jsonify, request
app = Flask(__name__)

#first student route
@app.route('/student')
def student():
    return jsonify({
        "Name": "Hilal",
        "Age": 18,
        "Branch": "Amal College of Advanced Studies"
    })

#secind route course
@app.route('/course')
def course():
    return jsonify({
        "Course Name": "Bvoc Mobile Application Development",
        "Duration": "4 years"
    })

# Route 3 trainer
@app.route('/trainer')
def trainer():
    return jsonify({
        "name": "Danish",
        "experience": "5 Years"
    })

#4th route add student post
@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    name = data['name']
    college = data['college']

    return jsonify({
        "message": "student added successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)
