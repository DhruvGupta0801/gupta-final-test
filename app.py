from flask import Flask
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror as e:
    logger.error(f"Failed to resolve hostname {hostname}: {e}")
    ip_address = "Unknown"

@app.route('/')
def hello_cloud():
    logger.info("Accessed / route")
    return 'Welcome to Dhruv Gupta Final Test API Server'

@app.route('/host')
def host_name():
    logger.info("Accessed /host route")
    return hostname

@app.route('/ip')
def host_ip():
    logger.info("Accessed /ip route")
    return ip_address

@app.route('/health')
def health_check():
    logger.info("Accessed /health route")
    return 'OK', 200

# Do not run app directly if using gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0')