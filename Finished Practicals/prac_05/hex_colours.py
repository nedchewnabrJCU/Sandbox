COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name_input = input("Enter a colour name: ")
while colour_name_input != "":
    print("The colour code of {} is {}".format(colour_name_input, COLOUR_NAMES.get(colour_name_input)))
    colour_name_input = input("Enter a colour name: ")