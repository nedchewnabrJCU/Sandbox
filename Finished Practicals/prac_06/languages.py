from programming_language import ProgrammingLanguage
from programming_language import language_test


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(str(ruby))
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(str(python))
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(str(visual_basic))
    languages = [ruby, python, visual_basic]
    language_test(languages)

main()