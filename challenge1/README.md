## Challenge1: Nginx Monitor Script

### What Problem Does It Solve?
This script monitors the status of the Nginx service on your system and automatically attempts to restart it if it is not running.

### How It Works

- The script checks the status of the Nginx service every 30 seconds using `systemctl is-active nginx`.
- If Nginx is running, it logs this status to `/var/log/nginx_monitor.log` only if the status has changed.
- If Nginx is not running, it logs a warning and attempts to restart the service using `sudo systemctl restart nginx` and logs the action.
- The script handles graceful shutdown on user interruption (Ctrl+C) and logs unexpected errors.

## Used Modules
- `subprocess`: To execute shell commands for checking the service status and restarting it.
- `time`: To implement the delay between checks.
- `logging`: To log the status and actions taken by the script.
- `sys`: To handle system exit and interruptions.

## Usage

1. Make sure you have Python 3 installed.
2. Run the script with sufficient privileges to restart Nginx:
   ```sh
   sudo python3 main.py