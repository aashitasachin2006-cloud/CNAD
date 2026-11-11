import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Pass a sample variable to the HTML template
    return render_template("index.html")

if __name__ == "__main__":
    # Uses the PORT environment variable if deployed to a cloud host, otherwise defaults to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

