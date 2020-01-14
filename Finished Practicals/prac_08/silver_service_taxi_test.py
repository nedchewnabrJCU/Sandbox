from silver_service_taxi import SilverServiceTaxi


def main():
    """Testing of silver_service_taxi.py"""
    taxi = SilverServiceTaxi("Limo Taxi", 100, 5)
    taxi.drive(11)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))


main()
