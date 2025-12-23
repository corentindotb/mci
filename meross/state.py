etat = False

def toggle_state():
    global etat                 # reach la var en dehors de la func
    etat = not etat              # = Inverse d'Etat (not)
    return etat