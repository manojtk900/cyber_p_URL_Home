from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import pickle
import re
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("FLASK_SECRET", "replace_this_with_real_secret")

# Load vectorizer and model (same filenames as before)
vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("phishing.pkl", "rb"))


def clean_url(input_url: str) -> str:
    """
    Basic cleaning of URL before vectorizing:
    - remove scheme (http/https) and leading www.
    - strip whitespace
    """
    if not input_url:
        return ""
    u = input_url.strip()
    # remove protocol and www
    u = re.sub(r"^https?://(www\.)?", "", u, flags=re.IGNORECASE)
    # remove trailing slash
    u = u.rstrip("/")
    return u


def predict_url_status(cleaned_url: str) -> dict:
    """
    Run model prediction and return structured result.
    """
    try:
        pred = model.predict(vector.transform([cleaned_url]))[0]
    except Exception as e:
        # In case model fails, return error structure
        return {"status": "error", "label": "error", "message": f"Prediction failed: {e}"}

    if pred == "bad":
        return {"status": "malicious", "label": "Malicious", "message": "This is a MALICIOUS website!"}
    elif pred == "good":
        return {"status": "safe", "label": "Safe", "message": "This website looks safe."}
    else:
        return {"status": "unknown", "label": "Unknown", "message": "Unable to determine website safety."}


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the main UI. Supports form POST and displays result in the page.
    """
    result = None
    submitted_url = None

    if request.method == "POST":
        submitted_url = request.form.get("url", "")
        cleaned = clean_url(submitted_url)

        if not cleaned:
            flash("Please enter a valid URL.", "warning")
            return redirect(url_for("index"))

        result = predict_url_status(cleaned)

        # Optionally, add a friendly flash for errors
        if result["status"] == "error":
            flash(result["message"], "danger")

    return render_template(
        "index2.html",
        predict=result,       # dict with status, label, message (or None)
        submitted_url=submitted_url
    )


@app.route("/api/check", methods=["POST"])
def api_check():
    """
    JSON API endpoint to check a URL. Accepts JSON: {"url": "https://..."}
    Returns JSON: {"status": "safe"|"malicious"|"unknown"|"error", "label": "...", "message": "..."}
    """
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"status": "error", "message": "Missing 'url' in JSON body."}), 400

    raw_url = data.get("url", "")
    cleaned = clean_url(raw_url)
    if not cleaned:
        return jsonify({"status": "error", "message": "Invalid or empty URL provided."}), 400

    result = predict_url_status(cleaned)
    return jsonify(result), 200


@app.route("/health", methods=["GET"])
def health():
    """
    Simple health endpoint for quick checks.
    """
    return jsonify({"status": "ok", "model_loaded": True}), 200


if __name__ == "__main__":
    # Use host=0.0.0.0 only if you want to expose app externally (e.g., Docker)
    app.run(debug=True, port=5000)
