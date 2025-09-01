# Importing MySQL library
import pymysql

# Importing House class
from House import House


# This class is responsible for connecting the database to the application.
# It provides various queries, including searching for a single house or
# all houses, as well as adding and modifying Real Estate records.

class DBConnection:
    def __init__(self):
        self.cursor = None

        try:
            #Connects to the RealStateDB database in mySQL
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="NewPassword123!",
                database="RealStateDB",
                autocommit=True
            )

            # All queries used
            self.select_all_except_photo_query = "SELECT houseID, address1, address2, city, state, postalcode, country, house_size, registerDate FROM realstate"
            self.select_by_id_query = "SELECT * FROM realstate where houseID=%s"
            self.insert_query = "INSERT INTO realstate (address1, address2, city, state, postalcode, country, photo, house_size, registerDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.update_query = "UPDATE realstate set address1=%s, address2=%s, city=%s, state=%s, postalcode=%s, country=%s, photo=%s, house_size=%s, registerDate=%s where houseID=%s"

            self.cursor = self.db.cursor()
            
            # Test the connection with a simple query
            self.cursor.execute("SELECT 1")
            
        except Exception as ex:
            print(f"Database connection error: {str(ex)}")
            print("Please check that:")
            print("1. MySQL server is running")
            print("2. The password is correct")
            print("3. The database 'RealStateDB' exists")
            print("4. The user 'root' has proper permissions")
            raise

    # Method to add a new house
    def add(self, house):
        self.cursor.execute(self.insert_query, house.get_insert_values())
        self.db.commit()

        return self.cursor.rowcount, self.cursor.lastrowid

    # Method to get all the houses
    def select_all_houses(self):
        self.cursor.execute(self.select_all_except_photo_query)

        return self.cursor

    # Search for a house based on the id
    def select_by_id(self, id):
        house = None
        values = (id,)

        self.cursor.execute(self.select_by_id_query, values)
        my_result = self.cursor.fetchall()

        if len(my_result) > 0:
            for record in my_result:
                houseID, address1, address2, city, state, postalcode, country, photo, house_size, registerDate,  = record

            house = House(address1, address2, city, state, postalcode, country, photo, house_size, registerDate, houseID)

        return house

    # Method to modify a house
    def update(self, house):
        self.cursor.execute(self.update_query, house.get_update_values())
        self.db.commit()

        return self.cursor.rowcount

    # Method that close the database
    def close(self):
        self.cursor.close()
        self.db.close()
