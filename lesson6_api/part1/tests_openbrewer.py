import pytest
import requests


@pytest.mark.parametrize("code", [200], ids=["code success"])
def test_code_openbrewer(url_openbrewer, url_openbrewer_meta, code):
    response1 = requests.get(url_openbrewer)
    response2 = requests.get(url_openbrewer_meta)
    assert response1.status_code == code
    assert response2.status_code == code


def test_get_adress1_openbrewer(url_openbrewer):
    param = {"brewery_type": "closed"}
    response = requests.get(url_openbrewer, params=param)
    assert response.json()[1]["address_1"] == '407 Radam Ln Ste F200'


@pytest.mark.parametrize(
    "dict_",
    [
        {'total': '8323', 'page': '1', 'per_page': '50'}
    ],
    ids=["data is true"]
)
def test_show_all_breweries_meta_data_positive(url_openbrewer_meta, dict_):
    response = requests.get(url_openbrewer_meta)
    assert response.json() == dict_


@pytest.mark.parametrize(
    "dict_",
    [
        1,
        {'modal': '8', 'page': '1', 'per_page': '50'}
    ],
    ids=["type of data true", "data is true"]
)
def test_show_all_breweries_meta_data_negative(url_openbrewer_meta, dict_):
    response = requests.get(url_openbrewer_meta)
    with pytest.raises(AssertionError):
        assert response.json() == dict_, f'per_page should be {response.json()["per_page"]}'


@pytest.mark.parametrize(
    "param",
    [
        "san%20diego",
        "Jangsu-gun"
    ],
    ids=["San Diego", "Jangsu-gun"]
)
def test_search_breweries_positive(url_search_breweries, param, code=200):
    response = requests.get(url_search_breweries, params=param)
    assert response.status_code == code
