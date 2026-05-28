# Little Lemon Django Web Application

Welcome to the **Little Lemon** restaurant web application! This project is built using Django as part of the Meta Backend Developer Professional Certificate.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, Vanilla CSS, JavaScript (AJAX for booking slot validation)
- **Database**: SQLite

## Setup Instructions

### 1. Set Up Virtual Environment
Ensure you have Python installed, then set up the virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
Ensure Django is installed in your virtual environment:
```bash
pip install django
```

### 3. Run Migrations
Apply database migrations to set up the SQLite database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser
Create an admin account to manage the menu items:
```bash
python manage.py createsuperuser
```

### 5. Run the Server
Launch the development server:
```bash
python manage.py runserver
```
Visit the application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
