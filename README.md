# Vibeosys Python FastAPI Assignment

This project is a Product Management API developed using Python, FastAPI, Pydantic, SQLAlchemy and MySQL.

## Technologies Used
- Python 3.11+
- FastAPI
- Pydantic
- SQLAlchemy
- MySQL
- PyMySQL
- Uvicorn

## Project Structure
```text
app/__init__.py
app/crud.py
app/database.py
app/main.py
app/models.py
app/schemas.py
app/routes/__init__.py
app/routes/product.py
.env
.gitignore
README.md
requirements.txt
```

## Database
- MySQL is used.
- Database name: `vibeosys_assignment`
- The `DATABASE_URL` is configured in the local `.env` file.
- Example `.env` file:
```ini
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/vibeosys_assignment
```
- Note: Never commit the actual `.env` containing your database username or password to GitHub.

## Installation
First, create a virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment (Windows):
```bash
.venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Run the Project
Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

- API URL: http://127.0.0.1:8000
- Swagger Documentation: http://127.0.0.1:8000/docs

## APIs
- `POST /product/add`
- `GET /product/list?page=1` (returns 10 products per page)
- `GET /product/{id}/info`
- `PUT /product/{id}/update`

## Product Fields
- Product ID
- Name
- Category
- Description
- Product Image
- SKU
- Unit of Measure
- Lead Time
- Created Date
- Updated Date

## Category Values
- finished
- semi-finished
- raw

## Unit of Measure Values
- mtr
- mm
- ltr
- ml
- cm
- mg
- gm
- unit
- pack