# 🛒 Shop Manager - Django manage shopping  platform

Shop Manager is a **Django-based e-commerce platform** that allows users to browse products, add them to their cart, and proceed with purchases. It includes **product management, cart functionality, secure authentication**, and a **responsive UI using Tailwind CSS**.

-----------------------------------------------------------------------------------------

## 📌 Features

- ✅ **User Authentication** - Secure login & signup  
- ✅ **Product Management** - Add, edit, and display products with images  
- ✅ **Shopping Cart** - Add, remove, and update cart items  
- ✅ **Product Filtering & Sorting** - Find products easily  ......................................................................
- .........................................
- ✅ **Order Management** - View cart & proceed to checkout  
- ✅ **Secure Payments** - Multiple payment options (future feature)  
- ✅ **Mobile-Friendly UI** - Responsive design with Tailwind CSS  

---

## 🚀 Tech Stack

- **Backend:** Django, SQLite  
- **Frontend:** Tailwind CSS, HTML  
- **Database:** SQLite  
- **Authentication:** Django Auth  

---

## 📂 Project Structure

```plaintext
shop_manager/        # Main project directory
│── shop/            # Main app for e-commerce functionalities
│   │── migrations/  # Database migrations
│   │── templates/   # HTML templates
│   │   ├── shop/    # Product & cart templates
│   │── static/      # CSS, JS, images
│   │── models.py    # Database models
│   │── views.py     # Business logic
│   │── urls.py      # URL routing
│   │── forms.py     # Django forms
│── media/           # Uploaded product images
│── db.sqlite3       # Database
│── manage.py        # Django management script
```

---

## 🛠 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ethic-bakeery/shop-manager.git
cd shop-manager
```
### **3️⃣ Apply Migrations & Create a Superuser**
```bash
python3 manage.py makemigrations shop
python3 manage.py migrate
python3 manage.py createsuperuser
```

### **4️⃣ Run the Development Server**
```bash
python manage.py runserver
```

📌 **Access the site at:**  
- **Frontend:** `http://127.0.0.1:8000/shop`  
- **Admin Panel:** `http://127.0.0.1:8000/admin/`

---
## 🛠 Future Enhancements

- ✅ **User Reviews & Ratings**
- ✅ **Payment Gateway Integration**
- ✅ **Order Tracking System**
- ✅ **Admin Dashboard**

---

## ⭐ Show Some Love!

If you like this project, give it a ⭐ on GitHub! 😊  

