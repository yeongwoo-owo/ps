from itertools import combinations, chain
from collections import Counter


def solution(orders, course):
    orders = [sorted(order) for order in orders]
    result = chain(*[create_course_menus(orders, size) for size in course])
    return sorted(result)


def create_course_menus(orders, size):
    candidates = list(chain(*[combinations(order, size) for order in orders]))
    menu_and_count = Counter(candidates).most_common()
    max_order_count = menu_and_count[0][1]
    return [''.join(k) for k, v in menu_and_count if v == max_order_count] if max_order_count > 1 else []


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
