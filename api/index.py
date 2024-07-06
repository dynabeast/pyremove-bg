from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve favicon.ico from the static directory
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return "Flask Vercel Example - Hello World from hp side", 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
