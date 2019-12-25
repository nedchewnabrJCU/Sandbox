from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i, guitar in enumerate(guitars):
        vintage_check = ""
        if guitar.is_vintage():
            vintage_check = "(vintage)"
        print("Guitar {}: {} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name,
                                                                  guitar.year, guitar.cost, vintage_check))


main()
