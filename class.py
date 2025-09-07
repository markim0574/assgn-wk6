# Assignment 1: Smartphone Classes
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # default battery level

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is now fully charged.")

    def check_battery(self):
        print(f"Battery level: {self.battery}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def charge(self):  # Polymorphism
        self.battery = 100
        print(f"{self.brand} {self.model} (Gaming Edition) charges extra fast ⚡!")

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} graphics card 🎮")

# Activity 2: Polymorphism with Vehicles
class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Interactive Menu
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Test Smartphone")
        print("2. Test Gaming Phone")
        print("3. Vehicle Polymorphism")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            phone = Smartphone("Samsung", "Galaxy S23", "256GB")
            phone.make_call("123456789")
            phone.check_battery()
            phone.charge()

        elif choice == "2":
            g_phone = GamingPhone("Asus", "ROG Phone 7", "512GB", "Adreno 730")
            g_phone.play_game("PUBG")
            g_phone.check_battery()
            g_phone.charge()

        elif choice == "3":
            vehicles = [Car(), Plane(), Boat()]
            for v in vehicles:
                v.move()

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Try again.")

# Run program
if __name__ == "__main__":
    main()
