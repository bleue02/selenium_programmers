def coding_Level_xpath():
    levels = {
        'Level.0': "(//li[@class='item'])[1]",
        'Level.1': "(//li[@class='item'])[2]",
        'Level.2': "(//li[@class='item'])[3]",
        'Level.3': "(//li[@class='item'])[4]",
        'Level.4': "(//li[@class='item'])[5]",
        'Level.5': "(//li[@class='item'])[6]",
    }
    return levels


def coding_Language_xpath():
    langs = {
        'C': "(//li[@class='item'])[1]",
        'C++': "(//li[@class='item'])[2]",
        'C#': "(//li[@class='item'])[3]",
        'Go': "(//li[@class='item'])[4]",
        'Java': "(//li[@class='item'])[5]",
        'JavaScript': "(//li[@class='item'])[6]",
        'Kotlin': "(//li[@class='item'])[7]",
        'Python2': "(//li[@class='item'])[8]",
        'Python3': "(//li[@class='item'])[9]",
        'Ruby': "(//li[@class='item'])[10]",
        'Scala': "(//li[@class='item'])[11]",
        'Swift': "(//li[@class='item'])[12]",
        'MySQL': "(//li[@class='item'])[13]",
        'Oracle': "(//li[@class='item'])[14]",
    }
    return langs

def coding_Language_xpath_numbers():
    langs = {
        1: "(//li[@class='item'])[1]",  # C
        2: "(//li[@class='item'])[2]",  # C++
        3: "(//li[@class='item'])[3]",  # C#
        4: "(//li[@class='item'])[4]",  # Go
        5: "(//li[@class='item'])[5]",  # Java
        6: "(//li[@class='item'])[6]",  # JavaScript
        7: "(//li[@class='item'])[7]",  # Kotlin
        8: "(//li[@class='item'])[8]",  # Python2
        9: "(//li[@class='item'])[9]",  # Python3
        10: "(//li[@class='item'])[10]",  # Ruby
        11: "(//li[@class='item'])[11]",  # Scala
        12: "(//li[@class='item'])[12]",  # Swift
        13: "(//li[@class='item'])[13]",  # MySQL
        14: "(//li[@class='item'])[14]",  # Oracle
    }
    return langs


import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def select_level():
    level = coding_Level_xpath()
    clear()
    for index, level in enumerate(level, start=1):
        print(f'{index} {level}\n')
    user_select_level = int(input('Please Select Level: '))
    return user_select_level


def select_lang():
    languages = coding_Language_xpath()
    for index, language in enumerate(languages, start=1):
        print(f'{index}. {language}\n')
    user_select_language = int(input('Select Language: '))
    selected_language = list(languages.keys())[user_select_language - 1]
    return user_select_language, selected_language
user_select_languages, _ = select_lang()