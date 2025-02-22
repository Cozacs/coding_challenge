# REST API - Person Info  

Simple API to add and search persons info based on name and company.

## 🚀 Technologies  
- Python 3  
- Flask  
- SQLAlchemy (ORM)  
- SQLite (banco de dados)  
- Pytest (testes automatizados)  

## 📌 How to install and run 

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Cozacs/coding_challenge
cd rest-api-person-info

### 2️⃣ Create and activate your virtual development

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Create Database

python -c "from app import db; db.create_all()"

### 5️⃣ Run Server

python run.py
API will run at door http://127.0.0.1:5000/

## 🛠 Endpoints da API

### 1️⃣ Add person to Database

method[POST]

JSON example
{
  "name": "John Doe",
  "current_role": "Software Engineer",
  "company": "Google",
  "location": "San Francisco, CA",
  "linkedin_url": "https://linkedin.com/in/johndoe"
}

Expected answer
Code[201]
{
  "message": "Person add to Database!"
}

### 2️⃣ Search person

method[GET]

Request example
/person-info?name=John%20Doe&company=Google

Expected answer
{
  "name": "John Doe",
  "current_role": "Software Engineer",
  "company": "Google",
  "location": "San Francisco, CA",
  "linkedin_url": "https://linkedin.com/in/johndoe"
}