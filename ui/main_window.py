import tkinter as tk
from meross.devices import get_devices
from PIL import Image, ImageTk

CARD_WIDTH = 180

def launch_app():
    root = tk.Tk()
    root.title("MCI - Meross Controller Interface")
    root.geometry("700x400")

    cards_frame = tk.Frame(root)
    cards_frame.pack(fill="both", expand=True, padx=10, pady=10)

    devices = get_devices()
    cards = []

    def create_device_card(parent, device):
        card = tk.Frame(
            parent,
            width=CARD_WIDTH,
            height=220,
            bd=2,
            relief="groove"
        )
        card.pack_propagate(False)
        
        pil_image = Image.open(device["image"])
        pil_image = pil_image.resize((140, 140))  # h x w

        image = ImageTk.PhotoImage(pil_image)

        image_label = tk.Label(card, image=image)
        image_label.image = image 
        image_label.pack(pady=5)

        name_label = tk.Label(card, text=device["name"])
        name_label.pack()

        def toggle():
            device["state"] = not device["state"]
            btn.config(text="ON" if device["state"] else "OFF")

        btn = tk.Button(card, text="ON" if device["state"] else "OFF", command=toggle)
        btn.pack(pady=5)

        return card





    for device in devices:
        card = create_device_card(cards_frame, device)
        cards.append(card)

    def get_columns(width):
        return max(1, width // CARD_WIDTH)

    def render_cards():
        for widget in cards_frame.winfo_children():
            widget.grid_forget()

        cols = get_columns(cards_frame.winfo_width())

        for index, card in enumerate(cards):
            row = index // cols
            col = index % cols
            card.grid(row=row, column=col, padx=10, pady=10, sticky="n")

    cards_frame.bind("<Configure>", lambda e: render_cards())
    root.mainloop()