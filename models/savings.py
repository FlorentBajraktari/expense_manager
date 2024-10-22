from .database import connect_db


def add_savings_goal(goal, target_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO savings (goal, target_amount, current_amount) VALUES (?, ?, ?)',
                   (goal, target_amount, 0))
    conn.commit()
    conn.close()


def update_savings_amount(savings_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE savings SET current_amount = current_amount + ? WHERE id = ?', (amount, savings_id))
    conn.commit()
    conn.close()


def get_savings_goals():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM savings')
    savings = cursor.fetchall()
    conn.close()
    return savings
