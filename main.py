from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("NAME", "World")  # Default to "World" if NAME is not set
    return f"<h1>Hello {name} from Google Cloud - Cloud Build + Cloud Deploy</h1>"

@app.route("/version")
def version():
    return "<h2>Helloworld 1.0</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
