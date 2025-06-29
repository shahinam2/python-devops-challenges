import psutil
from dotenv import load_dotenv
import os
import requests
import logging

# Configure logging
logging.basicConfig(
    filename='disk_usage_monitor.log',  # Change to '/var/log/disk_usage_monitor.log' for production logging
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

load_dotenv()

def telegram_send_message(message):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}

    try:
        response = requests.post(url, data=payload, timeout=10)
        result = response.json()
        if not result.get("ok"):
            logging.error(f"Failed to send Telegram message: {result}")
        else:
            logging.info("Telegram message sent successfully.")
        return result
    except Exception as e:
        logging.error(f"Exception while sending Telegram message: {e}")
        return None

def get_disk_usage():
    for part in psutil.disk_partitions(all=False):
        try:
            logging.info(f"Checking device: {part.device}")
            usage = psutil.disk_usage(part.mountpoint)
            total = f"{usage.total / (1024 ** 3):.2f} GB"
            used = f"{usage.used / (1024 ** 3):.2f} GB"
            free = f"{usage.free / (1024 ** 3):.2f} GB"
            percent = f"{usage.percent}%"

            if usage.percent > int(os.getenv('DISK_USAGE_THRESHOLD', 80)):
                message = (
                    f"⚠️ Warning: High Disk Usage! ⚠️\n"
                    f"Device: {part.device}\n"
                    f"Mountpoint: {part.mountpoint}\n"
                    f"Total: {total}\n"
                    f"Used: {used}\n"
                    f"Free: {free}\n"
                    f"Percent Used: {percent}\n"
                )
                telegram_send_message(message)
                logging.warning(f"High disk usage on {part.device} ({part.mountpoint}): {percent}")

        except PermissionError:
            logging.error(f"Permission Denied for {part.mountpoint}")

if __name__ == "__main__":
    get_disk_usage()
    logging.info("Disk usage check completed.")
