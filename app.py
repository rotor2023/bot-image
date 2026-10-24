from flask import Flask, render_template, request, jsonify
import urllib.parse, time
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt","").strip()
    if not prompt:
        return jsonify({"error":"kosong"}),400
    safe = urllib.parse.quote(prompt)
    seed = int(time.time()) % 100000
    url = f"https://image.pollinations.ai/prompt/{safe}?width=1024&height=1024&seed={seed}&nologo=true&enhance=true"
    return jsonify({"image_url": url, "prompt": prompt})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
