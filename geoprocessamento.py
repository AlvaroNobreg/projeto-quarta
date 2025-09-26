from geopy.distance import geodesic

def distance_km(p1, p2):
    return geodesic(p1, p2).km
