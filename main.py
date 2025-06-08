from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainWindow
from datetime import datetime
import json
import os


DATA_FILE = "plants.json"


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def load_plants(self):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            for plant in data:
                plant["last_transplant"] = datetime.strptime(plant["last_transplant"], "%Y-%m-%d").date()
                plant["next_watering"] = datetime.strptime(plant["next_watering"], "%Y-%m-%d").date()
                plant["next_fertilizer"] = datetime.strptime(plant["next_fertilizer"], "%Y-%m-%d").date()
            self.all_plants = data
            self.filtered_plants = self.all_plants


def save_plants(self):
    data = []
    for plant in self.all_plants:
        plant_copy = plant.copy()
        plant_copy["last_transplant"] = plant_copy["last_transplant"].strftime("%Y-%m-%d")
        plant_copy["next_watering"] = plant_copy["next_watering"].strftime("%Y-%m-%d")
        plant_copy["next_fertilizer"] = plant_copy["next_fertilizer"].strftime("%Y-%m-%d")
        data.append(plant_copy)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)