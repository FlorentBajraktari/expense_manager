import sqlite3
from models.database import connect_db


def add_transaction(user_id, category, amount, type, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (user_id, category, amount, type, date) VALUES (?, ?, ?, ?, ?)",
                   (user_id, category, amount, type, date))
    conn.commit()
    conn.close()


def get_transactions(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    return cursor.fetchall()


def update_transaction(transaction_id, category, amount, type, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET category = ?, amount = ?, type = ?, date = ? WHERE id = ?",
                   (category, amount, type, date, transaction_id))
    conn.commit()
    conn.close()


def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
