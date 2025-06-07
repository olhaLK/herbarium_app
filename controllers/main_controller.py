from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QGraphicsScene, QWidget, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from datetime import datetime
from ui.ui_main_window import Ui_MainWindow
from ui.ui_add_plant import Ui_addPlant
from ui.ui_item import Ui_Form
from models.plant_model import Plant
from database.db_manager import load_plants, save_plants
from utils.helpers import calc_progress, format_date
from controllers.plant_detail_window import PlantDetailWindow
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.all_plants: list[Plant] = load_plants()
        self.filtered_plants = self.all_plants.copy()

        self.ui.btnAddMain.clicked.connect(self.open_add_dialog)
        self.ui.btnSearchMain.clicked.connect(self.search_plant)
        self.ui.filterMain.addItems([
            "Все",
            "Полив просрочен",
            "Пересадка давно",
            "Удобрение просрочено"
        ])
        self.ui.filterMain.currentTextChanged.connect(self.apply_filter)

        layout = QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(layout)
        layout.setSpacing(15)
        layout.setContentsMargins(10, 10, 10, 10)
        self.render_plants()

    def render_plants(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        for plant in self.filtered_plants:
            item_ui = Ui_Form()
            form = QWidget()
            item_ui.setupUi(form)

            item_ui.labelNameItem.setText(plant.name)
            item_ui.labelSortItem.setText(plant.sort)
            item_ui.lastWateringItem.setText(format_date(plant.last_watering))
            item_ui.nextWateringItem.setText(format_date(plant.next_watering))
            item_ui.lastFeritilizerItem.setText(format_date(plant.last_fertilizer))
            item_ui.nextFeritilizerItem.setText(format_date(plant.next_fertilizer))
            item_ui.progressWateringItem.setValue(calc_progress(plant.last_watering, plant.next_watering))
            item_ui.progressFeritilizerItem.setValue(calc_progress(plant.last_fertilizer, plant.next_fertilizer))

            if plant.image and os.path.exists(plant.image):
                pix = QPixmap(plant.image).scaled(160, 160, Qt.KeepAspectRatio)
                scene = QGraphicsScene()
                scene.addPixmap(pix)
                item_ui.viewItem.setScene(scene)

            item_ui.btnMoreItem.clicked.connect(lambda _, p=plant: self.open_edit_view(p))
            layout.addWidget(form)

    def open_add_dialog(self):
        dialog = QDialog()
        self.add_ui = Ui_addPlant()
        self.add_ui.setupUi(dialog)

        self.add_ui.btnYesDelete.clicked.connect(dialog.reject)
        self.add_ui.btnBackDelete.clicked.connect(lambda: self.save_new_plant(dialog))
        dialog.exec()

    def save_new_plant(self, dialog):
        name = self.add_ui.textEditNameAddPlant.toPlainText().strip()
        sort = self.add_ui.textEditSortAddPlant.toPlainText().strip()
        watering_days = self.add_ui.spinWateringAddPlant.value()
        fertilizer_days = self.add_ui.spinFertilizerAddPlant.value()
        transplant_date = self.add_ui.dateAddPlant.date().toPython()

        today = datetime.today().date()
        new_plant = Plant(
            name=name,
            sort=sort,
            watering_freq=watering_days,
            fertilizer_freq=fertilizer_days,
            last_watering=today,
            last_fertilizer=today,
            last_transplant=transplant_date,
            image="",
            description=""
        )

        self.all_plants.append(new_plant)
        self.filtered_plants = self.all_plants
        save_plants(self.all_plants)
        self.render_plants()
        dialog.accept()

    def open_edit_view(self, plant: Plant):
        plant_dict = {
            "name": plant.name,
            "sort": plant.sort,
            "watering_freq": plant.watering_freq,
            "fertilizer_freq": plant.fertilizer_freq,
            "last_watering": plant.last_watering,
            "last_fertilizer": plant.last_fertilizer,
            "last_transplant": plant.last_transplant,
            "image": plant.image,
            "description": plant.description,
            "next_watering": plant.next_watering,
            "next_fertilizer": plant.next_fertilizer,
        }

        def sync_back():
            plant.name = plant_dict["name"]
            plant.sort = plant_dict["sort"]
            plant.watering_freq = plant_dict["watering_freq"]
            plant.fertilizer_freq = plant_dict["fertilizer_freq"]
            plant.last_watering = plant_dict["last_watering"]
            plant.last_fertilizer = plant_dict["last_fertilizer"]
            plant.last_transplant = plant_dict["last_transplant"]
            plant.image = plant_dict["image"]
            plant.description = plant_dict["description"]
            save_plants(self.all_plants)
            self.render_plants()

        def delete_callback(p_dict):
            self.all_plants.remove(plant)
            self.filtered_plants = self.all_plants
            save_plants(self.all_plants)
            self.render_plants()

        self.detail_window = PlantDetailWindow(plant_dict, sync_back, delete_callback)
        self.detail_window.show()

    def search_plant(self):
        query = self.ui.searchMain.text().strip().lower()
        self.filtered_plants = [
            plant for plant in self.all_plants if query in plant.name.lower()
        ] if query else self.all_plants
        self.render_plants()

    def apply_filter(self, text):
        today = datetime.today().date()
        if text == "Все":
            self.filtered_plants = self.all_plants
        elif text == "Полив просрочен":
            self.filtered_plants = [p for p in self.all_plants if p.next_watering < today]
        elif text == "Пересадка давно":
            self.filtered_plants = [p for p in self.all_plants if (today - p.last_transplant).days > 180]
        elif text == "Удобрение просрочено":
            self.filtered_plants = [p for p in self.all_plants if p.next_fertilizer < today]
        else:
            self.filtered_plants = self.all_plants
        self.render_plants()
