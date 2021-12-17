from typing import List, Any


def unique_list(elements: List[Any]) -> list:
    return list(set(elements))


if __name__ == '__main__':
    print("Example:")
    print(unique_list([1, 1, 2, 3, 2, 5]))

    assert unique_list([1, 1, 1]) == [1]
    assert unique_list([1, 2, 1]) == [1, 2]
    assert unique_list(['a', 'a', 'a']) == ['a']
    assert unique_list(['a', 'b', 'b']) == ['a', 'b']
    assert unique_list([]) == []
    assert unique_list([1]) == [1]