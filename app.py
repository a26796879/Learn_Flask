from flask import Flask , jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

application = app
