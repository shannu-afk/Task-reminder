# 📝 Smart Planner

A simple, modern web-based daily planner built with Flask.  
Organize your day by adding tasks, get voice reminders, and manage your schedule with a clean, responsive UI.

---

## 🚀 Features

- **User Registration & Login**  
  Secure authentication with session support.

- **Task Management**  
  - Add tasks with title, time, and duration.
  - View all tasks for the day, displayed neatly.
  - Delete tasks with a single click.
  - Tasks are kept per-user (in-memory for demo).

- **Voice Reminder**  
  - Enable reminders for tasks.  
  - At the scheduled time, your browser will speak the task name 3 times.
  - Task auto-deletes after reminders are finished.

- **Modern UI**  
  - Responsive and mobile-friendly.
  - Clean design with intuitive cards and buttons.

---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/shannu-afk/smart-planner.git
cd smart-planner
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install Flask
```

### 4. Run the app

```bash
export FLASK_APP=app
export FLASK_ENV=development  # Enables debug mode
flask run
```
Or on Windows CMD:
```cmd
set FLASK_APP=app
set FLASK_ENV=development
flask run
```

### 5. Open in your browser

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🗂️ Project Structure

```
smart-planner/
│
├── app/
│   ├── __init__.py
│   ├── routes.py           # All Flask routes, logic
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   └── static/
│       └── style.css       # Styles for auth & base pages
│
├── README.md
└── (venv/)
```

---

## 🛠️ Configuration & Customization

- **Session Secret Key:**  
  Make sure to set a secure `app.secret_key` in your `__init__.py`.

- **In-Memory Storage:**  
  For demo, user and task data are stored in Python dictionaries and will reset when the app restarts.  
  To persist data, connect to a database (e.g., SQLite, PostgreSQL).

- **Voice Reminder:**  
  - Only works on browsers that support the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis).
  - For the reminder to work, the browser tab must be open and have sound enabled.

---

## 👩‍💻 How to Use

1. **Register** for an account.
2. **Log in**.
3. **Add tasks** with a title, time, and duration.
4. See all your tasks on the dashboard.
5. Click the **🔔** reminder button to get a voice notification at the scheduled time.  
   After 3 reminders, the task is automatically deleted.
6. Remove tasks anytime with the **🗑** button.
7. **Logout** securely.

---

## 🔐 Security Note

- This demo uses in-memory storage and is for learning/testing only.
- For production, implement password hashing and persistent storage.
- Always use HTTPS and secure session management in real deployments.

---



---

## 📦 Requirements

- Python 3.7+
- Flask

---

## 🙌 Credits

- UI inspired by modern productivity apps.
- [Flask](https://flask.palletsprojects.com/)
- [Google Fonts – Inter](https://fonts.google.com/specimen/Inter)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## 📝 License

MIT License.  
Feel free to fork, contribute, and improve!

---

> Made with ❤️ for productivity.
