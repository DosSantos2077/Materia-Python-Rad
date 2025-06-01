import tkinter as tk


root = tk.Tk()
root.title("Menu")  
root.geometry("300x200")  
root.configure(bg="lightblue")

btn1 = tk.Button(root, text="Botão 1")
btn2 = tk.Button(root, text="Botão 2")
btn3 = tk.Button(root, text="Botão 3")

btn1.pack(fill="both", expand=True,padx=10, pady=5)
btn2.pack(fill="both", expand=True,padx=10, pady=5)
btn3.pack(fill="both", expand=True,padx=10, pady=5)

root.mainloop()