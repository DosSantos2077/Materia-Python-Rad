import login
import sqlite3
import criarBanco

if __name__ == "__main__":
    criarBanco.criar_ou_verificar_banco()
    login.iniciar_login()       