from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bazinga!</h1><p>Hello from Sheldon’s first Flask app on Azure.</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)