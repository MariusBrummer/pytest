from helper import *
import pytest_check as check

def test_planned_state_from_deliveries_in_planned_route():
    planned_data = make_planning_request()
    planned_ids = []
    for item in planned_data:
        if item["current_state"] == "planned":
            planned_ids.append(item['id'])

    rdata = make_route_request()
    route_ids = []
    for item in rdata["planned_route"]["deliveries"]:
        route_ids.append(item["id"])

    for i in range(len(planned_ids)):
        #assert planned_ids[i] in route_ids
        check.is_in(planned_ids[i], route_ids)


