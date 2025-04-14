import sqlite3

DB_NAME = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)')
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, content FROM messages')
    messages = [{'id': row[0], 'content': row[1]} for row in c.fetchall()]
    conn.close()
    return messages

def add_message(content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO messages (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
