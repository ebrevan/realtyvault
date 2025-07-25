import os
import shutil

# Importing PyQt6 libraries
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog

# Importing database connection library
from DBConnection import DBConnection
# Importing House class
from House import House


# This widget allows the user to modify a house in the database

class ModifyHouseWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("QModifyHouse.ui", self)

        self.id = -1
        self.current_image_path = None

    # Method to fill the fields with the information of the selected house
    def fill_the_fields(self, id):

        database = DBConnection()
        self.id = id
        flag = False

        # Searches the house by id in the database
        house = database.select_by_id(id)

        # If the house is found then
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

            # Resizes the image to fit well
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

    def modify_house_clicked(self):

        # Saves the image selected to a folder called "images" located in the project folder
        if self.current_image_path:
            # Create destination folder for house image if it doesn't exist
            dest_folder = os.path.join(os.getcwd(), "images")
            os.makedirs(dest_folder, exist_ok=True)

            # Get original filename (e.g., house1.jpg)
            file_name = os.path.basename(self.current_image_path)

            # Define destination path
            dest_path = os.path.join(dest_folder, file_name)

            # Copy image to destination folder
            shutil.copy(self.current_image_path, dest_path)

            # Print message confirming image saved
            print("Saved image to:", dest_path)

            # Sets the final destination path as the current path of the image
            self.current_image_path = dest_path

        database = DBConnection()

        id = self.id_lineEdit.text()
        address1 = self.address1_lineEdit.text()
        address2 = self.address2_lineEdit.text()
        city = self.city_lineEdit.text()
        state = self.state_lineEdit.text()
        postalcode = self.postalcode_lineEdit.text()
        country = self.country_lineEdit.text()
        photo = self.current_image_path
        size = float(self.size_lineEdit.text())
        date = self.date_lineEdit.text()

        house = House(address1, address2, city, state, postalcode, country, photo, size, date, id)

        rows = database.update(house)

        database.close()

        msgBox = QMessageBox()

        if rows == 1:
            msg = f"{rows} record updated"
        else:
            msg = "Database error"

        msgBox.setWindowTitle("Modify a House")
        msgBox.setText(msg)
        msgBox.exec()

        self.hide()

    # Method to load the image of the house using QFileDialog
    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        # Resizes the image to fit well

        if file_path:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.imageLabel.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.imageLabel.setPixmap(scaled_pixmap)

                self.current_image_path = file_path # Sets the path of the image
