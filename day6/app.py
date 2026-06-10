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