# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.
# Текст состоит из чисел, пробелом и английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.

def sum_numbers(text: str) -> int:
    # your code here
    pass


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
