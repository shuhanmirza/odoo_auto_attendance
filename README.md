# odoo_auto_attendance
Is your HR forcing you to check-in and check-out regularly and you are forgetting this every time?  
I built this out of boredom.
## overview
It's a simple selenium automation implementation. It logs in your account. Then goes to to attendance url and gives attendance.

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
- Rename env_sample.json to env.json and configure it with your username,password and target's username

## Running
You will need to add PATH for geckodriver
```console
(venv)your_pc$ export PATH=$PATH:.
```
```console
(venv)your_pc$ python main.py
```

## Process Steps of the bot
- goes to facebook.com
- logs in to your account
- goes to targets's timeline
- selects latest post
- starts commenting random letters
