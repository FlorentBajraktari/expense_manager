import sqlite3


def connect_db():
    return sqlite3.connect('expense_manager.db')


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela për përdoruesit
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Tabela për transaksionet
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            type TEXT,  -- "expense" ose "income"
            date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    # Tabela për buxhetet
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            limit_amount REAL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    # Krijo tabelën për faturat
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL,
            due_date TEXT,
            status TEXT, -- "paid" ose "unpaid"
            recurring INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL,
            due_date TEXT,
            status TEXT, -- "paid" ose "unpaid"
            recurring INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


def connect_db():
    return sqlite3.connect('expense_manager.db')


def validate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    # Tabela për faturat dhe strukturat tjera të mëparshme
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL,
            due_date TEXT,
            status TEXT,
            recurring INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


def connect_db():
    return sqlite3.connect('expense_manager.db')


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL,
            due_date TEXT,
            status TEXT, -- "paid" ose "unpaid"
            recurring INTEGER DEFAULT 0
        )
    ''')

    # Shto përdorues të paracaktuar nëse nuk ka përdorues në bazën e të dhënave
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if not users:
        cursor.executemany(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            [
                ("user1", "password1"),
                ("user2", "password2"),
                ("admin", "adminpass")
            ]
        )

    conn.commit()
    conn.close()
