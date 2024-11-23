from flask import Flask, render_template, request, redirect, url_for
from phishing_detector.url_analyzer import validate_url

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        is_valid, message, parsed = validate_url(url)
        result = {
            "is_valid": is_valid,
            "message": message,
            "parsed": parsed,
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
