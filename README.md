# 📱 Phone Number Tracker

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCage API](https://img.shields.io/badge/OpenCage-Geocoding-blue)](https://opencagedata.com/api)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](https://www.docker.com/)

> **A web app to track phone number details, including network provider, time zone, and location, with map visualization.**

---

## ✨ Features

- 🔍 Lookup network provider, time zone, and country for a phone number
- 🗺️ Geolocate the country and display it on a map
- 💾 Download the generated map as an HTML file
- 🖥️ Simple web interface built with Flask

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **Flask**
- **phonenumbers**
- **opencage**
- **folium**
- **python-dotenv**
- **gunicorn** (for production)
- **Docker** (optional)

---

## 🚀 Setup

### 1. Clone the repository

```sh
git clone https://github.com/Zitu-hoq/phone-number-tracker.git
cd phone-number-tracker
```

### 2. Install dependencies

Using [Poetry](https://python-poetry.org/):

```sh
poetry install
```

Or with pip:

```sh
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```
api_key=YOUR_OPENCAGE_API_KEY
DEBUG_MODE=True
```

Get your API key from [OpenCage Geocoding API](https://opencagedata.com/api).

### 4. Run the application

```sh
poetry run python main.py
```

Or with Flask directly:

```sh
export FLASK_APP=main.py
flask run
```

### 5. Using Docker (optional)

Build and run the Docker container:

```sh
docker build -t phonenumbertracker .
docker run -p 8000:8000 phonenumbertracker
```

---

## 💡 Usage

- Open [http://localhost:5000](http://localhost:5000) in your browser.
- Enter a phone number in international format (e.g., `+14155552671`).
- View details and map. Download the map if desired.

---

## 📁 File Structure

```
.
├── main.py              # Flask app
├── Dockerfile           # Docker setup
├── pyproject.toml       # Poetry dependencies
├── poetry.lock
├── .env                 # Environment variables
├── static/
│   └── style.css        # CSS styles
├── templates/
│   └── index.html       # Main HTML template
```

---

## 📄 License

MIT

---

## 👤 Author

Zitu Hoq (<zhzhitu121@gmail.com>)
