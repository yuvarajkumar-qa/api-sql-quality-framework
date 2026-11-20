import sqlite3
import pytest


@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_email TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    cur.executemany(
        "INSERT INTO orders (customer_email, amount, status) VALUES (?, ?, ?)",
        [
            ("user1@example.com", 49.99, "PAID"),
            ("user2@example.com", 19.50, "FAILED"),
        ],
    )
    conn.commit()
    yield conn
    conn.close()


@pytest.mark.db
def test_paid_order_persists_with_exact_amount(db_conn):
    cur = db_conn.cursor()
    cur.execute(
        "SELECT customer_email, amount, status FROM orders WHERE customer_email = ?",
        ("user1@example.com",),
    )
    row = cur.fetchone()

    assert row is not None
    assert row[0] == "user1@example.com"
    assert row[1] == 49.99
    assert row[2] == "PAID"


@pytest.mark.db
def test_failed_orders_are_excluded_from_revenue_sum(db_conn):
    cur = db_conn.cursor()
    # Only PAID orders should count toward settled revenue
    cur.execute("SELECT COALESCE(SUM(amount), 0) FROM orders WHERE status = 'PAID'")
    settled_total = cur.fetchone()[0]

    assert settled_total == pytest.approx(49.99)
