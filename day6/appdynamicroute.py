from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def home(name):
    return f"Hello {name}"

@app.route('/student/<student_name>')
def student(student_name):
    return f"Welcome {student_name}"


if __name__ == '__main__':
    app.run(debug=True)