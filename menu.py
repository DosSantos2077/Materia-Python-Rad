import tkinter as tk

def menu(user_id,usuario):
    janela = tk.Tk()
    janela.title("Sistema Principal")
    janela.geometry("300x150")

    label_id = tk.Label(janela, text=f"ID do usuário: {user_id}")
    label_id.pack(pady=10)

    label = tk.Label(janela, text=f"Bem-vindo, {usuario}!", font=("Arial", 14))
    label.pack(pady=30)

    btn_sair = tk.Button(janela, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10)

    janela.mainloop()
