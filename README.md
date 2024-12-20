# Level 6 Software Engineering & DevOps Assignment

## Project Overview

This application is designed to demonstrate advanced software engineering and DevOps practices. It integrates various tools and methodologies to ensure efficient development, testing, deployment, and monitoring of software projects. The primary goals of this application are to:

- Implement continuous integration and continuous deployment (CI/CD) pipelines.
- Utilise containerisation technologies such as Docker.
- Apply infrastructure as code (IaC) principles using tools like Terraform.
- Ensure high availability and scalability through render cloud services.
- Monitor application performance and health using monitoring tools.
- Automate testing and deployment processes to reduce manual intervention and errors.

## Functional Operations

The application performs the following functional operations:

- **User Management**: Allows administrators to create, update, and delete user accounts and tickets, as well as manage user roles and permissions.
- **Project Management**: Enables users to manage tickets, including assign tasks to users, updating story points/status, and overall tracking progress.

## Technologies Used

### Backend Development

- **Programming Languages**: Python, JavaScript (Node.js)
- **Frameworks**: Django, Express.js
- **Libraries**: SQLAlchemy, Mongoose, JWT for authentication

### Frontend Development

- **Programming Languages**: JavaScript, TypeScript
- **Frameworks**: React, Angular
- **Libraries**: Redux for state management, Axios for HTTP requests, Material-UI for UI components

## Local Development Setup

### Prerequisites
- Python (v3.9 or higher)
- Docker Desktop
- Git

### Step-by-Step Installation

 **Clone the Repository**
   bash
   git clone https://github.com/jasonpcooke/devopsproject.git
   cd devopsproject

 **Setup**
   bash
   # Python Django setup
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

 **Environment Configuration**
   - Create a `.env` file
   - Copy the contents from `.env.example` files
   - Update the values according to your local setup

The application should now be running at:
- http://'ip':8000
- For database connection issues, verify your PostgreSQL service is running
- Check that all environment variables are properly set e.g. export DATABASE_URL='your database url'

