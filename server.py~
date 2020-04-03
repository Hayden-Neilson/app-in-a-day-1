from flask import Flask, request, render_template
import dict


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/return_info", methods=["POST"])
def return_info():
    if request.method == "POST":
       return "true"


if __name__ == "__main__":
    app.run(debug=True)

