# Django Task Manager

This is a Django-based task manager that allows administrators to manage categories and tasks, and assign tasks to users. Regular users can view and complete their assigned tasks.

## Features

- User Registration and Authentication
- Task Creation and Management (Admin)
- Category Creation and Management (Admin)
- Task Assignment to Users
- Task Completion and Status Tracking
- User-Specific Task View
- HTTP-based client-server communication for handling requests and responses

## Networking Features

This project uses HTTP for communication between the client (web browser) and the server. This includes:

- Handling user authentication and session management.
- Serving dynamic web pages based on user roles (admin or regular user).
- Processing form submissions for task and category management.
- Fetching and displaying data from the server based on user actions.

## Getting Started

Follow these steps to set up and run the project locally.

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/heshanraj/Assignment---2.git
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

    Follow the prompts to set up the superuser account.

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

### Usage

To get started with using the application, follow these steps:

1. **Register a Regular User:**
    - Visit the registration page and create a new user account.
    - Log out of this account after registration.

2. **Log in as Superuser:**
    - Use the superuser account created during setup to log in.

3. **Assign Tasks:**
    - Navigate to the task management section and assign tasks to the newly created user.
    - This step is necessary because when a regular user creates an account, their information is stored in the database, allowing the admin to manage and assign tasks to them. 

4. **Regular User:**
    - Log back into the regular user account to view and complete the assigned tasks.

### Project Structure

- `models.py` - Defines the database schema for categories and tasks.
- `views.py` - Contains the logic for handling user requests and responses.
- `urls.py` - Maps URLs to views.
- `templates/` - Directory for HTML templates.


