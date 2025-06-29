## Challenge2: Disk Usage Monitor Using psutil

### What problem does it solve?
This script monitors the disk usage of all mounted partitions on your system and sends a notification via Telegram if the disk usage exceeds a specified threshold. It uses the `psutil` library to gather disk usage statistics and the `python-telegram-bot` library to send notifications.

### How It Works
- The script retrieves all mounted disk partitions using `psutil.disk_partitions()`.
- For each partition, it checks the disk usage using `psutil.disk_usage()` and compares it against the specified threshold.
- If the usage exceeds the threshold, it sends a notification to a Telegram chat using the Telegram Bot API.

### Configuration
1. Create a new bot on Telegram by talking to the [BotFather](https://t.me/botfather).
2. Get the bot token from BotFather and set the `TELEGRAM_BOT_TOKEN` environment variable in the `.env` file.
3. Get your chat ID by using the [RawDataBot](https://t.me/RawDataBot) or any other method to find your chat ID, and set the `TELEGRAM_CHAT_ID` environment variable in the `.env` file.
4. Set the `DISK_USAGE_THRESHOLD` environment variable in the `.env` file to specify the disk usage threshold percentage (e.g., 80 for 80%). The default is set to 80%.
5. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
6. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
7. Create a cronjob to run the script periodically (e.g., every 5 minutes):
   ```bash
   */5 * * * * /path/to/venv/bin/python /path/to/main.py
   ```

### Used Modules
- `psutil`: To gather disk usage statistics.
- `os`: To access environment variables.
- `dotenv`: To load environment variables from a `.env` file.
- `requests`: To send HTTP requests to the Telegram Bot API for sending notifications.
- `logging`: To log the script's actions and errors.

###  Notes:
- When creating a telegram bot, use a [uuid](https://www.uuidgenerator.net/version4) for username to avoid conflicts with existing bots.  
Example: `disk_usage_027e2398_bot`.  

- In `psutil.disk_partitions(all=False)`, the `all` parameter controls which partitions are listed:  
`all=False` (default): Only returns physical devices (real disk partitions that are currently mounted).  
`all=True`: Returns all mount points, including pseudo, duplicate, and inaccessible filesystems (like `tmpfs`, `proc`, etc).  
