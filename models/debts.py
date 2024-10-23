from models.database import connect_db


def get_debts():
    """
    Merr të gjitha borxhet nga baza e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM debts")
    result = cursor.fetchall()
    conn.close()
    return result


def plan_debt_payment(debt_id, amount):
    """
    Planifikon një pagesë për një borxh specifik duke shtuar një rekord të ri.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE debts SET remaining_amount = remaining_amount - ? WHERE id = ?",
                   (amount, debt_id))
    conn.commit()
    conn.close()


def add_debt(name, total_amount, remaining_amount):
    """
    Shton një borxh të ri në bazën e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO debts (name, total_amount, remaining_amount) VALUES (?, ?, ?)",
                   (name, total_amount, remaining_amount))
    conn.commit()
    conn.close()


def update_debt(debt_id, name, total_amount, remaining_amount):
    """
    Përditëson informacionin e një borxhi ekzistues.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE debts SET name = ?, total_amount = ?, remaining_amount = ? WHERE id = ?",
                   (name, total_amount, remaining_amount, debt_id))
    conn.commit()
    conn.close()


def delete_debt(debt_id):
    """
    Fshin një borxh të caktuar nga baza e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM debts WHERE id = ?", (debt_id,))
    conn.commit()
    conn.close()
