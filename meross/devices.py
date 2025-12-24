devices = [
    {
        "id": 1,
        "name": "Lampe Bureau",
        "type": "bulb",
        "image": "meross/images/bulb.png",
        "state": False
    },
    {
        "id": 2,
        "name": "Prise Télé",
        "type": "plug",
        "image": "meross/images/plug.png",
        "state": True
    },
    {
        "id": 3,
        "name": "Machine à Laver",
        "type": "plug",
        "image": "meross/images/plug.png",
        "state": False
    },
    {
        "id": 4,
        "name": "Luminaire Salon",
        "type": "bulb",
        "image": "meross/images/bulb.png",
        "state": True
    }
]

def get_devices():
    return devices