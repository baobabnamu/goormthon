from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    resp = requests.get("http://service2:5000/")
    return f"Service1 received: {resp.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
