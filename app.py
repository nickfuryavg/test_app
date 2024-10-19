from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the current time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Get the full name of the user (assuming environment variables or placeholder)
    full_name = "Your Full Name"

    # Get the system username
    system_username = os.getlogin()

    # Get the output of the ⁠ top ⁠ command
    top_output = subprocess.getoutput('top -b -n 1')

    # Generate the response
    response = f"""
    <h2>System Info:</h2>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {system_username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <h3>TOP Output:</h3>
    <pre>{top_output}</pre>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)