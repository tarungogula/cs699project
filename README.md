# Course Management Web Application

## Overview
This project is a comprehensive web application developed as part of the **CS 699: Software Lab** course under the guidance of **Prof. Bhaskaran Raman** (Aug’23-Nov’23). The application is designed to streamline the process of course management, enabling educators to create, modify, and manage courses with ease. The project is built using Django for the backend, with a front-end powered by JavaScript, HTML, and CSS, and PostgreSQL as the database.

## Features
- **Course Creation**: Educators can create new courses by providing essential details such as course name, description, syllabus, and schedule.
- **Course Modification**: Courses can be modified, allowing updates to the course content, schedule, or any other relevant information.
- **Course Management**: Admin users can manage all the courses, including viewing, editing, and deleting existing courses.
- **Student Enrollment**: Students can enroll in courses, view course content, and access other resources provided by the educators.
- **User Authentication**: Secure login and registration system for both educators and students.

## Tech Stack
- **Backend**: Django
- **Frontend**: JavaScript, HTML, CSS
- **Database**: PostgreSQL
- **Deployment**: Configured to be deployed on any standard web server with PostgreSQL support.

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL 12.x or higher
- Node.js (for JavaScript package management)
- Git

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/course-management-app.git
    cd course-management-app
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:
   - Create a new PostgreSQL database:
     ```bash
     sudo -u postgres psql
     CREATE DATABASE course_management_db;
     CREATE USER yourusername WITH PASSWORD 'yourpassword';
     GRANT ALL PRIVILEGES ON DATABASE course_management_db TO yourusername;
     ```

   - Update the database settings in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'course_management_db',
             'USER': 'yourusername',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
   Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

### Educators
- **Login**: Access the educator's dashboard by logging in with your credentials.
- **Create a Course**: Use the "Create Course" feature to add new courses to the system.
- **Modify a Course**: Edit existing courses to update details like course name, description, and schedule.
- **Manage Courses**: View and manage all courses, including student enrollment and course content.

### Students
- **Register/Login**: Create an account or log in to view available courses.
- **Enroll in Courses**: Browse and enroll in courses offered by educators.
- **Access Course Material**: View course content, including lecture notes, assignments, and schedules.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## Acknowledgments
- **Instructor**: Prof. Bhaskaran Raman, for providing guidance and support throughout the development of this project.
- **Course Material**: The concepts and skills learned in the CS 699: Software Lab course were instrumental in building this application.
