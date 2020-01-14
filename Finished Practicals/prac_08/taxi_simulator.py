from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """The user should be presented with a list of available taxis and get to choose one,
    Then they can choose how far they want to drive,
    At the end of each trip, show them the trip cost and add it to their bill."""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    print("q)uit, c)hoose taxi, d)rive")
    menu_input = ""
    """"Menu Loop until q is inputted"""
    while menu_input != "q":
        menu_input = input(">>> ").lower()
        if menu_input == "c":
            """Choose taxi"""
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_input = int(input("Choose Taxi: "))
            selected_taxi = taxis[taxi_input]
        elif menu_input == "d":
            """Drive taxi"""
            selected_taxi.start_fare()
            drive_distance = int(input("Drive how far? "))
        else:
            print("Invalid Option")


def display_taxis(taxis):
    """Display each taxi in a list"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
