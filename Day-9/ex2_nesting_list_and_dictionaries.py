# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France": {"citties_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"citties_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a List
travel_log = {
    {
        "country": "France",
        "citties_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "citties_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}