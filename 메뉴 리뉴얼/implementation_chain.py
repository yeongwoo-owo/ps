from itertools import combinations, chain


def solution(orders, course):
    orders = [sorted(order) for order in orders]
    result = chain(*[create_course_menus(orders, size) for size in course])
    return sorted(result)


def create_course_menus(orders, size):
    candidates = list(chain(*[combinations(order, size) for order in orders]))
    order_map = {order: candidates.count(order) for order in set(candidates)}
    max_order_count = max(order_map.values()) if order_map else 0
    return [''.join(k) for k, v in order_map.items() if v == max_order_count] if max_order_count > 1 else []


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
