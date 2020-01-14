from unreliable_car import UnreliableCar


def main():
    working_car = UnreliableCar("Working Car", 100, 90)
    broken_car = UnreliableCar("Broken Car", 100, 10)
    """Test cars driving different distances"""
    for i in range(1, 11):
        print("Attempting to drive {}km:\n".format(i))
        """Test if working car could drive"""
        if working_car.drive(i) == 0:
            print("{} failed to drive {}km.".format(working_car.name, i))
        else:
            print("{} successfully drove {}km.".format(working_car.name, i))
        """Test if broken car could drive"""
        if broken_car.drive(i) == 0:
            print("{} failed to drive {}km.".format(broken_car.name, i))
        else:
            print("{} successfully drove {}km.".format(broken_car.name, i))
        print("\n")
    """Final Car Result"""
    print(working_car)
    print(broken_car)


main()
