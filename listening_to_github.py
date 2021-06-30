from flask import json
from flask import request
from flask import Flask

#Create flask object
app = Flask(__name__)

#Create a Route
@app.route('/')
def api_root():
    return "Welcome"

#Create 2nd Route
@app.route('/superman')
def helloSuperman():
    return "Hello Superman"


#Create 3nd Route
@app.route('/github', methods=['POST'])
def getMessage():
    if request.headers['Content-Type'] == 'application/json':
        return json.dumps(request.json)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000, debug=True)