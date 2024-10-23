import sqlite3


def get_budgets():
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budgets")
    result = cursor.fetchall()
    conn.close()
    return result


def add_budget(category, amount, month):
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO budgets (category, amount, month) VALUES (?, ?, ?)", (category, amount, month))
    conn.commit()
    conn.close()


def update_budget(id, category, amount, month):
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE budgets SET category=?, amount=?, month=? WHERE id=?",
                   (category, amount, month, id))
    conn.commit()
    conn.close()


def delete_budget(id):
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE id=?", (id,))
    conn.commit()
    conn.close()
