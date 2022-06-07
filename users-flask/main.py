from flask import Flask 
from flask_sql



app = Flask(__name__)

@app.route("/")
def home(): 
    return "hello"

if __name__ == "__main__": 
    app.run(port=8000, host="0.0.0.0", debug=True)