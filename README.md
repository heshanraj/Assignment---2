# Assignment---2
Project task manager

# Task Management System

This is a Django-based task management system that allows administrators to manage categories and tasks and assigns tasks to users. Regular users can view and complete their assigned tasks.

## Features

- User Registration and Authentication
- Task Creation and Management (Admin)
- Category Creation and Management (Admin)
- Task Assignment to Users
- Task Completion and Status Tracking
- User-Specific Task View

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/task-management-system.git
    cd task-management-system
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

- **Admin:**
  - Login as the superuser.
  - Manage categories and tasks.
  - Assign tasks to users.

- **Regular User:**
  - Register and log in.
  - View and complete assigned tasks.

### Project Structure

- `models.py` - Defines the database schema for categories and tasks.
- `views.py` - Contains the logic for handling user requests and responses.
- `urls.py` - Maps URLs to views.
- `templates/` - Directory for HTML templates.

### Files in `templates/` Directory

- `category_list.html`
- `category_tasks.html`
- `completed_tasks.html`
- `create_category.html`
- `create_task.html`
- `home.html`
- `login.html`
- `mark_task_complete.html`
- `register.html`
- `task_chart.html`
- `update_task.html`
- `user_task_list.html`

### Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to add detailed information about your changes in the pull request.

### License

This project is licensed under the MIT License.

### Contact

For any questions or suggestions, please contact [your-email@example.com].

---

Thank you for using the Task Management System!
