# Importing PyQt6 libraries
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QMessageBox
# Importing database connection
from DBConnection import DBConnection


# This widget allows the user to search for a house in the database

class SearchHouseWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui_files", "QSearchHouse.ui")
        loadUi(ui_file, self)

    # Method to fill the fields with the information of the selected house
    def fill_the_fields(self, id):
        database = DBConnection()
        self.id = id
        flag = False

        # Searches the house by id in the database
        house = database.select_by_id(id)

        if house is not None:
            flag = True

            # Fills the fields
            self.id_lineEdit.setText(str(id))
            self.address1_lineEdit.setText(house.get_address1())
            self.address2_lineEdit.setText(house.get_address2())
            self.city_lineEdit.setText(house.get_city())
            self.state_lineEdit.setText(house.get_state())
            self.postalcode_lineEdit.setText(house.get_postalcode())
            self.country_lineEdit.setText(house.get_country())
            self.size_lineEdit.setText(str(house.get_house_size()))
            self.date_lineEdit.setText(str(house.get_registerDate()))

            # Gets the path of the photo and inserts it in the frame
            photo_path = house.get_photo()
            pixmap = QPixmap(photo_path)

            if not pixmap.isNull():
                self.imageLabel.setPixmap(pixmap.scaled(
                    self.imageLabel.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
            else:
                print("Failed to load image.")

        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("House ID")
            msgBox.setText(f"ID {id} not found")
            msgBox.exec()

        database.close()

        return flag
