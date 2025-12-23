import hashlib
import json
from pathlib import Path



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def verify_user(email, password):
    file_path = Path(__file__).parent / "users.json" # Prends le meme dossier parent que lui
    if not file_path.exists():
        return False  # pas d'utilisateurs

    with open(file_path, "r") as f:
        users = json.load(f)

    hashed_password = hash_password(password)

    for user in users:
        if user["email"] == email and user["password"] == hashed_password:
            return True

    return False