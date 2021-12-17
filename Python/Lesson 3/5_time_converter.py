# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.
# Текст состоит из чисел, пробелом и английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.

def time_converter(time):
    # replace this for solution
    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
