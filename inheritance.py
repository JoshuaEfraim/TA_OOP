from TAhouse import House

class Apartment(House):
    total_apartments = 0

    def __init__(self, floors, doors, windows, color, has_garage, address, num_units, has_security_system):
        super().__init__(floors, doors, windows, color, has_garage, address)
        self.num_units = num_units
        self.has_security_system = has_security_system

        Apartment.total_apartments += 1

    def display_info(self):
        super().display_info()
        print(f"      -Number of Units: {self.num_units}")
        print(f"      -Security System: {'Yes' if self.has_security_system else 'No'}")

    @classmethod
    def display_total_apartments(cls):
        print(f"Total number of apartments = {cls.total_apartments}")
    def install_security_system(self):
        if self.has_security_system:
            print("Security system already installed")
        else:
            self.has_security_system = True

        return self.has_security_system
    
    def validate_apartment(apartment):
        if not House.validate_house(apartment):
            return False 
        if not isinstance(apartment.num_units, int) or apartment.num_units <= 0:
            return False  

    
apartment1 = Apartment(floors=5, doors=10, windows=20, color='White', has_garage=True, address='123 Main St', num_units=10, has_security_system=False)
apartment1.display_info()

apartment1.paint_house()
apartment1.install_security_system()
House.display_total_house()
Apartment.display_total_apartments()


if Apartment.validate_apartment(apartment1):
    print("Apartment is valid.")
else:
    print("Apartment is not valid.")
    