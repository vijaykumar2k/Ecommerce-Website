
# Django E-commerce Project

## Overview
This project is a fully functional e-commerce website developed using Django. It provides functionalities such as user registration, product management, and data handling through FastAPI.

## Features
- **User Authentication:** Allows users to register, log in, and manage their accounts.
- **Product Management:** CRUD operations for products, including adding, editing, and deleting products.
- **FastAPI Integration:** Utilizes FastAPI for data insertion and patching in the database.
- **Search Functionality:** Enables users to search for products based on various criteria.
- **User Profiles:** Displays user profiles with order history (if implemented).
- **Frontend:** HTML, CSS, JavaScript for frontend development.
- **Database:** MySQL for data storage and management.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. Create and activate a virtual environment:
   ```bash
   virtualenv env
   .\env\Scripts\activate  # On Windows
   source env/bin/activate  # On macOS/Linux
3. Install dependencies
   ```bash
   Copy code
   pip install -r requirements/requirements.txt
4. Set up the database:
   ```bash
   Copy code
   python manage.py makemigrations
   python manage.py migrate
5. Start the Django development server:
   ```bash
   Copy code
   python manage.py runserver
6. Access the application in your web browser at http://localhost:8000.



## Usage
- **Admin Panel:** Access the Django admin panel at http://localhost:8000/admin to manage users, products, and other site content.
- **API Documentation:** View FastAPI documentation for data handling and management.
##Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
