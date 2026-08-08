# 🚀 Smart Complaint Analyzer

> An AI-powered complaint management system that automates complaint classification, tracking, and analytics using Machine Learning, FastAPI, Streamlit, and MongoDB Atlas.

---

## 📌 Overview

Smart Complaint Analyzer is an intelligent grievance management platform designed to streamline the complaint handling process for organizations and public authorities.

The system automatically classifies complaints into predefined categories using a Machine Learning model, detects urgency, stores complaint records in a cloud database, and provides administrators with a powerful dashboard for monitoring, tracking, and managing complaints.

---

## ✨ Key Features

### 🤖 AI & Machine Learning
- Complaint classification using Machine Learning
- Automatic category prediction
- Confidence score prediction
- Urgency detection

### 🌐 Backend
- RESTful APIs built with FastAPI
- Complaint registration
- Complaint status management
- Analytics APIs
- MySQL Database Integration
- Relational Database Design
- SQL-based CRUD Operations
- UUID-based complaint IDs

  ## Database -> MySQL
  <img width="1357" height="538" alt="image" src="https://github.com/user-attachments/assets/34fc783c-83b5-4f68-958a-00eb41a74e77" />


### 👤 Citizen Dashboard
- Submit complaints
- Receive unique complaint ID
- View complaint analysis
- Track submitted complaints

  ## Citizen Dashboard
  <img width="1919" height="1035" alt="image" src="https://github.com/user-attachments/assets/17ec8508-3d4b-4989-a3bf-6234e9448753" />


---

### 📊 Admin Dashboard
- Secure Admin Login
- Complaint statistics
- Complaint status updates
- Search & filtering
- High-priority complaint monitoring
- Interactive analytics dashboard
- Category distribution charts
- Status distribution charts

  ## Public Complaint Analysis
  <img width="1919" height="1028" alt="image" src="https://github.com/user-attachments/assets/9b1125d0-44b8-4558-b403-6de63270654b" />

  ## Admin Dashboard — Analytics
  <img width="1919" height="1030" alt="image" src="https://github.com/user-attachments/assets/2e941406-0694-419d-a5e9-1ee96b6bb9de" />

  ## Admin Dashboard — Complaint Management
  <img width="1919" height="1039" alt="image" src="https://github.com/user-attachments/assets/01fe26ae-170a-412e-ae53-a6dbeb432570" />

  ## High Priority & Status Management
  <img width="1919" height="1040" alt="image" src="https://github.com/user-attachments/assets/c9f52efa-bc98-45b9-87b7-71aeea0d1455" />
  


# 🏗️ System Architecture

```text
Citizen
    │
    ▼
Streamlit Dashboard
    │
    ▼
FastAPI Backend
    │
    ├────────► Machine Learning Model
    │              │
    │              ▼
    │       Category Prediction
    │
    ▼
MongoDB Atlas
    │
    ▼
Admin Dashboard
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Machine Learning | Scikit-learn |
| Database | MySQL |
| Database Driver | SQLAlchemy |
| Data Processing | Pandas |
| Visualization | Plotly |
| Model Serialization | Joblib |

---

# 📂 Project Structure

```text
Smart-Complaint-Analyzer/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── ...
│
├── admin_dashboard/
│   └── app.py
│
├── public_dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/priyankasaini3927/Smart-Complaint-Analyzer.git
cd Smart-Complaint-Analyzer
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Launch Admin Dashboard

```bash
streamlit run admin_dashboard/app.py
```

---

## 5️⃣ Launch Citizen Dashboard

```bash
streamlit run public_dashboard/app.py
```

---

# 📈 Current Capabilities

- ✅ AI-powered complaint classification
- ✅ Confidence score prediction
- ✅ Complaint tracking
- ✅ Complaint status management
- ✅ Admin dashboard
- ✅ Complaint analytics
- ✅ Search & filtering
- ✅ High-priority complaint detection
- ✅ Interactive visualizations
- ✅ MySQL Database

---

# 📊 Future Roadmap (Version 2)

- MySQL Database
- JWT Authentication
- Citizen, Officer & Admin Roles
- Officer Dashboard
- Image Upload
- Notifications
- PDF Report Generation
- Complaint Assignment
- AI Duplicate Complaint Detection
- AI Priority Prediction
- React Frontend
- Docker Deployment

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning Classification
- REST API Development
- Database Design
- Cloud Database Integration
- Dashboard Development
- Data Visualization
- Backend Development
- Full Stack Application Architecture

---

# 🤝 Contributing

Contributions, feature suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is developed for educational and portfolio purposes.

---

# 👩‍💻 Author

**Priyanka Saini**

AI & Data Science Student

- GitHub: https://github.com/priyankasaini3927
- LinkedIn: https://www.linkedin.com/in/priyanka-saini-460511261/

---

⭐ If you found this project interesting, consider giving it a star!
