# tests/test_lib.py
from mlproject.distance import haversine

def test_type_of_haversine():
    assert type(haversine(1,2,3,4)) == float
