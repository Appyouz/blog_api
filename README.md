# Personal Blog API

## Description

This project is a RESTful API for managing a personal blog. It allows users to create, read, update, and delete blog articles and tags. The API is built using Django and Django REST Framework, with MySQL as the database.

## Technologies Used

* Python
* Django
* Django REST Framework
* MySQL

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Appyouz/blog_api.git
    cd blog_api/
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file if you haven't already. You can generate it using `pip freeze > requirements.txt` after installing all necessary packages like Django, djangorestframework, mysqlclient, and python-dotenv.)*

4.  **Create the MySQL database:**
    Log in to your MySQL server and create the database:
    ```sql
    CREATE DATABASE <your_database_name_goes_here> CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER '<your_username>'@'localhost' IDENTIFIED BY '<Your_password>';
    GRANT ALL PRIVILEGES ON <your_database_name>.* TO '<your_username>'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
    ```
    *(Adjust the database name, username, and password as per your configuration.)*

5.  **Configure database settings:**
    Create a `.env` file in the root of your project with the following content:
    ```
    DATABASE_ENGINE=django.db.backends.mysql
    DATABASE_NAME=<your_database_name>
    DATABASE_USER=<your_username>
    DATABASE_PASSWORD=<your_password>
    DATABASE_HOST=localhost
    DATABASE_PORT=3306
    DATABASE_CHARSET=utf8mb4
    ```
    Ensure you have `from dotenv import load_dotenv` and `load_dotenv()` at the top of your `mysite/settings.py` file.

6.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Articles

* **`/api/articles/`**
    * `GET`: List all articles.
    * `POST`: Create a new article (requires authentication).
* **`/api/articles/{id}/`**
    * `GET`: Retrieve a specific article by ID.
    * `PUT` / `PATCH`: Update a specific article by ID (requires authentication).
    * `DELETE`: Delete a specific article by ID (requires authentication).

### Tags

* **`/api/tags/`**
    * `GET`: List all tags.
    * `POST`: Create a new tag (requires authentication).
* **`/api/tags/{id}/`**
    * `GET`: Retrieve a specific tag by ID.
    * `PUT` / `PATCH`: Update a specific tag by ID (requires authentication).
    * `DELETE`: Delete a specific tag by ID (requires authentication).

## Authentication

The API uses Token Authentication. To access protected endpoints (like creating, updating, or deleting articles and tags), you need to include a valid token in the `Authorization` header of your request.

You can obtain a token for a user through the Django admin interface:

1.  Log in to the admin panel (usually at `/admin/`).
2.  Navigate to the "Auth Token" section.
3.  Create a new token for the desired user.
4.  Include the token in your request headers as `Authorization: Token YOUR_TOKEN_HERE`.

## Filtering

### Articles

You can filter articles using query parameters in the `/api/articles/` endpoint:

* **`publication_date`**: Filter articles by a specific publication date (e.g., `?publication_date=2025-04-14`).
* **`tags`**: Filter articles by one or more tags (e.g., `?tags=python` or `?tags=python,django`).
