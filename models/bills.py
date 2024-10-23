from models.database import connect_db


def get_unpaid_bills():
    """
    Merr të gjitha faturat që janë të papaguara nga baza e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills WHERE status = 'unpaid'")
    result = cursor.fetchall()
    conn.close()
    return result


def get_paid_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills WHERE status = 'paid'")
    result = cursor.fetchall()
    conn.close()
    return result


def add_bill(name, amount, due_date, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (name, amount, due_date, status) VALUES (?, ?, ?, ?)",
                   (name, amount, due_date, status))
    conn.commit()
    conn.close()


def update_bill(bill_id, name, amount, due_date, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE bills SET name = ?, amount = ?, due_date = ?, status = ? WHERE id = ?",
                   (name, amount, due_date, status, bill_id))
    conn.commit()
    conn.close()


def delete_bill(bill_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bills WHERE id = ?", (bill_id,))
    conn.commit()
    conn.close()
