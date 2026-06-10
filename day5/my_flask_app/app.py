'''
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flask Application"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "Contact us at adkhilal@gmail.com"

@app.route("/profile")
def profile():
    return """
    Name: Hilal <br>
    College : Amal College <br>
    Branch: Bvoc Amal 
    """

if __name__ == "__main__":
    app.run(debug=True)

'''
from flask import Flask, jsonify 
app = Flask(__name__)

@app.route('/student', methods=['GET'])
def student():
    return jsonify({
        "Name": "Hilal",
        "Age": 20,
        "Branch": "Bvoc Mad" 
    })

if __name__ == "__main__":
    app.run(debug=True)