"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    score_check(score)


def score_check(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif 50 <= score <= 90:
        print("Passable")
    elif score < 50:
        print("Bad")

main()