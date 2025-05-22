from flask import Flask, request, render_template
import socket
import threading
from port_scanner import run_port_scan

app = Flask(__name__)
open_ports = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])

    result = run_port_scan(target, start_port, end_port)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
