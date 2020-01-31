from flask import Flask, request, jsonify
app = Flask(__name__)

admin = {
        "email": "admin@admin.com",
        "password": "admin"
    }

admin_email = (list(admin.values())[0])
admin_password = (list(admin.values())[1])


@app.route('/users', methods=['GET'])
def respond():

    return jsonify(admin)


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()

    new_data = json.loads(user_data)

    user_email = new_data["email"]

    return jsonify(user_email)


@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)