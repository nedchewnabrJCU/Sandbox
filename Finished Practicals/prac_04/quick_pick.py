from random import randint
MIN_PICK = 1
MAX_PICK = 45


def main():
    number_test_one = False
    # quick_picks = 0
    while not number_test_one:
        quick_picks = input("How many quick picks? ")
        if not quick_picks.isdigit():
            print("Invalid input; enter a valid number")
        else:
            quick_picks = int(quick_picks)
            number_test_one = True
    for n in range(0, quick_picks):
        lottery_list = []
        for i in range(0, 6):
            number_test_two = False
            while not number_test_two:
                number_random = randint(MIN_PICK, MAX_PICK)
                if number_random not in lottery_list:
                    lottery_list.append(number_random)
                    number_test_two = True
        lottery_list.sort()
        for x in range(0, 6):
            print("{:2}".format(lottery_list[x]), end=" ")
        print("")


main()
