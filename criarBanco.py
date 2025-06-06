import sqlite3


def criar_ou_verificar_banco():
    """Cria o banco e as tabelas se não existirem."""
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    # Criação da tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL 
        )
    """)

    # Criação da tabela de registros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userId INTEGER NOT NULL,
            desc TEXT,
            data TEXT,
            todo INTEGER,
            path TEXT NOT NULL UNIQUE,
            FOREIGN KEY (userId) REFERENCES usuarios(id)
        )
    """)

    conn.commit()
    conn.close()