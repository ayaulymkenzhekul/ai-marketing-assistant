from flask import Flask, render_template, request, Response
from ai_service import stream_marketing

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    product = request.args.get("product", "").strip()

    def event_stream():
        for chunk in stream_marketing(product):
            yield f"data: {chunk}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)
