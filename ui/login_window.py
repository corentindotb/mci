import tkinter as tk
from tkinter import messagebox
from utils.auth import verify_user
from ui.main_window import launch_app

def launch_login():
    root = tk.Tk()
    root.title("MCI - Login")
    root.geometry("300x200")

    tk.Label(root, text="Email:").pack(pady=(20,0))
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Mot de passe:").pack(pady=(10,0))
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def check_login():
        email = email_entry.get()
        password = password_entry.get()

        if verify_user(email, password):
            root.destroy()
            launch_app()        # Ouvre la fenêtre principale
        else:
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect")
    
    tk.Button(root, text="Se connecter", command=check_login).pack(pady=20)

    root.mainloop()