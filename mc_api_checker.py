import requests

def check_availible(word):
    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{word}")
    if resp.status_code == 204:
        return True
    else:
        return False