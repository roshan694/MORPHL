from flask import Flask
import os
import datetime
import subprocess
import platform
app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "K ROSAN SINGHA"
    username = os.getlogin()
    ist_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
    if platform.system() == "Windows":
        top_output = subprocess.getoutput('powershell -Command "Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 10"')
    else:
        top_output = subprocess.getoutput("top -b -n 1")
    return f"""
    <h1>System Monitor</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
