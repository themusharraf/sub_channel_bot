import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('preson.db')
cursor = conn.cursor()

# Define the users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        active INTEGER DEFAULT 1
    )
''')
conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'active' = ? WHERE 'user_id' = ?", (active, user_id,))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
