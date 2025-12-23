import tkinter as tk

def hello_world():
    print("Hello World.")


def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("400x300")
    
    btn_1 = tk.Button(root,text="Hello World", command=hello_world)
    
    btn_1.pack()
    root.mainloop()