import tkinter as tk
from meross.state import toggle_state



def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("400x300")
    
    etat = False
    
    def changement_etat():
        etat_courant = toggle_state()           # call la fonction qu'on a importé de meross.state
        if etat_courant:
            btn_1.config(text="ON")
        else:
            btn_1.config(text="OFF")     
    
    btn_1 = tk.Button(root,text="OFF", command=changement_etat)
    
    btn_1.pack()
    root.mainloop()