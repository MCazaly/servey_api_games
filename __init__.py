from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Internal API!"
if __name__ == "__main__":
    app.run()

