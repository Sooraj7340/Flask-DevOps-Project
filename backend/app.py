from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    return jsonify({"message": f"Received {name} with email {email}."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
