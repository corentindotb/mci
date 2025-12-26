import tkinter as tk
from meross.devices import get_devices
from PIL import Image, ImageTk

CARD_WIDTH = 180

def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("700x400")
    root.resizable(False, False)
    root.configure(background='#252e3d')

    container = tk.Frame(root, bg='#252e3d')
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg='#252e3d', highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    cards_frame = tk.Frame(canvas, bg='#252e3d')
    canvas_window = canvas.create_window((0, 0), window=cards_frame, anchor="nw")


    def resize_canvas(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_canvas)

    devices = get_devices()
    cards = []

    def create_device_card(parent, device):
        card = tk.Frame(parent, width=180, height=220, bg='#2e3645')
        card.grid_propagate(False)

        pil_image = Image.open(device["image"]).resize((140, 140))
        image = ImageTk.PhotoImage(pil_image)

        img_label = tk.Label(card, image=image, bg='#2e3645')
        img_label.image = image
        img_label.pack(pady=5)

        name = tk.Label(card, text=device["name"], fg="white", bg='#2e3645')
        name.pack()

        def toggle():
            device["state"] = not device["state"]
            btn.config(text="ON" if device["state"] else "OFF")

        btn = tk.Button(card, text="ON" if device["state"] else "OFF", command=toggle)
        btn.pack(pady=5)

        return card

    for device in devices:
        cards.append(create_device_card(cards_frame, device))

    COLS = 3

    for i, card in enumerate(cards):
        row = i // COLS
        col = i % COLS
        card.grid(row=row, column=col, padx=10, pady=10)

    cards_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    root.mainloop()
