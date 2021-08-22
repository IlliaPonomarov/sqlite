import sqlite3



class SQLighter:
    def __init__(self):
        self.connection = sqlite3.connect('userSQL.db')
        self.cursor = self.connection.cursor()
        print("Connection successful.")

    def get_users(self):
        return self.cursor.execute('SELECT * FROM stocks')

    def add_users(self,  user_id, user_name, user_age, user_country, status=True):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_id, user_name, user_age, user_country, status))

    def exists_users(self, user_id):
        with self.connection:
            res = self.cursor.execute(f"SELECT * FROM users WHERE ").fetchall()
            return bool(len(res))

    def p_sql(self):
        for rows in self.cursor.execute('SELECT * FROM users'):
            print(rows)

    def close(self):
        self.connection.close()


illia = SQLighter()

illia.add_users(2, 'Igor', 89, 'Slovak')
illia.add_users(3, 'Vitalik', 11, 'Germany')
illia.add_users(4, 'Artur', 16, 'USA')
illia.add_users(5, 'Nikita', 21, 'UK')
illia.add_users(6, 'Monster', 35, 'Russia')
illia.p_sql()