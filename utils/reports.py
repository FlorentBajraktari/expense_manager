import pandas as pd
from fpdf import FPDF
import sqlite3


def generate_transaction_report(filename="transaction_report.xlsx"):
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    data = cursor.fetchall()
    conn.close()

    # Krijo një DataFrame për eksport në Excel
    df = pd.DataFrame(
        data, columns=["ID", "Kategoria", "Shuma", "Lloji", "Data"])
    df.to_excel(filename, index=False)
    print(f"Raporti u gjenerua dhe u ruajt në {filename}")


def generate_pdf_report(filename="report.pdf"):
    conn = sqlite3.connect('expense_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, amount, type, date FROM transactions')
    transactions = cursor.fetchall()
    conn.close()

    # Krijo një dokument PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Shto titullin dhe përmbajtjen e raportit
    pdf.cell(200, 10, txt="Raporti Financiar", ln=True, align="C")
    pdf.cell(200, 10, txt="-------------------", ln=True, align="C")
    for transaction in transactions:
        category, amount, trans_type, date = transaction
        pdf.cell(
            200, 10, txt=f"{category}: ${amount} ({trans_type}) on {date}", ln=True, align="L")

    pdf.output(filename)
    print(f"Raporti u gjenerua dhe u ruajt në {filename}")
