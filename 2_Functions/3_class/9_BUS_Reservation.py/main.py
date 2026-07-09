class Bus:
    def  __init__(self, bus_id, bus_name, source, destination, seats, fare):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.available_seats = seats
        self.fare = fare

    def display(self):
        print( f"{self.bus_id}\t{self.bus_name}\t{self.source}\t{self.destination}\t{self.seats}\t{self.available_seats}\t{self.fare}")

class Reservation:
    def __init__(self, booking_id, passenger_name, bus, seats_booked):
        self.booking_id = booking_id
        self.passenger_name = passenger_name
        self.bus = bus
        self.seats_booked = seats_booked
        self.total_fare = seats_booked * bus.fare

    def display(self):
        print(f"{self.booking_id}\t{self.passenger_name}\t{self.bus}\t{self.seats_booked}\t{self.total_fare}")

class busReservationSystem:
    def __init__(self):
        self.buses = []
        self.reservations = []

    def find_bus(self, bus_id):
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
        return None
    
    def find_reservation(self, booking_id):
        for reservation in self.reservations:
            if reservation.booking_id == booking_id:
                return reservation
        return None
    
    # Add Bus
    def add_bus(self):
        bus_id = int(input("Enter Bus ID:"))
        name = input("Enter Bus Name:")
        source = input("Enter source")
        destination = input("Enter destination: ")
        seats = int(input("Enter Total Seats: "))
        fare = float(input("Enter fare per Seats:"))

        self.buses.append(Bus(bus_id, name, source, destination, seats, fare))

        print("BUS Added Successfully!")

    # View Bus
    def View_buses(self):
        print("\nID: \tBus \t source \tdestination \t seats \tfare ")
        print("------------------------------------")

        for bus in self.buses:
            bus.display()

    def book_Ticket(self):
        booking_id = int(input("Enter Booking Id:"))
        passenger = input("Enter Passenger name:")
        bus_id  = int(input("Enter Bus ID:"))
        seats = int(input("Enter Number of seats:"))

        bus = self.find_bus(bus_id)

        if bus:
            if seats <= bus.available_seats:
                bus.avilable_seats -= seats

                reservation = Reservation(
                    booking_id, passenger, bus, seats
                )
                self.reservations.append(reservation)

                print("Ticket Booking Successfully")
                print("Total Fare: " + reservation.total_fare)
            else:
                print("Seats Not Available")
        else:
            print("Bus Not Found")

    #Cancel Ticket
    def cancel_ticket(self):
         booking_id = int(input("Enter Booking ID:"))

         reservation = self.find_reservation(booking_id)

         if reservation:
             reservation.bus.available_seats += reservation.seats_booked
             self.reservations.remove(self.reservation)

             print("Ticket Canceled Successfully")

         else:
             print("Booking Not Found")


    #View Reservation 
    def view_reservations(self):
        print("\nBookingID\tpassenger\tbus\tSeats\tFare")
        print("-------------------------------------")

        for reservation in self.reservations:
            reservation.display()

    def search_bus(self):
        bus_id = int(input("Enter Bus ID:"))
        bus = self.find_bus(bus_id)

        if bus:
           print("\nID\tBus\tSource\tDestination\tseats\tfare")
           print("-----------------------------------------")
    
           bus.display()
        else:
            print("Bus Not Found")

    # Revenue
    def calculate_revenue(self):
        revenue = sum(r.total_fare for r in self.reservations)
        print(f"\n Total Revenue = Rs {revenue}")

    # Main Program

system = busReservationSystem()
    
while True:
        print("\n======= Bus Reservation System =======")
        print("1. Add Bus")
        print("2. view Buses")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. View Reservations")
        print("6. Search Bus")
        print("7. Calculate Revenue")
        print("8. Exit")

        choice = int(input("Enter Choice: "))

        if choice ==1:
            system.add_bus()
        elif choice ==2:
            system.View_buses()
        elif choice == 3:
            system.book_Ticket()
        elif choice ==4:
            system.cancel_ticket()
        elif choice == 5:
            system.view_reservations()
        elif choice == 6:
            system.search_bus()
        elif choice == 7:
            system.calculate_revenue()
        elif choice ==8:
            print("System Closed!")
            break
        else:
            print("Invalid Choice!")
