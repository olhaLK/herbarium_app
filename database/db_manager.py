import json
import os
from models.plant_model import Plant

DATA_FILE = "plants.json"

def load_plants():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return [Plant.from_dict(p) for p in data]
        except Exception as e:
            print(f"Ошибка при загрузке базы: {e}")
            return []

def save_plants(plants: list[Plant]):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([p.to_dict() for p in plants], file, ensure_ascii=False, indent=2)
