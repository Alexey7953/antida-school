"""
Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.
"""

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Сортируем в порядке возрастания:
result = set(sorted(d.items(), key=operator.itemgetter(1)))
# И в порядке убывания:
result = set(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

