travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, cities):
    travel = {}
    travel["country"] = country
    travel["visits"] = visits
    travel["cities"] = cities
    travel_log.append(travel)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)