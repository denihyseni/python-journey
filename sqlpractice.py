import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
'''
)

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@example.com'))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()







