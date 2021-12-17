# Вам дан список элементов.
# Нужно вернуть номер телефона в формате (888) 888-8888.
# Входные данные: Список.
# Выходные данные: Строка.


def create_phone_number(n) -> str:
    n = [str(i) for i in n]  # Transformation list element to str format [1, 2, 3] --> ['1', '2', '3']
    n.insert(0, '(')
    n.insert(4, ')')
    n.insert(5, ' ')
    n.insert(9, '-')
    return "".join(n)


def assert_equals(a, b, c=''):
    assert a == b, c


if __name__ == '__main__':
    assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
    assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
    assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
