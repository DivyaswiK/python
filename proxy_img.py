from flask import Flask, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/proxy_image', methods=['GET'])
def proxy_image():
    url = request.args.get('url')
    try:
        response = requests.get(url,timeout=20)
        response.raise_for_status()
        return send_file(BytesIO(response.content), mimetype='image/jpeg')
    except Exception as e:
        return {"error": str(e)}, 500
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)