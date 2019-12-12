"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state (Type ALL to print all states): ")
while state != "":
    state = state.upper()
    if state == "ALL":
        for x, y in STATE_NAMES.items():
            print("{:3} is {}".format(x, y))
    elif state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state (Type ALL to print all states): ")
