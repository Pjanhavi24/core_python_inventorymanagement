
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

FILE_PATH = os.path.join(DATA_DIR, "inventory.json")


def load_inventory():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        print("Error reading inventory file!")
        return []


def save_inventory(products):

    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(FILE_PATH, "w") as file:
            json.dump(products, file, indent=4)

        return True

    except OSError as error:
        print("Error saving inventory:", error)
        return False
