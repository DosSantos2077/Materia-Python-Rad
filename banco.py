import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE login(user text, senha text)")

banco.commit()