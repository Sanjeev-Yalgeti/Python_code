class Vehicle:
    def __init__(self, regno, brand, rate):
        self.regno = regno
        self.brand = brand
        self.rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if rate > 0:
            self._rate = rate

    def calculate_rental_cost(self, days):
        return self.rate * days

    def to_string(self):
        return f"{self.regno} {self.brand} {self.rate}"


class Bike(Vehicle):
    def calculate_rental_cost(self, days, capacity=0):
        if capacity > 500:
            return self.rate * days * 1.1
        return self.rate * days


class Car(Vehicle):
    def __init__(self, regno, brand, rate, door):
        super().__init__(regno, brand, rate)
        self.door = door

    def to_string(self):
        return f"{self.regno} {self.brand} {self.rate} {self.door}"


vehicles = {}

if __name__ == "__main__":
    while True:
        ch = int(input("1.Add\n2.Display\n3.Calculate\n4.Delete\n5.Exit\nEnter: "))

        if ch == 5:
            break

        match ch:
            case 1:
                vehtype = input("Enter type (CAR/BIKE): ")
                regno = input("Enter RegNo: ")
                brand = input("Enter brand: ")
                rate = int(input("Enter rate: "))

                if vehtype.upper() == "CAR":
                    door = int(input("Enter doors: "))
                    veh = Car(regno, brand, rate, door)
                elif vehtype.upper() == "BIKE":
                    veh = Bike(regno, brand, rate)
                else:
                    print("Invalid type")
                    continue

                vehicles[regno] = veh

            case 2:
                for v in vehicles.values():
                    print(v.to_string())

            case 3:
                reg = input("Enter RegNo: ")
                days = int(input("Enter days: "))

                if reg not in vehicles:
                    print("Vehicle not found")
                    continue

                if isinstance(vehicles[reg], Bike):
                    capacity = int(input("Enter capacity: "))
                    print(vehicles[reg].calculate_rental_cost(days, capacity))
                else:
                    print(vehicles[reg].calculate_rental_cost(days))

            case 4:
                reg = input("Enter RegNo: ")
                vehicles.pop(reg, None)