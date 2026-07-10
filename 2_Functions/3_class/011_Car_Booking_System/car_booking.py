# Cab Booking management system
class Cab:
    def __init__(self, cab_id, cab_number, cab_type, fare_per_km):
        self.cab_id = cab_id
        self.cab_number = cab_number
        self.cab_type = cab_type
        self.fare_per_km = fare_per_km
        self.available = True

    def display(self):
        status = 'Available' if self.available else "Booked"
        print(f"{self.cab_id} \t{self.cab_number}\t{self.cab_type}\t{self.fare_per_km}\t{status}")

class Driver:
    def __init__(self, driver_id, name, phone):
        self.driver_id = driver_id
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.driver_id}\t{self.name}\t{self.phone}")

class Booking:
    def __init__(self, booking_id, customer_name, cab, pickup, drop, distance):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.cab = cab
        self.pickup = pickup
        self.drop = drop
        self.distance = distance
        self.fare = distance * cab.fare_per_km

    def display(self):
        print("{self.booking_id}\t{self.customer_name}\t{self.cab.cab_number}\t{self.pickup}\t{self.drop}\t{self.distance}\t{self.fare}")

class CabBookingSystem:
    def __init__(self):
        self.cabs = []
        self.drivers = []
        self.bookings = []

    def find_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None
    
    #Add Cab
    def add_cab(self):
        cab_id = int(input("Enter Cab ID:"))
        cab_number = input("enter cab number:")
        cab_type = input("Enter cab Type (Mini/Sedan/SUV):")
        rate = float(input("Enter Rate Per Km:"))

        self.cabs.append(Cab(cab_id, cab_number, cab_type, rate))

        print("Cab Added Successfully!")

    #Add Driver
    def add_driver(self):
        driver_id =int(input("Enter Driver ID:"))
        name = input("Enter Driver Name:")
        phone = input("Enter Phone Number:")

        self.drivers.append(Driver(driver_id, name, phone))

        print("Driver Added Successfully!")

    #Book Cab
    def book_cab(self):
        booking_id = int(input("Enter booking ID:"))
        customer = input("Enter customer name:")
        cab_id = int(input("Enter Cab ID:"))
        pickup = input("Enter pickup Location:")
        drop = input("Enter Drop Location:")
        distance = float(input("Enter Distance (KM):"))

        cab = self.find_cab(cab_id)

        if cab and cab.available:
            cab.available = False

            booking = Booking(booking_id, customer, cab, pickup, drop, distance)

            self.bookings.append(booking)

            print("Cab Booked Successfully!")
            print("Fare = ", booking.fare)

        else:
            print("cab Not Available")

    # Cancel Booking
    def cancel_booking(self):
        booking_id = int(input("Enter Booking ID:"))

        booking = self.find_booking(booking_id)

        if booking:
            booking.cab.available = True

            self.bookings.remove(booking)

            print("Booking Removed Successfully!")
        else:
            print("No Booking Found!")
        
    # View Cabs
    def view_cabs(self):
        print("\nID\tCab_number\tType\tRate/KM\tstatus")
        print("--------------------------------------------")

        for cab in self.cabs:
            cab.display()

    # View Drivers
    def view_drivers(self):
        print("\nDirver ID\tDriver_name\tPhone")
        print("----------------------------------")

        for driver in self.drivers:
            driver.display()

    # View Bookings
    def view_bookings(self):
        print("\nBookingID\tCustomer\tCab\tPickup\tDrop\tFare")
        print("------------------------------------")

        for booking in self.bookings:
            booking.display()

    # Revenue
    def calculate_revenue(self):
        revenue = sum(b.fare for b in self.bookings)
        print(f"\n Total Revenue = Rs.{revenue}")

system = CabBookingSystem()

while True:
    print("\n========= Cab Booking Management System =======")
    print("1. Add Cab")
    print("2. Add Driver")
    print("3. Book Cab")
    print("4. Cancel Booking")
    print("5. View Cabs")
    print("6. View Drivers")
    print("7. View Bookings")
    print("8. Calculate Revenue")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        system.add_cab()
    if choice == 2:
        system.add_driver()
    if choice == 3:
        system.book_cab()
    if choice == 4:
        system.cancel_booking()
    if choice == 5:
        system.view_cabs()
    if choice == 6:
        system.view_drivers()
    if choice == 7:
        system.view_bookings()
    if choice == 8:
        system.calculate_revenue()
    elif choice == 9:
        print("Thank you for using cab booking system.")
        break
    else:
        print("Invalid Choice!")