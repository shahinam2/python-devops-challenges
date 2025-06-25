import subprocess
import time
import logging
import sys

CHECK_INTERVAL = 30  # Check every 30 seconds

# Configure logging
logging.basicConfig(
    filename='/var/log/nginx_monitor.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def check_nginx():
    nginx_status = subprocess.run(['systemctl', 'is-active', 'nginx'], capture_output=True, text=True)
    return nginx_status.returncode

def restart_nginx():
    result = subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], capture_output=True, text=True)
    return result.returncode, result.stderr

def main():
    last_status = None
    while True:
        status = check_nginx()
        if status == 0:
            if last_status != 0:  # Only log if the status has changed.
                logging.info("Nginx is running")
            last_status = 0
        else:
            if last_status != status:
                logging.warning("Nginx is not running")
            logging.info("Attempting to restart Nginx...")
            returncode, stderr = restart_nginx()
            if returncode == 0:
                logging.info("Nginx restarted successfully")
            else:
                logging.error(f"Failed to restart Nginx: {stderr.strip()}")
            last_status = status
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful shutdown on user interrupt
        logging.info("Nginx monitor stopped by user.")
        sys.exit(0)
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
        sys.exit(1)