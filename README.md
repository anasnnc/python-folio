# Anas NC - Graphic Designer Portfolio

A premium, fully responsive portfolio web application built with the Python Django framework and styled with custom modern Vanilla CSS.

## Features

- **Dynamic Homepage**: Managed completely from the Django admin.
- **Interactive Works Showcase**: High-fidelity projects grid with detailed modal overlays.
- **Glassmorphism Services Grid**: Highlighting competencies and skill bars.
- **AJAX Contact Form**: Modern message submission with interactive client states.
- **Responsive Navigation**: Full mobile support with active toggle animations.

---

## Installation & Local Setup

To run this application locally, follow these steps:

### 1. Clone the repository and navigate to it:
```bash
git clone https://github.com/anasnnc/python-folio.git
cd python-folio
```

### 2. Create and activate a Python virtual environment:
- **Windows**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies:
```bash
pip install django pillow
```

### 4. Run database migrations:
```bash
python manage.py migrate
```

### 5. Seed the database with default Anas NC portfolio data:
```bash
python seed_db.py
```

### 6. Create the administrator account:
```bash
python create_admin.py
```

### 7. Run the development server:
```bash
python manage.py runserver
```

Open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

