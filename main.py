
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello World from Google Cloud - Cloud Build Demostration with Approval and Deploy to Cloud Run</h1>"

@app.route("/version")
def version():
  return "<h2>Helloworld 1.0</h2>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
