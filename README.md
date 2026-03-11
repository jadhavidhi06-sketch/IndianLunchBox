# IndianLunchBox
IndianLunchBox is a full-stack web application built with React.js and Django that connects users with authentic homemade Indian meals. The platform allows users to browse lunchboxes, place orders, manage subscriptions, and experience traditional Indian home-cooked food digitally.

🍱 IndianLunchBox

IndianLunchBox is a modern full-stack web platform designed to connect users with healthy, homemade Indian meals prepared by local home chefs and tiffin providers.

The platform enables customers to browse menus, order lunchboxes, manage subscriptions, and track deliveries, while vendors can manage meals, orders, and availability through a dashboard.

This project is developed as a Blackbook Project using modern web technologies.

🚀 Project Overview

Many people living away from home struggle to find healthy, affordable, and authentic home-style food. IndianLunchBox aims to solve this problem by providing a platform where users can easily subscribe to daily homemade meals prepared by local vendors.

The platform focuses on:

Healthy home-cooked meals

Easy subscription-based lunch services

Vendor management system

Seamless ordering experience

🏗️ Tech Stack
Frontend

⚛️ React.js

Bootstrap / CSS

Axios

React Router

Backend

🐍 Django

Django REST Framework

MySQL Database

Django Authentication System

Other Tools

Git & GitHub

REST API

JSON Data Exchange

📂 Project Structure
IndianLunchBox
│
├── frontend (React)
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   │   ├── Home
│   │   │   ├── Menu
│   │   │   ├── Login
│   │   │   ├── Register
│   │   │   ├── Cart
│   │   │   ├── Orders
│   │   ├── services
│   │   ├── App.js
│   │   └── index.js
│
├── backend (Django)
│   ├── indianlunchbox
│   ├── api
│   ├── users
│   ├── orders
│   ├── menu
│   ├── manage.py
│
└── README.md
✨ Features
👤 User Features

User Registration & Login

Browse available lunchboxes

View daily menus

Add meals to cart

Place orders

Subscription based meal plans

Order history

Profile management

🧑‍🍳 Vendor Features

Vendor dashboard

Add / update meal menus

Manage orders

Set meal availability

View customer requests

⚙️ Admin Features

Manage users

Manage vendors

Manage menus

Monitor orders

Platform analytics

🖥️ Frontend Pages

🏠 Home Page

🍛 Menu Page

🛒 Cart Page

📦 Orders Page

👤 User Profile

🔑 Login / Register

📊 Vendor Dashboard

⚙️ Admin Panel

🔌 API Endpoints
Authentication
POST /api/register
POST /api/login
POST /api/logout
Meals
GET /api/meals
GET /api/meals/{id}
POST /api/meals
PUT /api/meals/{id}
DELETE /api/meals/{id}
Orders
POST /api/orders
GET /api/orders
GET /api/orders/{id}
Users
GET /api/profile
PUT /api/profile
⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/IndianLunchBox.git
cd IndianLunchBox
2️⃣ Backend Setup (Django)

Install dependencies

pip install django djangorestframework mysqlclient

Run migrations

python manage.py makemigrations
python manage.py migrate

Start Django server

python manage.py runserver

Backend will run on

http://127.0.0.1:8000
3️⃣ Frontend Setup (React)

Move to frontend folder

cd frontend

Install dependencies

npm install

Start React server

npm start

Frontend will run on

http://localhost:3000
🗄️ Database Schema (Example)
Users
Field	Type
id	Integer
name	Varchar
email	Varchar
password	Varchar
role	User/Vendor/Admin
Meals
Field	Type
id	Integer
name	Varchar
description	Text
price	Decimal
vendor_id	Foreign Key
Orders
Field	Type
id	Integer
user_id	Foreign Key
total_price	Decimal
order_status	Pending/Delivered
📊 Future Improvements

Payment Gateway Integration

Real-time Order Tracking

Meal Subscription System

AI-based Meal Recommendation

Mobile App Version

Nutrition Information

🎯 Learning Outcomes

This project demonstrates:

Full Stack Development

REST API Design

React Component Architecture

Django Backend Development

Database Integration

Authentication Systems

👩‍💻 Author

Bella
Full Stack Developer
Python | React | Django

📜 License

This project is developed for academic and educational purposes.
