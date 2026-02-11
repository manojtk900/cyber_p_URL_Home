from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("phishing.pkl", "rb"))


def clean_url(url):
    if not url:
        return ""
    url = url.strip()
    url = re.sub(r"^https?://(www\.)?", "", url, flags=re.IGNORECASE)
    url = url.rstrip("/")
    return url


def predict_result(cleaned_url):
    try:
        pred = model.predict(vector.transform([cleaned_url]))[0]
    except:
        return {"message": "Something went wrong!", "css_class": "neutral"}

    if pred == "good":
        return {"message": "This website is SAFE!", "css_class": "good"}

    elif pred == "bad":
        return {"message": "This is a PHISHING website!", "css_class": "bad"}

    else:
        return {"message": "Unable to determine!", "css_class": "neutral"}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url", "")
        cleaned = clean_url(url)
        result = predict_result(cleaned)
        return render_template("index4.html", predict=result, submitted_url=url)

    # GET request → load empty page (no previous results)
    return render_template("index4.html", predict=None, submitted_url=None)


if __name__ == "__main__":
    app.run(debug=True)
