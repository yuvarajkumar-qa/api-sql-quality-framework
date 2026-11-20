# API & SQL Quality Framework

REST API and database persistence checks built with Python, Pytest, `requests`, and SQLite, running automatically in GitHub Actions.

## What's Tested
* **Users API (`tests/test_users_api.py`):** Fetching an existing user (`200`), handling a missing user ID (`404`), and creating a user payload (`201`) via `UsersClient`.
* **Orders & SQL Integrity (`tests/test_orders_sql.py`):** Verifying persisted order records and ensuring failed transactions are excluded from settled revenue totals using SQL queries.

## Folder Structure
```text
├── .github/workflows/api-sql-tests.yml
├── api/
│   └── users_client.py
├── tests/
│   ├── test_users_api.py
│   └── test_orders_sql.py
├── pytest.ini
└── requirements.txt
