# Multilingual Django Site with Chatbot and RAG

This project demonstrates a simple Django application that supports multilingual content, integrates a chatbot using GPT models, and implements a Retrieval-Augmented Generation (RAG) search functionality.

## Features

- Multilingual support (English and French)
- Blog with CRUD operations for articles
- Integration of a chatbot using GPT models
- RAG-based search for blog articles
- Bootstrap 4 theme for UI

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/multilang_site1.git
   cd multilang_site1
2. Create a virtual environment and activate it (optional but recommended):
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Apply database migrations:
    ```bash
    python manage.py migrate
5. Create a superuser (to access Django admin):
    ```bash
    python manage.py createsuperuser
6. Populate the database with initial articles:
    ```bash
    python populate_db.py
7. Start the development server:
    ```bash
    python manage.py runserver

## Usage
- Admin Interface: Navigate to http://localhost:8000/admin/ to manage articles and other site content.
- View Site: Visit http://localhost:8000/ to view the multilingual blog and interact with the chatbot and RAG search.
