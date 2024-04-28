import sqlite3


def create_table_users():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        user_name TEXT,
        phone TEXT
    );
    ''')


def first_select_user(chat_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute('''
    SELECT * FROM users WHERE chat_id = ?
    ''', (chat_id,))
    user = cur.fetchone()
    conn.close()
    return user


def first_register_user(chat_id, full_name):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO users(chat_id, user_name) VALUES (?, ?)
    ''', (chat_id, full_name))
    conn.commit()
    conn.close()


def update_user_finish_register(phone, chat_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute('''
    UPDATE users
        SET phone = ?
        WHERE chat_id = ?
    ''', (phone, chat_id))
    conn.commit()
    conn.close()
