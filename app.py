from flask import Flask, render_template, request, jsonify
from ai_engine import get_ai_response

app = Flask(__name__)

# -------------------------------
# ROUTES
# -------------------------------

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/ai-stylist", methods=["GET", "POST"])
def ai_stylist():
    if request.method == "POST":
        user_input = request.form.get("query")
        response = get_ai_response(user_input)
        return jsonify(response)

    return render_template("ai_stylist.html")
# -------------------------------
# RUN APP
# -------------------------------
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)