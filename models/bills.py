from models.database import connect_db


def add_new_bill(name, amount, due_date, status, recurring):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (name, amount, due_date, status, recurring) VALUES (?, ?, ?, ?, ?)",
                   (name, amount, due_date, status, recurring))
    conn.commit()
    conn.close()


def get_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    result = cursor.fetchall()
    conn.close()
    return result


def update_bill_status(bill_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE bills SET status = ? WHERE id = ?",
                   (status, bill_id))
    conn.commit()
    conn.close()


def get_paid_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills WHERE status = 'paid'")
    result = cursor.fetchall()
    conn.close()
    return result


def get_unpaid_bills():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills WHERE status = 'unpaid'")
    result = cursor.fetchall()
    conn.close()
    return result
