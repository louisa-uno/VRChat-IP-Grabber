import logging
import requests
from flask import Flask, jsonify, send_file, request, redirect
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# Configure logging
logging.basicConfig(level=logging.INFO)

def filenamebylogs_id(logs_id):
    if logs_id is None:
        filename = "logs.txt"
    else:
        filename = f"logs_{logs_id}.txt"
    return filename

def fileexists(logs_id):
    try:
        with open(filenamebylogs_id(logs_id), "r") as f:
            pass
    except FileNotFoundError:
        return False
    return True

def log(string, logs_id=None):
    filename = filenamebylogs_id(logs_id)
    if not fileexists(logs_id) and not "ip-lookup" in string:
        log("IP-Lookup: https://www.iplocation.net/ip-lookup", logs_id=logs_id)
    
    logging.info(string)
    line = datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ": " + string + "<br>"
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(line)
    

@app.route('/health')
def health_check():
    # TODO: Perform some regular health functions
    return jsonify({'status': 'OK'})

@app.route('/whatsmyip', methods=['GET'])
def get_ip():
    # Get the original client IP address from the X-Forwarded-For header
    client_ip = request.headers.get('X-Forwarded-For')  
    return jsonify({'ip': client_ip})

@app.route('/<ignore>.mp4', methods=['GET'])
def grabme(ignore=None):
    return get_video(grabme=True)

@app.route('/logs')
def get_logs():
    # Get the 'v' parameter from the original URL's query string
    logs_id = request.args.get('v')
    filename = filenamebylogs_id(logs_id)
    try:
        with open(filename, 'r') as f:
            logs = f.read()
    except FileNotFoundError:
        return "Logs not found."
    return logs

@app.route('/watch')
@app.route('/<ignore1>:/<ignore2>/<ignore3>')
def get_video(grabme=False, ignore1=None, ignore2=None, ignore3=None):
    if grabme:
        logs_id = None
    else:
        video_id = request.args.get('v')
        logs_id = hash(video_id)
        
    if not fileexists(logs_id):
        if grabme:
            log("Just put https://cdnapp.de/grabme.mp4 into a video player and reload this page.", logs_id=logs_id)
        else:
            log(f"Just put https://cdnapp.de/watch?v={video_id} into a video player and reload this page.", logs_id=logs_id)
            return redirect(f"/logs?v={logs_id}")
    
    # Get the original client IP address from the X-Forwarded-For header
    client_ip = request.headers.get('X-Forwarded-For')
    if not client_ip:
        client_ip = request.remote_addr
        
    if client_ip == requests.get('https://cdnapp.de/whatsmyip').json()['ip']:
        log(f'Original client IP: THE SERVER ITSELF', logs_id=logs_id)
    else:
        log(f'Original client IP: {client_ip}', logs_id=logs_id)

    if grabme:
        return send_file('grabme.mp4', as_attachment=True)
    else:
        return redirect(f'https://www.youtube.com/watch?v={video_id}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3926)
