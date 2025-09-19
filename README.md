Personal Finance Tracker 

A simple but powerful backend service to track income & expenses, built with Django + Django REST Framework.
Includes JWT authentication, custom categories, transactions CRUD, and monthly reports.


Features-
User registration & JWT login
Categories (your own + shared defaults optional)
Transactions (income/expense) CRUD
Monthly report API
Admin panel for superusers
SQLite by default
Easy switch to MySQL for production


SETUP(Mac/Linux)-

# clone project
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
cd finance-tracker

# create & activate virtual env
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py makemigrations
python manage.py migrate

# create superuser (admin panel)
python manage.py createsuperuser

# run server
python manage.py runserver


Server runs at:
http://127.0.0.1:8000



API Endpoints-
Auth-
POST /api/register/ → Create account
POST /api/token/ → Get access/refresh token
POST /api/token/refresh/ → Refresh access token

Categories-
GET /api/categories/
POST /api/categories/ → create category
PUT /api/categories/{id}/
DELETE /api/categories/{id}/

Transactions-
GET /api/transactions/
POST /api/transactions/
PUT /api/transactions/{id}/
DELETE /api/transactions/{id}/

Reports-
GET /api/reports/monthly/?month=YYYY-MM → JSON
GET /api/reports/monthly/?month=YYYY-MM&format=csv → CSV download

Admin Panel-
Visit http://127.0.0.1:8000/admin/
Log in with your superuser credentials



API Testing with Postman(examples)-

Create a category-
POST http://127.0.0.1:8000/api/categories/
Headers → Authorization: Bearer <your-access-token>
Body → raw JSON
{
  "name": "Salary"
}

Create a transaction-
POST http://127.0.0.1:8000/api/transactions/
Headers → Authorization: Bearer <your-access-token>
Body → raw JSON
{
  "type": "income",
  "amount": 1500,
  "note": "September Salary",
  "date": "2025-09-01",
  "category": 1
}

Get monthly report-
GET http://127.0.0.1:8000/api/reports/monthly/?month=2025-09
Headers → Authorization: Bearer <your-access-token>
Response:
{
  "month": "2025-09",
  "income": 1500.0,
  "expense": 0.0,
  "net_saving": 1500.0
}
