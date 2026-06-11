from flask import Flask, jsonify, request

app = Flask(__name__)

students =[
    {"id": 1,
    "name": "Hilal",
    "age": 18,
    "college": "Amal College",
    "branch": "Bvoc Mad"},

    {"id": 2,
    "name": "Danish",
    "age": 19,
    "college": "Amal College",
    "branch": "Bvoc Mad"
    },

    {"id": 3,
    "name": "Abhaj",
    "age": 19,
    "college": "Amal College",
    "branch": "Bvoc Mad"
    },

    {"id": 4,
    "name": "Salman",
    "age": 19,
    "college": "Amal College",
    "branch": "Bvoc Mad"
    },

    {"id": 5,
    "name": "Shaham",
    "age": 19,
    "college": "Amal College",
    "branch": "Bvoc Mad"
    },
    ]

next_id = 6

@app.route('/students', methods=['GET'])
def get_students():
    if len(students) == 0:
        return jsonify({"message": "The list is empty"}), 200
    else:
        return jsonify(students), 200
    


@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    id = int(id)
    for student in students:
        if student["id"] == id:
            return jsonify(student), 200
    return jsonify({
        "message": "Could not find matching data"
    }), 404

@app.route('/add-student', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    if "name" not in data or "age" not in data or "college" not in data or "branch" not in data:
        return jsonify({"message": "All fields are required"}), 400
    new_student = {
        "id": next_id,
        "name": data["name"],
        "age": data["age"],
        "college": data["college"],
        "branch": data["branch"]
    }
    students.append(new_student)
    next_id += 1
    return jsonify({"message": "Student Added Successfully", "student": new_student}), 201

@app.route('/search-student/<name>', methods = ['GET'])
def search_student(name):
    results = []
    for student in students:
        if student["name"].lower() == name.lower():
            results.append(student)
    if len(results) == 0:
        return jsonify({"message": "nothing matches your value"}), 404
    else:
        return jsonify(results), 200


@app.route('/delete-students/<id>', methods=['DELETE'])
def remove_student(id):
    id = int(id)
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            }), 200
    return jsonify({
        "message": "Could not find matching data"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
    