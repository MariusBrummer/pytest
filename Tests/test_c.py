from datetime import datetime
import pytest_check as check

from helper import make_route_request

def test_all_etas_of_deliveries_in_planning():
    data = make_route_request()
    deliver = data["planned_route"]["deliveries"]
    eta = []
    min_time = []
    max_time = []

    eta2 = []
    min_time2 = []
    max_time2 = []
    for d in deliver:
        if 'algorithm_fields' in d:
            if 'eta' in d['algorithm_fields'] and d['algorithm_fields']['type'] == 'delivery':
                eta.append(d['algorithm_fields']['eta'])
                min_time.append(d["min_time"])
                max_time.append(d["max_time"])

    for time in eta:
        t_obj = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.000000Z')
        eta2.append(t_obj)

    for time in min_time:
        t_obj = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.000000Z')
        min_time2.append(t_obj)

    for time in max_time:
        t_obj = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.000000Z')
        max_time2.append(t_obj)

    for i in range(len(eta2)):
        #assert (max_time2[i] > eta2[i] > min_time2[i])
        # assert (max_time2[i] > eta2[i])
        # assert (eta2[i] > min_time2[i])
        #assert 1 + 1 == 2
        check.greater(max_time2[i], eta2[i])
        check.greater(eta2[i], min_time2[i])


