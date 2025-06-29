
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello World from Google Cloud - Cloud Build Demostration</h1>"

@app.route("/version")
def version():
  return "Helloworld 1.0\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
