# Importing PyQt6 libraries
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow
# Importing database connection
from DBConnection import DBConnection

# This widget lists all the houses

class ReportWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("QReport.ui", self)
        self.update_report()


    # This method allows to refresh the list of houses
    def update_report(self):
        database = DBConnection()

        # Selects all the houses in the database except for the photo column
        all_employees_cursor = database.select_all_houses()

        # Creates a variable for the table view widget
        tableWidget = self.report_tableView

        # Creates the model for the table itself
        model = QStandardItemModel()

        # Sets the headers
        model.setHorizontalHeaderLabels(
            ['houseID', 'Address1', 'Address2', 'City', 'State', 'Postal Code', 'Country', 'House Size',
             'Register Date'])

        row = 0

        # Populates the table with the data of all the houses
        for (houseID, address1, address2, city, state, postalcode, country, house_size,
             registerDate) in all_employees_cursor:
            array_data = [str(houseID), address1, address2, city, state, postalcode, country, str(house_size),
                          str(registerDate)]

            for col in range(9):
                item = QStandardItem()

                value = array_data[col]

                item.setData(value, 0)

                model.setItem(row, col, item)

            row = row + 1

        tableWidget.setModel(model)

        database.close()


