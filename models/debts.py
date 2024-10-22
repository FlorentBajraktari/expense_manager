from .database import connect_db


def add_debt(debtor, amount, interest_rate, due_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO debts (debtor, amount, interest_rate, due_date) VALUES (?, ?, ?, ?)',
                   (debtor, amount, interest_rate, due_date))
    conn.commit()
    conn.close()


def get_debts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM debts')
    debts = cursor.fetchall()
    conn.close()
    return debts


def make_debt_payment(debt_id, payment_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE debts SET amount = amount - ? WHERE id = ?', (payment_amount, debt_id))
    conn.commit()
    conn.close()
