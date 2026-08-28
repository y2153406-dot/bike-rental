# 🚲 BikeRental

A web-based Bike Rental application built using Django. The platform allows users to browse available bikes, register and log in, book bikes, make payments, and manage their bookings.

---

## 🚀 Features

### 👤 User Authentication

- User registration
- User login and logout
- Google OAuth authentication
- Secure authentication using Django

### 🚲 Bike Management

- View available bikes
- View bike details
- Browse different bike categories
- Check bike availability

### 📅 Booking System

- Book bikes for selected dates
- Manage bike bookings
- Track booking information
- Prevent booking conflicts based on availability

### 💳 Payment Integration

- Online payment integration using Razorpay
- Secure payment processing
- Test mode support for development

### 🖥️ Responsive Design

- Responsive user interface
- Mobile-friendly layout
- Clean and simple design using Bootstrap

---

## 🛠️ Technologies Used

### Backend

- Python
- Django

### Database

- SQLite (Development)
- PostgreSQL (Production)

### Authentication

- Django Authentication
- Django Allauth
- Google OAuth

### Payment Gateway

- Razorpay

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

### Deployment

- Render

---

## 📂 Project Structure

```text
BikeRental/
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── bookings/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── vehicles/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│
├── static/
│
├── requirements.txt
│
├── manage.py
│
└── README.md
