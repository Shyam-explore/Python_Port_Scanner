# 🔍 Python Port Scanner (Flask Web App)

A lightweight, web-based network reconnaissance tool that scans open TCP ports on a given IP address or domain using Python's socket programming and multi-threading. Built with Flask, it provides a simple user interface for entering a target and port range.

---

## 🚀 Features

- 🌐 Web UI using Flask & HTML (Jinja2 templates)
- 🔧 Accepts both IP addresses and domain names
- 🔍 Customizable TCP port range for scanning
- ⚡ Fast concurrent scanning using Python’s `threading`
- 📄 Displays open ports with common service names
- 🛡️ Demonstrates Nmap-like behavior using basic socket programming

---

## 📁 Project Structure
```bash
flask-port-scanner/
├── app.py # Main Flask app
├── port_scanner.py # Port scanning logic using socket and threading
├── templates/
│ └── index.html # Web UI form + result output
├── static/
│ ├── css/
│ │ └── style.css # (Optional) Stylesheet
│ └── js/
│ └── script.js # (Optional) JavaScript
├── requirements.txt # Required Python packages
└── README.md # Project documentation
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-port-scanner.git
cd flask-port-scanner
```
### 2. Create a Virtual Environment
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
 ```bash
pip install -r requirements.txt
```
### 4. Run the App
 ```bash
python app.py
```
### 5. Open in Browser
Visit: 
```bash 
 http://localhost:5000
 ```
-------

## ⚠️ Disclaimer
This project is intended for educational purposes only.
Use it only on systems and networks you own or have permission to scan.
Unauthorized port scanning can be illegal and unethical.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests and feedback are welcome! If you find a bug or want to suggest a feature, feel free to open an issue.

