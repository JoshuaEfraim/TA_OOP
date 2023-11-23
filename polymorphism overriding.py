from TAhouse import House
class Apartment(House):
    def __init__(self, floors, doors, windows, color, has_garage, address, num_units):
        super().__init__(floors, doors, windows, color, has_garage, address)
        self.num_units = num_units

    def display_info(self):
        print("Apartment information: ")
        print(f"      -Address: {self.address}")
        print(f"      -Doors: {self.doors}")
        print(f"      -Floors: {self.floors}")
        print(f"      -Windows: {self.windows}")
        print(f"      -Color: {self.color}")
        print(f"      -Garage: {'Yes' if self.has_garage else 'no'}")
        print(f"      -Number of Units: {self.num_units}")

apartment = Apartment(floors=5, doors=20, windows=50, color='Beige', has_garage=False, address='123 Main St', num_units=10)

apartment.display_info()