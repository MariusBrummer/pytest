import requests

def make_planning_request():
    response = requests.get("http://www.amock.io/api/mbrummer75@/planning")
    planning_data = response.json()
    return planning_data
    
def make_route_request():
    BaseURL = "http://www.amock.io/api/mbrummer75@/route"
    response = requests.get("http://www.amock.io/api/mbrummer75@/route")
    route_data = response.json()
    return route_data


