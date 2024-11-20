import os

HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as file:
        return int(file.read())

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))