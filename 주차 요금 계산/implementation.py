from collections import defaultdict
from math import ceil


def solution(fees, records):
    total_time = defaultdict(int)
    parking = {}

    for record in records:
        time, car, content = record.split()

        if content == "IN":
            parking[car] = time
        else:
            park_time = parking[car]
            total_time[car] += duration(park_time, time)
            del parking[car]

    for car in parking:
        total_time[car] += duration(parking[car], "23:59")

    return list(map(lambda x: calculate_fee(fees, x), map(lambda x: total_time[x], sorted(total_time))))


def duration(start, end):
    return to_minute(end) - to_minute(start)


def to_minute(time):
    hour, second = time.split(":")
    return int(hour) * 60 + int(second)


def calculate_fee(fees, minute):
    default_time, default_fee, unit_time, unit_fee = map(int, fees)

    if minute <= default_time:
        return default_fee
    return default_fee + unit_fee * ceil((minute - default_time) / unit_time)
