# Project Management Tool

This is a Django-based Project Manager Tool that allows administrators to manage categories and tasks, and assign tasks to users. Regular users can view and complete their assigned tasks.

## Features

- User Registration and Authentication
- Task Creation and Management (Admin)
- Category Creation and Management (Admin)
- Task Assignment to Users
- Task Completion and Status Tracking
- User-Specific Task View
- HTTP-based client-server communication for handling requests and responses

## Target Audience

The Django Task Manager platform is designed to cater to a diverse audience interested in task and project management:

- **Administrators**: Oversee and manage tasks, categories, and user assignments. Ensure the smooth operation of the task management system.
- **Project Managers**: Coordinate and assign tasks to team members, track task progress, and ensure project deadlines are met.
- **Team Members**: View and complete tasks assigned to them, providing updates on task status and collaborating with other team members.
- **Students**: Manage personal projects and study schedules, learning how to organize tasks and manage time effectively.
- **Freelancers**: Keep track of client projects, deadlines, and deliverables, ensuring efficient task management and communication with clients.
- **Educators**: Assign tasks and projects to students, monitor progress, and provide feedback on completed tasks.
- **Small Business Owners**: Organize business tasks, delegate responsibilities to employees, and monitor task completion and productivity.
- **Task Enthusiasts**: Anyone interested in enhancing their productivity through effective task management and organization.

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

# Running Tests

To run tests using pytest, follow these steps:

1. Install pytest if you haven't already:
    ```bash
    pip install pytest
    ```

2. Run pytest:
    ```bash
    pytest
    ```
* Please make sure you do it in the virtual environment *
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
  
## Networking Features

This project uses HTTP for communication between the client (web browser) and the server. This includes:

- Handling user authentication and session management.
- Serving dynamic web pages based on user roles (admin or regular user).
- Processing form submissions for task and category management.
- Fetching and displaying data from the server based on user actions.

  ## Database Usage

- **User Data**: Stores user account information for authentication and personalization.
- **Task Data**: Stores details of tasks including name, category, assigned user, start and end dates, priority, and completion status.
- **Category Data**: Stores task categories for better organization and management.

### Project Structure

- `models.py` - Defines the database schema for categories and tasks.
- `views.py` - Contains the logic for handling user requests and responses.
- `urls.py` - Maps URLs to views.
- `templates/` - Directory for HTML templates.


