from flask import Flask, jsonify
from routes import videostream
from routes import overlay

app = Flask(__name__)

@app.route("/")
def Home():
    return jsonify("SAGAR ARORA.")


app.register_blueprint(videostream)
app.register_blueprint(overlay)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
