# **🏦 Budgeting App**

### A web application to help users manage their finances, set savings goals, and visualize the impact of non-essential expenses in real time

## **📜 Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## **📌 Introduction**

The **Budgeting App** allows users to track their income, essential expenses, and savings goals, while experimenting with non-essential expenses. This lets users visualize how these additional expenses affect their savings goals over time. The app provides an intuitive and user-friendly interface for managing personal finances.

---

**Project Status:**  
✅ **Backend is fully implemented and deployed on AWS EC2.**  
🚧 **Frontend is still in development.**  

---

## **🚀 Features**

- **Secure User Authentication** – Implements **JWT authentication** for stateless, token-based security.  
- **User Registration & Login** – Encrypted password storage for data privacy.  
- **Manage Budgets** – Users can input income, essential expenses, and set savings goals.  
- **Real-Time Updates** – Dynamic calculations on how non-essential expenses affect savings goals.  
- **Modern API-Driven Architecture** – Fully RESTful backend API.  

---

## **🛠 Tech Stack**

### **Backend (Django)**

- **Django**: Python web framework to handle the backend logic and API requests
- **Django Rest Framework (DRF)**: To create REST APIs for interacting with the frontend
- **PostgreSQL**: Database for production
- **JWT Authentication**: Secure user login

### **Frontend (React) (In Progress)**

- **React.js**: JavaScript library for building the user interface
- **Axios** or **Fetch API**: For making HTTP requests to the Django API

---

## **📥 Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/budgeting-app.git
cd budgeting-app
```
### **2. Backend Setup (Django)**
#### **a. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### **b. Install Python dependencies**

```bash
pip install -r requirements.text
```

#### **c. Apply database migrations**

```bash
python manage.py migrate
```

#### **d. Create a superuser (optional, for admin panel access**

```bash
python maange.py createsuperuser
```

#### **e. Run the Django development server**

```bash
python manage.py runserver
```

### **3. Frontend Setup (React)**
#### **a. Navigate to the frontend folder**

```bash
cd frontend
```

#### **b. Install Javascript dependencies**

```bash
npm install
```

#### **c. Start the React development server**

```bash
npm start
```

### **4. Environmental Variables**
#### Create a `.env` file in the root directory with the following keys:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
```
#### For React, if using environment variables, you can add them in the `frontend/.env` file:
```bash
REACT_APP_API_URL=http://127.0.0.1:8000/api
```

---
## **API Endpoints**

The Django backend exposes RESTful API endpoints for the frontend to interact with. Below are some of the critical endpoints:

### **Authentication**

- **POST** `/api/login/` : User login
- **POST** `/api/register/` : User registration
- **POST** `/api/logout/` : User logout

### **Income**

- **GET** `/api/income/`: Retrieve user's income
- **POST** `/api/income/`: Add or update income

### **Expenses**

- **GET** `/api/expenses/`: Retrieve all expenses
- **POST** `/api/expenses/`: Add a new expense

### **Savings Goals**

- **GET** `/api/savings-goal/`: Retrieve savings goals
- **POST** `/api/savings-goal/`: Add or update savings goals

---
## **Usage**
### **1. Running on the Backend (Django)**
To run the Django server: 
```bash
python manage.py runserver
```
The server will be running at `http://127.0.0.1:8000`.

### **2. Running the Frontend (React)**
To start the React development server:
```bash
npm start
```
The frontend will be running at `http://localhost:3000`.

### **3. Accessing the Application**
Once both the frontend and backend are running, open your browser and navigate to `http://localhost:3000` to start using the app.

---
## **Project Structure**

```plaintext
budgeting-proj/
├── budgeting_backend/           # Django Backend
│   ├── budget/                  # Core functionality app for managing income, expenses, and savings goals
│   ├── budgeting_backend/       # Project settings and URL configurations
│   ├── user_auth/               # Authentication app handling user registration, login, and logout
│   └── manage.py                # Django project entry point
├── frontend/                    # React Frontend
│   ├── src/                     # Frontend source files
│   ├── public/                  # Static assets
│   └── package.json             # Frontend dependencies
├── venv/                        # Virtual environment (not included in version control)
├── requirements.txt             # Python dependencies
└── README.md                    # Project README
```

---

## **🤝 Contributing**

Contributions are welcome! To contribute:

1. Fork the project
2. Create a new feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add a feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

---

## **📜 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **👥 Contact**

For any questions or feedback, feel free to contact us at:
- FrontEnd [sayra6123@gmail.com]
- BackEnd [socheatajpok@gmail.com]








