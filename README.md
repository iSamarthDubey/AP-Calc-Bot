---

# Telegram Arithmetic Progression Bot

This Telegram bot calculates the nth term of an arithmetic progression (AP) based on the values provided by the user.

## Features
- Accepts three inputs: `first_term`, `common_difference`, and `num_terms`.
- Calculates the nth term of the arithmetic progression.
- Provides an interactive interface via Telegram.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Setup](#local-setup)
3. [Hosting on a VPS](#hosting-on-a-vps)
4. [Running the Bot in the Background](#running-the-bot-in-the-background)
5. [Creating a Service for Auto-Restart (Optional)](#creating-a-service-for-auto-restart-optional)
6. [License](#license)

---

## Prerequisites

To set up and run this bot, you will need:
- A Telegram account.
- A bot token from [BotFather](https://core.telegram.org/bots#botfather).
- Python 3.x installed on your local or remote machine.
- Access to a VPS (if deploying the bot on a server).

### Required Python Libraries
Make sure to install the following Python libraries:
```bash
pip install python-telegram-bot --upgrade
```

---

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/telegram-ap-bot.git
cd telegram-ap-bot
```

### 2. Set up the Bot

1. Go to Telegram and create a new bot using **BotFather**. Follow the instructions and obtain the **API token**.
2. Replace `YOUR_API_TOKEN` in `bot.py` with your actual bot token.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: Ensure that you are using `python-telegram-bot` version 20 or higher.

### 4. Run the Bot

```bash
python bot.py
```

Now, your bot should be up and running locally. You can interact with it using the Telegram app.

---

## Hosting on a VPS

To deploy your bot on a VPS and keep it running continuously, follow these steps:

### 1. Set up the VPS

1. Choose a VPS provider such as [DigitalOcean](https://www.digitalocean.com/), [Linode](https://www.linode.com/), or [AWS Lightsail](https://aws.amazon.com/lightsail/).
2. Create a VPS instance and choose an operating system like Ubuntu.
3. SSH into your VPS using:
   ```bash
   ssh root@<your_vps_ip>
   ```

### 2. Install Python and Dependencies

Update your VPS and install Python:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Install the required Python libraries:
```bash
pip3 install python-telegram-bot
```

### 3. Upload the Bot Script

Transfer your bot script (`bot.py`) from your local machine to the VPS using `scp`:
```bash
scp bot.py root@<your_vps_ip>:/home/your_user/
```

### 4. Run the Bot on VPS

Run the bot on your VPS:
```bash
python3 bot.py
```

---

## Running the Bot in the Background

To keep your bot running after disconnecting from the VPS, you can use one of the following options:

### Option 1: `nohup`

`nohup` allows your bot to keep running in the background:
```bash
nohup python3 bot.py &
```

### Option 2: `screen`

`screen` allows you to create a persistent session that you can reconnect to:
1. Install `screen`:
   ```bash
   sudo apt install screen
   ```

2. Create a new screen session:
   ```bash
   screen -S telegram_bot
   ```

3. Run your bot inside the screen:
   ```bash
   python3 bot.py
   ```

4. Detach from the screen (leave it running in the background):
   ```bash
   Ctrl + A, then D
   ```

---

## Creating a Service for Auto-Restart (Optional)

To ensure that your bot restarts automatically after a reboot or crash, you can set up a `systemd` service.

### 1. Create a Service File

Create a new service file:
```bash
sudo nano /etc/systemd/system/telegram_bot.service
```

### 2. Add the Following Configuration

Replace `YOUR_USER` with your VPS username:
```ini
[Unit]
Description=Telegram Arithmetic Progression Bot
After=network.target

[Service]
User=YOUR_USER
WorkingDirectory=/home/YOUR_USER/
ExecStart=/usr/bin/python3 /home/YOUR_USER/bot.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### 3. Enable and Start the Service

1. Reload `systemd` to register the new service:
   ```bash
   sudo systemctl daemon-reload
   ```

2. Enable the service to start on boot:
   ```bash
   sudo systemctl enable telegram_bot.service
   ```

3. Start the service:
   ```bash
   sudo systemctl start telegram_bot.service
   ```

### 4. Check the Status of the Service

Verify that your bot is running:
```bash
sudo systemctl status telegram_bot.service
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Notes:
- Make sure to replace all instances of `YOUR_API_TOKEN`, `YOUR_USER`, and `<your_vps_ip>` with the correct values.
- After running your bot on a VPS, it will remain operational and available for users to interact with on Telegram.

Let me know if you need more assistance!
