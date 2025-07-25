
class House:
    def __init__(self, address1='', address2=None, city='', state='', postalcode = '', country = '', photo='', house_size = 0.0, registerDate=None, houseID=None):
        self.__address1 = address1
        self.__address2 = address2
        self.__city = city
        self.__state = state
        self.__postalcode = postalcode
        self.__country = country
        self.__photo = photo
        self.__house_size = house_size
        self.__registerDate = registerDate
        self.__houseID = houseID

    # Getters
    def get_houseID(self):
        return self.__houseID

    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_postalcode(self):
        return self.__postalcode

    def get_country(self):
        return self.__country

    def get_photo(self):
        return self.__photo

    def get_house_size(self):
        return self.__house_size

    def get_registerDate(self):
        return self.__registerDate

    # Setters
    def set_houseID(self, houseID):
        self.__houseID = houseID

    def set_address1(self, address1):
        self.__address1 = address1

    def set_address2(self, address2):
        self.__address2 = address2

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_postalcode(self, postalcode):
        self.__postalcode = postalcode

    def set_country(self, country):
        self.__country = country

    def set_photo(self, photo):
        self.__photo = photo

    def set_house_size(self, house_size):
        self.__house_size = house_size

    def set_registerDate(self, registerDate):
        self.__registerDate = registerDate

    # Return values to be inserted
    def get_insert_values(self):
        return self.__address1, self.__address2, self.__city, self.__state, self.__postalcode, self.__country, self.__photo, self.get_house_size(), self.__registerDate

    # Return values to update a house
    def get_update_values(self):
        return self.__address1, self.__address2, self.__city, self.__state, self.__postalcode, self.__country, self.__photo, self.__house_size, self.__registerDate, self.__houseID
