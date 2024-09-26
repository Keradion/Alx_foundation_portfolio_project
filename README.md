
# 🌟 **Mezgebe Expense Tracker (CRUD Application)** 🌟

> 🚀 **Track, manage, and manipulate your daily expenses with ease** using this web-based CRUD application, featuring secure user authentication and password reset functionalities!

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python) ![Flask](https://img.shields.io/badge/Flask-1.1.2-green?style=for-the-badge&logo=flask) ![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)

---

## 📑 **Table of Contents**

- [📖 Introduction](#introduction)
- [🌐 Deployed Site](#deployed-site)
- [✨ Features](#features)
- [⚠️ Challenges & Solutions](#challenges--solutions)
- [💻 Technologies Used](#technologies-used)
- [🚀 Deployment Details](#deployment-details)
- [🧑‍💻 Author & Contact](#author--contact)
- [⚙️ Installation](#installation)
- [🚦 Usage](#usage)
- [🔗 Contributing](#contributing)
- [📜 License](#license)

---

## 📖 **Introduction**

The **Mezgebe Expense Tracker** is a 🌐 **web-based CRUD application** designed to help users manage their daily expenses with ease. It offers:
- Secure user login/logout with 🛡️ token-based password reset.
- Full CRUD (Create, Read, Update, Delete) functionalities for managing expenses.
- A simple, yet powerful dashboard for a smooth and responsive user experience.  

Developed by **Daniel Berihun**, this application features a robust backend and focuses on **Backend Engineering** using **Flask**. 🧑‍💻

---

## 🌐 **Deployed Site**

Check out the live application here:  
🔗 [**yourdanatalx.tech**](http://yourdanatalx.tech)

---

## ✨ **Features**

🎯 **User Authentication**:  
🔐 Secure registration, login, and password reset system powered by Flask-Login and Flask-Bcrypt.

📊 **Expense Dashboard**:  
Create, track, update, and delete expenses by amount, reason, and date — all from a user-friendly dashboard.

📧 **Email Password Reset**:  
Forgot your password? No worries! Reset it with a token-based link sent to your email.

📱 **Responsive Design**:  
The app is fully responsive and works across devices for a seamless experience.

---

## ⚠️ **Challenges & Solutions**

💡 **Password Reset via Email**  
I faced issues when integrating Flask-Mail with Gmail to send password reset tokens due to Google’s policy changes. Flask-Mail didn’t accept standard passwords, causing email failures.

### 🛠️ **Solution**:  
After searching through **StackOverflow** and community forums, I learned that Gmail now requires **App Passwords** instead of standard account passwords. I generated a **16-character App Password**, and successfully implemented the password reset feature!

For more details, check out this StackOverflow post: [**Flask-Mail and Gmail App Passwords**](https://stackoverflow.com/questions/66211708/how-to-send-an-email-with-flask-mail-from-a-bussiness-acount)

---

## 💻 **Technologies Used**

**Backend**:  
- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python**: Core programming language.  
- ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) **Flask**: Micro web framework for building the application.  
- ![Flask-Mail](https://img.shields.io/badge/-Flask_Mail-E34F26?style=flat-square&logo=gmail&logoColor=white) **Flask-Mail**: To send email notifications for password resets.  
- ![Flask-SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-8B0000?style=flat-square&logo=sqlite&logoColor=white) **SQLAlchemy**: ORM used for managing the database.

**Frontend**:  
- **HTML/CSS**: For web structure and styling.  
- ![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white) **Bootstrap**: For responsive design.

**Database**:  
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) **SQLite**: For data storage.

---

## 🚀 **Deployment Details**

🛠️ The application was deployed on an **Ubuntu server** using **Nginx** for static file serving and **Gunicorn** for serving the Python app. **Supervisor** was employed to keep the app running smoothly in the background.

### Key Components:
- **Nginx**: A web server used to handle requests and serve static files.
- **Gunicorn**: A WSGI server used to serve the Flask application.
- **Supervisor**: Ensures the application stays running even when the server restarts.

---

## 🧑‍💻 **Author & Contact**

👨‍💻 I’m **Daniel Berihun**, currently a Software Engineering student at **ALX Africa**, specializing in **Backend Engineering**.  
I’m passionate about backend development and eager to build more robust web applications!

💼 **LinkedIn**: [Daniel Berihun](https://www.linkedin.com/in/daniel-berihun-43126224a/)  
🔗 **GitHub**: [Keradion](https://github.com/Keradion/Alx_foundation_portfolio_project)  
🌐 **Project Page**: [yourdanatalx.tech](http://yourdanatalx.tech)

Feel free to reach out with feedback, suggestions, or any advice on my tech journey!

---

## ⚙️ **Installation**

### Prerequisites:
- Python 3.8+
- Pip
- Virtual Environment (recommended)

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Keradion/Alx_foundation_portfolio_project.git
   cd Alx_foundation_portfolio_project
   ```

2. **Set up a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file with the following content:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   ```

5. **Run the application**:
   ```bash
   flask run
   ```

The app will run locally on `http://127.0.0.1:5000/`.

---

## 🚦 **Usage**

Once the application is up and running, you can:
- Create an account, log in, and manage your expenses.
- Add, edit, or delete expenses directly from the dashboard.
- Use the password reset functionality if you forget your password.

---

## 🔗 **Contributing**

Contributions are always welcome! 🎉

To contribute:
1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 📜 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

