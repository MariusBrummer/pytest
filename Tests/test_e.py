from helper import make_route_request
import pytest_check as check

def test_less_or_equal_to_any_two_consecutive_deliveries():
    data = make_route_request()
    deliver = data["planned_route"]["deliveries"]

    algorithm_fields = []

    for d in deliver:
        if 'algorithm_fields' in d:
            if 'time_to_next' in d['algorithm_fields']:
                algorithm_fields.append(d['algorithm_fields'])

    delivery_time_to_next = []
    for i in algorithm_fields:
        if "delivery" in i.values():
            delivery_time_to_next.append(i)

    time_to_next = [x['time_to_next'] for x in delivery_time_to_next]
    num = len(time_to_next) - 2

    for i in range(len(time_to_next)):
        if i == num:
            break
        #assert time_to_next[i] < (time_to_next[i + 2] - time_to_next[i + 1])
        check.less(time_to_next[i], time_to_next[i+2] - time_to_next[i+1])
        print()
        print(f"{time_to_next[i]} should be smaller than {time_to_next[i+2] - time_to_next[i+1]}")


