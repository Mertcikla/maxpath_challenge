from fastapi.testclient import TestClient
import json

from main import app

client = TestClient(app)


def test_get_max_path_sum_case_one():
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "2", "right": "3", "value": 1}, '
        '{"id": "3", "left": "6", "right": "7", "value": 3}, '
        '{"id": "7", "left": null, "right": null, "value": 7}, '
        '{"id": "6", "left": null, "right": null, "value": 6}, '
        '{"id": "2", "left": "4", "right": "5", "value": 2}, '
        '{"id": "5", "left": null, "right": null, "value": 5}, '
        '{"id": "4", "left": null, "right": null, "value": 4} ], '
        '"root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 200
    assert response.json() == {"max_path_sum": 18}


def test_get_max_path_sum_case_two():
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "2", "right": "3", "value": 1}, '
        '{"id": "3", "left": null, "right": null, "value": 3}, '
        '{"id": "2", "left": null, "right": null, "value": 2} ], '
        '"root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 200
    assert response.json() == {"max_path_sum": 6}


def test_get_max_path_sum_case_three():
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "-10", "right": "-5", "value": 1}, '
        '{"id": "-5", "left": "-20", "right": "-21", "value": -5}, '
        '{"id": "-21", "left": "100-2", "right": "1-3", "value": -21}, '
        '{"id": "1-3", "left": null, "right": null, "value": 1}, '
        '{"id": "100-2", "left": null, "right": null, "value": 100}, '
        '{"id": "-20", "left": "100", "right": "2", "value": -20}, '
        '{"id": "2", "left": null, "right": null, "value": 2}, '
        '{"id": "100", "left": null, "right": null, "value": 100}, '
        '{"id": "-10", "left": "30", "right": "45", "value": -10}, '
        '{"id": "45", "left": "3", "right": "-3", "value": 45}, '
        '{"id": "-3", "left": null, "right": null, "value": -3}, '
        '{"id": "3", "left": null, "right": null, "value": 3}, '
        '{"id": "30", "left": "5", "right": "1-2", "value": 30}, '
        '{"id": "1-2", "left": null, "right": null, "value": 1}, '
        '{"id": "5", "left": null, "right": null, "value": 5} ], '
        '"root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 200
    assert response.json() == {"max_path_sum": 154}


def test_get_max_path_invalid_input_no_nodes():
    json_test_data = json.loads(
        '{ "tree": '
        '{  "root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 422


def test_get_max_path_invalid_input_no_value():
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "2", "right": "3"}, '
        '{"id": "3", "left": null, "right": null, "value": 3}, '
        '{"id": "2", "left": null, "right": null, "value": 2} ], '
        '"root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 422


def test_get_max_path_invalid_input_no_root():
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "2", "right": "3"}, '
        '{"id": "3", "left": null, "right": null, "value": 3}, '
        '{"id": "2", "left": null, "right": null, "value": 2} ] } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 422


def test_get_max_path_invalid_input_no_json():
    response = client.post("/max-path-sum/")
    assert response.status_code == 422


def test_get_max_path_sum_case_three_without_nulls():
    """
    asserts that left,right null values are Optional and can be excluded from input if null
    """
    json_test_data = json.loads(
        '{ "tree": '
        '{ "nodes": [{"id": "1", "left": "-10", "right": "-5", "value": 1}, '
        '{"id": "-5", "left": "-20", "right": "-21", "value": -5}, '
        '{"id": "-21", "left": "100-2", "right": "1-3", "value": -21}, '
        '{"id": "1-3",  "value": 1}, '
        '{"id": "100-2",   "value": 100}, '
        '{"id": "-20", "left": "100", "right": "2", "value": -20}, '
        '{"id": "2",   "value": 2}, '
        '{"id": "100",   "value": 100}, '
        '{"id": "-10", "left": "30", "right": "45", "value": -10}, '
        '{"id": "45", "left": "3", "right": "-3", "value": 45}, '
        '{"id": "-3",   "value": -3}, '
        '{"id": "3",   "value": 3}, '
        '{"id": "30", "left": "5", "right": "1-2", "value": 30}, '
        '{"id": "1-2",   "value": 1}, '
        '{"id": "5",   "value": 5} ], '
        '"root": "1" } }')
    response = client.post("/max-path-sum/", json=json_test_data)
    assert response.status_code == 200
    assert response.json() == {"max_path_sum": 154}
