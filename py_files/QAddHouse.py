import os
import shutil
import sys

# Importing date libraries for the register date
from datetime import datetime, date

# Importing PyQt6 libraries
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
from PyQt6.QtGui import QPixmap

# Importing database connection
from DBConnection import DBConnection
# Importing House class
from House import House


# This widget allows the user to add a house into the database

class AddHouseWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui_files", "QAddHouse.ui")
        loadUi(ui_file, self)
        self.date_lineEdit.setText(str(date.today())) # Automatically sets the register date to today's date
        self.current_image_path = None # Instantiates the file path variable of the house image

    # Method for adding the new house
    def add_house_clicked(self):

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


        # Connects with the database
        database = DBConnection()

        # Extracts all the information filled in the widget
        address1 = self.address1_lineEdit.text()
        address2 = self.address2_lineEdit.text()
        city = self.city_lineEdit.text()
        state = self.state_lineEdit.text()
        postalcode = self.postalcode_lineEdit.text()
        country = self.country_lineEdit.text()
        photo = self.current_image_path
        size = float(self.size_lineEdit.text())
        date = self.date_lineEdit.text()

        # Creates a House object with that information
        house = House(address1, address2, city, state, postalcode, country, photo, size, date)

        # Adds the house to the database using the add method in DBConnection
        rows, id = database.add(house)

        database.close()

        msgBox = QMessageBox()

        if rows == 1:
            msg = f"{rows} record inserted with ID {id}"
        else:
            msg = "Database error"

        msgBox.setWindowTitle("Add House")
        msgBox.setText(msg)
        msgBox.exec()

        self.hide()

    # Method to load the image of the house using QFileDialog
    def load_image(self):
        # Opens the QFileDialog menu
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        if file_path:
            pixmap = QPixmap(file_path)

            # Resizes the image to fit well

            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.imageLabel.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.imageLabel.setPixmap(scaled_pixmap)

                self.current_image_path = file_path # Sets the path of the image

if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = AddHouseWidget()
    add.show()
    sys.exit(app.exec())