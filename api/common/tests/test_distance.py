from common.utils.distance import calculate_distance_in_miles, build_matrix

def test_build_matrix():
    starting = "28.365801,-81.521347"
    target = "34.136970,-118.237620"
    expected = [[28.365801, 34.136970], [-81.521347, -118.237620]]
    output = build_matrix(starting, target)
    assert expected[0][0] == output[0][0]
    assert expected[0][1] == output[0][1]
    assert expected[1][0] == output[1][0]
    assert expected[0][1] == output[0][1]

def test_distance_calculates_correctly():
    starting = "28.365801,-81.521347"
    target = "34.136970,-118.237620"
    matrix = build_matrix(starting, target)
    expecting = 2193.07 # from https://gps-coordinates.org/distance-between-coordinates.php
    output = calculate_distance_in_miles(matrix)
    assert abs(float(expecting) - float(output)) < 1

