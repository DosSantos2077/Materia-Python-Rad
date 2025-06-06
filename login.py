import tkinter as tk
from tkinter import messagebox
import sqlite3
import menu



def login(entry_usuario, entry_senha, janela_login):
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, usuario FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        user_id, nome_usuario = resultado
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        janela_login.destroy()
        menu.menu(user_id, nome_usuario)
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorretos.")

def cadastrar(entry_usuario, entry_senha):
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuario cadastrado.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuario já existe.")
    finally:
        conn.close()

def iniciar_login():
    

    janela_login = tk.Tk()
    janela_login.title("Login e Cadastro")
    janela_login.geometry("300x200")

    label_usuario = tk.Label(janela_login, text="Usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(janela_login)
    entry_usuario.pack(pady=5)

    label_senha = tk.Label(janela_login, text="Senha:")
    label_senha.pack(pady=5)
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.pack(pady=5)

    btn_login = tk.Button(janela_login, text="Login",
                          command=lambda: login(entry_usuario, entry_senha, janela_login))
    btn_login.pack(pady=5)

    btn_cadastrar = tk.Button(janela_login, text="Cadastrar",
                              command=lambda: cadastrar(entry_usuario, entry_senha))
    btn_cadastrar.pack(pady=5)

    janela_login.mainloop()
