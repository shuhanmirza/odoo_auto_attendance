# odoo_auto_attendance
## overview
It's a simple selenium automation implementation. It logs in your account. Then goes to to attendance url and gives attendance and takes a screenshot.

## Prerequisites
- You will need have Python3
- Setup virtualenv and install selenium
```console
your_pc$ virtualenv -p /usr/bin/python3 venv
```
```console
your_pc$ source venv/bin/activate
```
```console
(venv)your_pc$ pip install -r requirements.txt
```
- Have chrome installed
- I used chromedriver for mac.
- download link https://chromedriver.chromium.org/downloads
- Rename env_sample.json to env.json and configure it with your username, password, links and path.

## Running
```console
(venv)your_pc$ python main.py
```

## Process Steps of the bot
- goes to odoo_link
- logs in to your account
- goes to attendance_url
- clicks to to give attendance
- takes a screenshot
