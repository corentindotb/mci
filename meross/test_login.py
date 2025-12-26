from meross_iot.http_api import MerossHttpClient

EMAIL = "corentin.lajeunesse@gmail.com"
PASSWORD = "Coco67coco67*c"

client = MerossHttpClient(email=EMAIL, password=PASSWORD)
client.login()

print("Login réussi !")
client.logout()