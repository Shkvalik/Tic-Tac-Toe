def array_diff(a, b):
    list_difference = []
    for item in a:
        if item not in b:
            list_difference.append(item)
    return list_difference



def assert_equals(a, b, c):
    assert a == b, c


if __name__ == '__main__':
    assert_equals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    assert_equals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
    assert_equals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    assert_equals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
    assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
    assert_equals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")
