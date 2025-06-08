from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from ui.ui_item_full import Ui_itemFull
from ui.ui_delete_dialog import Ui_deleteDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from datetime import timedelta
import os


class PlantDetailWindow(QMainWindow):
    def __init__(self, plant: dict, save_callback, delete_callback):
        super().__init__()
        self.ui = Ui_itemFull()
        self.ui.setupUi(self)

        self.setWindowTitle("Edit Plant")

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_path, "icons", "logo.svg")
        self.setWindowIcon(QIcon(icon_path))

        self.plant = plant
        self.save_callback = save_callback
        self.delete_callback = delete_callback
        self.image_path = self.plant.get("image", "")

        self.fill_fields()
        self.setup_connections()


    def fill_fields(self):
        self.ui.textEditNameItemFull.setPlainText(self.plant["name"])
        self.ui.textEditSortItemFull.setPlainText(self.plant["sort"])
        self.ui.spinWateringItemFull.setValue(self.plant["watering_freq"])
        self.ui.spinFeritilizerItem.setValue(self.plant["fertilizer_freq"])
        self.ui.dateLastWateringItem.setDate(self.plant["last_watering"])
        self.ui.dateLastFeritilizerItem.setDate(self.plant["last_fertilizer"])
        self.ui.textEditDescriptionItemFull.setPlainText(self.plant.get("description", ""))

        if os.path.exists(self.image_path):
            pix = QPixmap(self.image_path).scaled(250, 230, Qt.KeepAspectRatio)
            from PySide6.QtWidgets import QGraphicsScene
            scene = QGraphicsScene()
            scene.addPixmap(pix)
            self.ui.viewItemFull.setScene(scene)


    def setup_connections(self):
        self.ui.btnSaveItem.clicked.connect(self.save)
        self.ui.btnBackItem.clicked.connect(self.close)
        self.ui.btnDeleteItem.clicked.connect(self.confirm_delete)
        self.ui.changeImageItemFull.clicked.connect(self.change_image)


    def change_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select image", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.image_path = path
            pix = QPixmap(path).scaled(250, 230, Qt.KeepAspectRatio)
            from PySide6.QtWidgets import QGraphicsScene
            scene = QGraphicsScene()
            scene.addPixmap(pix)
            self.ui.viewItemFull.setScene(scene)


    def save(self):
        self.plant["name"] = self.ui.textEditNameItemFull.toPlainText()
        self.plant["sort"] = self.ui.textEditSortItemFull.toPlainText()
        self.plant["watering_freq"] = self.ui.spinWateringItemFull.value()
        self.plant["fertilizer_freq"] = self.ui.spinFeritilizerItem.value()
        self.plant["last_watering"] = self.ui.dateLastWateringItem.date().toPython()
        self.plant["last_fertilizer"] = self.ui.dateLastFeritilizerItem.date().toPython()
        self.plant["next_watering"] = self.plant["last_watering"] + timedelta(days=self.plant["watering_freq"])
        self.plant["next_fertilizer"] = self.plant["last_fertilizer"] + timedelta(days=self.plant["fertilizer_freq"])
        self.plant["image"] = self.image_path
        self.plant["description"] = self.ui.textEditDescriptionItemFull.toPlainText()

        self.save_callback()
        self.close()


    def confirm_delete(self):
        dialog = QDialog(self)
        ui = Ui_deleteDialog()
        ui.setupUi(dialog)
        ui.btnYesDelete.clicked.connect(lambda: self.delete_plant(dialog))
        ui.btnBackDelete.clicked.connect(dialog.close)
        dialog.exec()


    def delete_plant(self, dialog):
        self.delete_callback(self.plant)
        dialog.accept()
        self.close()
