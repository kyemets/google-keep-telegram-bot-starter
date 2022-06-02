# Google keep telegram bot starter based on [aiogram](https://aiogram.dev/) and [gkeepapi](https://github.com/kiwiz/gkeepapi)  
---

# About 
Create and send notes in telegram bot to Google Keep

# Installation
1. Clone this repo: `git clone https://github.com/kyemets/gkeep-bot-starter`
2. Install [Aiogram](#aiogram)
3. Install [gkeepapi](#gkeepapi)

# aiogram
## Using PIP

> `$ pip install -U aiogram`

## Using Pipenv

> `$ pipenv install aiogram`

## Using Pacman

_aiogram_ is also available in Arch Linux Repository, so you can install this framework on any Arch-based distribution like Arch Linux, Antergos, Manjaro, etc. To do this, just use pacman to install the [python-aiogram](https://archlinux.org/packages/community/any/python-aiogram/) package:

> `$ pacman -S python-aiogram`



# gkeepapi 
## Installation

> `pip install gkeepapi`

## Create an app password
1.  Enable 2-step authentication in your Google settings.
2.  Create an app password here: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3.  Choose for the app `other`, I named it `gkeepapi` and I generated a password.
4.  I user the generated password in the scrip instead of my Google password.

# Local launch

1. Install dependencies with `requirements.txt`
2. Run `python bot.py`

---

# Environment variables
- `TOKEN` — Telegram bot token
- `email` — Google account email
- `password` — Generated google app password
