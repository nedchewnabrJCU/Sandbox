from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """The user should be presented with a list of available taxis and get to choose one,
    Then they can choose how far they want to drive,
    At the end of each trip, show them the trip cost and add it to their bill."""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    menu_input = ""
    """Menu Loop until q is inputted"""
    while menu_input != "q":
        print("q)uit, c)hoose taxi, d)rive")
        menu_input = input(">>> ").lower()
        if menu_input == "c":
            """Choose taxi"""
            print("Taxis available: ")
            try:
                """Check if taxis variable exist"""
                display_taxis(taxis)
            except NameError:
                print("There are no taxis available.")
            else:
                taxi_input = int(input("Choose Taxi: "))
                selected_taxi = taxis[taxi_input]
        elif menu_input == "d":
            """Drive taxi"""
            try:
                """Check if user choose a taxi"""
                selected_taxi.start_fare()
            except UnboundLocalError:
                print("Taxi not selected. Please select a taxi first.")
            else:
                drive_distance = int(input("Drive how far? "))
                selected_taxi.drive(drive_distance)
                trip_fare = selected_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(selected_taxi.name, trip_fare))
                total_bill += trip_fare
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_bill))
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display each taxi in a list"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
