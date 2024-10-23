from models.database import connect_db


def get_auto_savings():
    """
    Merr të gjitha kursimet automatike nga baza e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM auto_savings")
    result = cursor.fetchall()
    conn.close()
    return result


def add_saving_goal(description, amount, frequency):
    """
    Shton një kursim të ri automatik në bazën e të dhënave.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO auto_savings (description, amount, frequency) VALUES (?, ?, ?)",
                   (description, amount, frequency))
    conn.commit()
    conn.close()


def update_saving_goal(saving_id, description, amount, frequency):
    """
    Përditëson një kursim automatik të caktuar.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE auto_savings SET description = ?, amount = ?, frequency = ? WHERE id = ?",
                   (description, amount, frequency, saving_id))
    conn.commit()
    conn.close()


def delete_saving_goal(saving_id):
    """
    Fshin një kursim automatik të caktuar.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM auto_savings WHERE id = ?", (saving_id,))
    conn.commit()
    conn.close()
