import socket
import threading

def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            open_ports.append((port, service))
        sock.close()
    except:
        pass

def run_port_scan(target, start_port, end_port):
    open_ports = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return "Invalid host!"

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if open_ports:
        result = "<h3>Open Ports:</h3><ul>"
        for port, service in sorted(open_ports):
            result += f"<li>Port {port}: {service}</li>"
        result += "</ul>"
        return result
    else:
        return "No open ports found."
