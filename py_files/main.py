import sys

from PyQt6.QtGui import QIcon
# Importing PyQt6 libraries
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox

# Importing UI classes
from QAddHouse import AddHouseWidget
from QModifyHouse import ModifyHouseWidget
from QReport import ReportWidget
from QSearchHouse import SearchHouseWidget


# This the main application where open the app menu
# in QMenuHouse.ui. This application manages all the Real Estate information,
# from adding, modifying, and viewing their information. Additionally, we can
# view the list of all houses.

class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the application
        self.app = QApplication(sys.argv)

        super().__init__()
        self.window = loadUi("QMenuHouse.ui", self)

        self.setFixedSize(400, 400)
        # Instantiating UI objects
        self.addHouse = AddHouseWidget()
        self.modifyHouse = ModifyHouseWidget()
        self.searchHouse = SearchHouseWidget()
        self.houseReport = ReportWidget()

        # Signals and Slots (menu with methods or UI)
        self.actionModify_a_House.triggered.connect(self.modify_house)  # calling method
        self.actionAdd_a_House.triggered.connect(self.addHouse.show)  # calling UI
        self.actionSearch_for_a_House.triggered.connect(self.search_house)
        self.actionReport.triggered.connect(self.houseReport.show)

        self.actionExit.triggered.connect(self.quitApp)  # calling method

        self.actionAbout.triggered.connect(self.aboutMessage)
        self.actionHelp_Contents.triggered.connect(self.helpMessage)

        # Display the window
        self.window.show()

    # Quit from App
    def quitApp(self):
        sys.exit(0)

    # Method for class SearchHouseWidget()
    def search_house(self):
        id_str, ok = QInputDialog().getText(self, "Search for a House", "Enter an ID:")

        if ok:
            id = int(id_str)
            flag = self.searchHouse.fill_the_fields(id)

            if flag:
                # Display the window
                self.searchHouse.show()

    # Method for class ModifyHouseWidget()
    def modify_house(self):
        id_str, ok = QInputDialog().getText(self, "Modify a House", "Enter an ID:")

        if ok:
            id = int(id_str)
            flag = self.modifyHouse.fill_the_fields(id)

            if flag:
                # Display the window
                self.modifyHouse.show()

    # Message for Help -> About
    def aboutMessage(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("About")
        msgBox.setText("Team members:\n\nEdgardo Reyes")
        msgBox.setWindowIcon(QIcon("icon.png"))
        msgBox.exec()

    # Message for Help -> Help Contents
    def helpMessage(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Help")
        msgBox.setText(
            "File -> Add a House: To add a house to the database\n\nFile -> Modify a House: To modify a house\n\nFile -> Search for a House: To view a specific house\n\nFile -> Report: To view all houses: \n\nFile -> Exit: To exit")
        msgBox.setWindowIcon(QIcon("icon.png"))
        msgBox.exec()

    # Display the window app
    def run(self):
        sys.exit(self.app.exec())


# Instantiate the class MainWindow()
# and execute this app
def main():
    app = MainWindow()
    app.run()


if __name__ == '__main__':
    main()  # call main() method
