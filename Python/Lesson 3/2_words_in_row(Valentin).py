# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв.
# Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.

def check(words):
    i = 0
    words = words.split(' ')  # Make list from string by split
    for elements in words:
        if elements.isalpha():  # Check if element has only liters
            i += 1
            if i == 3:
                return True
        else:
            i = 0
    return False


if __name__ == '__main__':
    assert check("Hello World hello") is True, "Hello"
    assert check("He is 123 man") is False, "123 man"
    assert check("1 2 3 4") is False, "Digits"
    assert check("bla bla bla bla") is True, "Bla Bla"
    assert check("Hi") is False, "Hi"
