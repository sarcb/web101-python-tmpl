from flask import Flask, render_template, request
import math, os

app = Flask(__name__)

@app.route("/")
@app.route("/submit")
def index():
    return render_template("pizza.html", name="PythonBot", areaA="0", areaB="0", ratio="0")

# Add your /submit route here

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
