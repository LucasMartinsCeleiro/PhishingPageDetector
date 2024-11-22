from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page with a URL input form."""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Analyze the provided URL for phishing indicators."""
    url = request.form["url"]
    # Placeholder for analysis logic
    result = f"Analyzing: {url}"
    return render_template("result.html", url=url, result=result)


if __name__ == "__main__":
    app.run(debug=True)
