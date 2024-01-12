from time import time
from datetime import timedelta
from itertools import chain
from functools import reduce


def check_time(function):
    start = time()
    function()
    end = time()
    print("실행 시간:", timedelta(seconds=end - start), "sec")


data = [[i] for i in range(100000)]


def flatten_by_chain():
    print("chain")
    result = chain(*data)


def flatten_by_list_comprehension():
    print("list comprehension")
    result = [y for x in data for y in x]


def flatten_by_sum():
    print("sum")
    result = sum(data, [])


def flatten_by_for():
    print("for")
    result = []
    for d in data:
        result += d


def flatten_by_extend():
    print("extend")
    result = []
    for d in data:
        result.extend(d)


def flatten_by_reduce():
    print("reduce")
    result = reduce(lambda x, y: x + y, data)


methods = [flatten_by_chain,
           flatten_by_list_comprehension,
           flatten_by_sum,
           flatten_by_for,
           flatten_by_extend,
           flatten_by_reduce]

for method in methods:
    check_time(method)
