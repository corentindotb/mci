import tkinter as tk




def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("400x300")
    
    def hello_world():
        btn_1.config(text="Cliqué !",state="disabled")
    
    btn_1 = tk.Button(root,text="Hello World", command=hello_world)
    
    btn_1.pack()
    root.mainloop()