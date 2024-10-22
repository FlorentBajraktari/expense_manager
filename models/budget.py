from .database import connect_db


def add_budget(user_id, category, limit_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO budgets (user_id, category, limit_amount) VALUES (?, ?, ?)",
                   (user_id, category, limit_amount))
    conn.commit()
    conn.close()


def get_budgets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM budgets')
    budgets = cursor.fetchall()
    conn.close()
    return budgets


def update_budget(category, new_limit):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE budgets SET limit=? WHERE category=?',
                   (new_limit, category))
    conn.commit()
    conn.close()
