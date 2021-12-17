# Класические крестики нолики
# Вам дан список с текстовыми значениями
# Нужно определить кто выиграл крестики или нолики
# Входные данные: Список.
# Выходные данные: Строка.

def check(game_result):
    pass


if __name__ == '__main__':
    assert check([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert check([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert check([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert check([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
