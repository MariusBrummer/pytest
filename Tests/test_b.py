from datetime import datetime
from helper import make_route_request


def test_sum_of_weights_less_than_carry_capacity():
    data = make_route_request()
    deliver = data["planned_route"]["deliveries"]
    weights = []
    for d in deliver:
        if 'algorithm_fields' in d:
            if 'weight' in d['algorithm_fields']:
                weights.append(d['algorithm_fields'])
    ld = [x['weight'] for x in weights]
    total_weight = (sum(ld))
    assert total_weight < data["planned_route"]["resource"]["carrying_capacity"]


