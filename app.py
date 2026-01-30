from flask import Flask, render_template, request
from ai_service import generate_marketing

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        product = request.form["product"]
        if len(product) > 300:  
            product = product[:300]

        result = generate_marketing(product)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
