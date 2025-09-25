import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Headers for API request
HEADERS = {
    'authority': 'vehicle.cars24.team',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Basic YzJiX2Zyb250ZW5kOko1SXRmQTk2bTJfY3lRVk00dEtOSnBYaFJ0c0NtY1h1',
    'device_category': 'mSite',
    'origin': 'https://www.cars24.com',
    'origin_source': 'c2b-website',
    'platform': 'rto',
    'referer': 'https://www.cars24.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

@app.route("/", methods=["GET"])
def home():
    vnum = request.args.get("vnum")
    if not vnum:
        return jsonify({"error": "Please provide vehicle number using ?vnum=XXXX"}), 400

    url = f"https://vehicle.cars24.team/v1/2025-09/vehicle-number/{vnum}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON received from API"}), 500

if __name__ == "__main__":
    app.run(debug=True)
