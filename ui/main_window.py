import tkinter as tk




def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("400x300")
    
    etat = False
    
    def changement_etat():
        
        nonlocal etat    
        
        if etat == True:    
            btn_1.config(text="OFF")
            etat = False
        else:
            btn_1.config(text="ON")
            etat = True        
    
    btn_1 = tk.Button(root,text="OFF", command=changement_etat)
    
    btn_1.pack()
    root.mainloop()