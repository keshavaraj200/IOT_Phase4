class SmartParking:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def check_availability(self):
        return self.available_spaces

    def park(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print("Car parked. Available spaces:", self.available_spaces)
        else:
            print("Parking lot is full. Cannot park.")

    def leave(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            print("Car left. Available spaces:", self.available_spaces)
        else:
            print("Parking lot is already empty.")

def main():
    total_spaces = 10  # Change this to the desired number of parking spaces
    parking_lot = SmartParking(total_spaces)

    while True:
        print("Options:")
        print("1. Check availability")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            print("Available spaces:", parking_lot.check_availability())
        elif choice == '2':
            parking_lot.park()
        elif choice == '3':
            parking_lot.leave()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
