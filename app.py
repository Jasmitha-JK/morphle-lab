from flask import Flask, render_template
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Jasmitha JK"
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output</h2>
    <pre>{top_output}</pre>
    """
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)
