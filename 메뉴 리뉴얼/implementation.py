from itertools import combinations


def solution(orders, course):
    orders = [sorted(order) for order in orders]
    course_menus = []
    for size in course:
        course_menus += create_course_menus(orders, size)
    return sorted(course_menus)


def create_course_menus(orders, size):
    candidates = []
    for order in orders:
        candidates += combinations(order, size)
    order_map = {order: candidates.count(order) for order in set(candidates)}
    max_order_count = max(order_map.values()) if order_map else 0
    return [''.join(k) for k, v in order_map.items() if v == max_order_count] if max_order_count > 1 else []


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
