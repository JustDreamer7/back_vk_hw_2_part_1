"""Домашняя работа №2 - 1-ая часть"""
class ModifiedList(list):
    """Модифицированный список, который меняет методы арифметических операций"""
    #     def __init__(self, values):
    #         self.extend(values)
    def __add__(self, other):
        new_mod_lst = ModifiedList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x + y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend(other[min_len:])
        return new_mod_lst

    def __radd__(self, other):
        return self + ModifiedList(other)

    def __sub__(self, other):
        new_mod_lst = ModifiedList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x - y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend([x - y for x, y in zip([0] * len(other[min_len:]), other[min_len:])])
        return new_mod_lst

    def __rsub__(self, other):
        return ModifiedList(other) - self

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)


if __name__ == "__main__":
    a = ModifiedList([2, 3, 4, 5])
    b = ModifiedList([3, 4, 5, 6, 7, 8])
    print(f'Разность двух модифицированных списков: {a - b}')
    print(f'Сумма двух модифицированных списков: {a + b}')
    print(f'Сумма списка и  модифицированного списка: {[1, 2, 3] + a}')
    print(f'Разность списка и  модифицированного списка: {[1, 2, 3] - b}')
    print(f'Сравниваем два списка: {[2, 1, 3, 4] > [2, 3, 4]}')
    print(f'Сравниваем два модифицированных списка: {ModifiedList([2, 1, 3, 4]) > ModifiedList([2, 3, 4])}')
