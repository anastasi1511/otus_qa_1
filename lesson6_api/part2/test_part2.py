import requests


def test_request(url, status_code):
    assert status_code == requests.get(url).status_code
