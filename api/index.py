from flask import Flask, request, send_file,jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image file provided", 400

    file = request.files['image']
    img = Image.open(file)
    img_no_bg = remove(img)

    img_byte_arr = io.BytesIO()
    img_no_bg.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/png')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="Server is running"), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)