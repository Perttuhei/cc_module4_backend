from flask import Flask, request
from flask_cors import CORS
from sentiment import sentiment

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p> Hello world from cc backend! version 2.2<p>"

@app.route('/data', methods=['POST'])
def get_data():
    data = request.json
    response = sentiment(reviewText=data["reviewText"])
    print(response)
    #print(data["name"])
    return {"message": "Data received", "data": data, "sentiment_analysis": response}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)