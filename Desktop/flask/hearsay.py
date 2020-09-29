# installing flask is all you need.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def sort(json):
    sortkeys = json["sortKeys"]
    data = json["payload"]
    response = {}
    for key, value in data.items():
        if key in sortkeys:
            value.sort()
            response.update({key:value})
        else:
            response.update({key:value})

    
    return response

@app.route('/sort', methods=['POST'])
def request_handler():
    req = request.get_json()



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@jau-db.cjnn3otq8vka.us-east-2.rds.amazonaws.com/jau-db'
db = SQLAlchemy(application)

@application.route('/')
def hello_world():
    return 'Hello World'

    

    return jsonify(sort(req)), 200

if __name__ == "__main__":
    app.run(debug=True)