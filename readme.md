# Masterblog - Flask Application

A simple and interactive blog application built with Python and the Flask web framework. This project was developed as part of the Backend Development module at Masterschool.

## Features
- **Display Posts**: View a list of all blog posts on the home page.
- **Add Posts**: Create new blog posts with an author, title, and content.
- **Update Posts**: Edit the details of existing posts.
- **Delete Posts**: Remove posts from the blog.
- **Like Posts**: Interactive "Like" button for each blog entry.
- **JSON Storage**: Data is persistently stored in a JSON file.

## Technologies Used
- Python 3
- Flask (Web Framework)
- Jinja2 (Templating Engine)
- HTML/CSS
- JSON (Data Storage)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd masterblog-flask
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000`.

## Project Structure
- `app.py`: Main Flask application logic.
- `posts.json`: File used for data storage.
- `templates/`: HTML templates for the UI.
- `static/`: CSS and image files.

---
Created by S.Zhang
