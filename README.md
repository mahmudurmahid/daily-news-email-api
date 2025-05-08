# 🗞️ Daily News Email API

The **Daily News Email API** is a Python automation script that fetches the latest tech news headlines from the [NewsAPI](https://newsapi.org) and delivers them directly to your email inbox. This tool is ideal for anyone who wants to stay informed with minimal effort—no apps, no feeds, just news in your inbox.

Perfect for developers, journalists, or anyone wanting a daily summary of current events in technology.

---

## 📑 CONTENTS

- [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [News Formatting](#news-formatting)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Libraries](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [Environment Variables](#environment-variables)
  - [How to Run](#how-to-run)
- [Testing](#testing)
- [Credits](#credits)

---

## 🧠 User Experience (UX)

### User Stories

As a user, I want to:

- Automatically receive a daily tech news summary via email.
- Read only the top 20 relevant headlines with descriptions and links.
- Avoid clutter—just clean, readable information delivered to my inbox.

---

## 🎨 Design

### News Formatting

- **Subject Line:** `"Today's Tech News"`
- **Headline:** Uppercase formatting for easy scanning.
- **Content:** Description of the article and a direct URL link.
- **Email Body:** Plain-text format for maximum compatibility and readability.

---

## 🛠 Features

### Implemented Features

- ✅ Fetches top 20 tech headlines from TechCrunch via NewsAPI.
- ✅ Formats and compiles news into a structured plain-text email.
- ✅ Sends the news using secure SSL email delivery with `smtplib`.
- ✅ Uses `.env` file for safe credential storage.

### Planned Improvements

- 🔄 Add scheduling functionality via `cron` or `schedule` module.
- 🔄 Add more source options or categories.
- 🔄 Enable Markdown or HTML email formatting for richer display.
- 🔄 Add logging for email send status and news fetch results.

---

## 💻 Technologies Used

### Languages Used

- Python 3.13

### Libraries Used

| Library           | Purpose                        |
| ----------------- | ------------------------------ |
| `requests`        | API requests to fetch news     |
| `smtplib` & `ssl` | Secure email sending           |
| `dotenv`          | Load credentials from `.env`   |
| `os`              | Environment variable access    |
| `NewsAPI`         | Source of daily tech headlines |

---

## 📁 Project Files

```bash
.
├── main.py # Main script to fetch news and send email
├── send_email.py # Handles secure email sending via SMTP
├── requirements.txt # Python dependencies
└── .env # (User created) Stores sensitive config values
```

---

## 🚀 Installation & Usage

### Prerequisites

Ensure Python 3 is installed, then install dependencies:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a .env file in the root directory and include the following:

```bash
API_KEY=your_newsapi_api_key
HOST=smtp.your-email-provider.com
PORT=your_smtp_port
USERNAME=your_email_address
PASSWORD=your_email_password
RECEIVER=recipient_email_address
```

### How to Run

Run the script using:

```bash
python main.py
```

This will send an email with the latest tech headlines to the configured recipient.

## ✅ Testing

Manual testing was conducted:

- Confirmed API connection and news data retrieval. ✔
- Validated formatting and encoding of email message. ✔
- Verified email delivery with SSL connection using test SMTP. ✔
- Checked message structure in Gmail and Outlook clients. ✔

## 🧾 Credits

### Code

- Built using Python and NewsAPI.
- Email handling powered by Python’s built-in smtplib and ssl.

### Acknowledgements

- Thanks to NewsAPI for providing a developer-friendly news API.
- Inspired by daily tech briefing newsletters and automation tools.
