class House:
    
    total_house = 0
    
    def __init__(self, floors, doors, windows, color, has_garage, address):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address
        
        House.total_house += 1
    
    def display_info(self):
        #Display information
        print("House information: ")
        print(f"      -Address: {self.address}")
        print(f"      -Doors: {self.doors}")
        print(f"      -Floors: {self.floors}")
        print(f"      -Windows: {self.windows}")
        print(f"      -Color: {self.color}")
        print(f"      -Garage: {'Yes' if self.has_garage else 'no'}")
    
    @classmethod
    def display_total_house(cls):
        print(f"Total number of houses = {cls.total_house}")
    
    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False #not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False #floors, doors, windows should be positive int
        
        return True
    
    def paint_house(self):
        newColor = str(input("Enter the new paint color: "))
        self.color = newColor

        return self.color
    
    def add_garage(self):
        if self.has_garage == True:
            print("Already have garage")
        else:
            self.has_garage = True

        return self.has_garage
    
    def set_address(self, new_address):
        self.address = new_address
        print(self.address)
        return self.address

        

house1 = House(floors = 2, doors = 3, windows = 6, color = "Blue", has_garage= True, address= "123 Main st.")
house2 = House(floors = 3, doors = 3, windows = 9, color = "yellow", has_garage= False, address= "123 Main st.")

house1.display_info()
print()
house2.display_info()
House.display_total_house()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")

house1.paint_house()
house1.add_garage()
house1.set_address("blabla st.")




