import pytest
import requests
from openbrewer import OpenBrewer


@pytest.mark.parametrize(
    "add_url, code",
    [
        ("/v1/breweries", 200),
        ("/v1/breweries/meta", 200),
        ("/v1/breweries/autocomplete", 200),
    ],
    ids=["breweries", "all breweries meta data", "empty list for empty search"]
)
def test_code_openbrewer(url_openbrewer, add_url,  code):
    response = OpenBrewer(url_openbrewer).get_response(add_url)
    assert response.status_code == code


@pytest.mark.parametrize(
    "query_, lang_of_list_in_city",
    [
        ("San diego", 15),
        ("Jangsu-gun", 1)
    ],
    ids=["San Diego", "Jangsu-gun"]
)
def test_search_breweries_autocomplete_positive(url_search_breweries, query_, lang_of_list_in_city, code=200):
    response = OpenBrewer(url_search_breweries).searching(query_)
    assert response.status_code == code
    assert (len(response.json())) == lang_of_list_in_city


@pytest.mark.parametrize("add_url, code, param", [("/v1/breweries", 200, {"brewery_type": "closed"})])
def test_get_adress1_openbrewer(url_openbrewer, add_url,  code, param):
    response = OpenBrewer(url_openbrewer).get_response_param(add_url, param)
    assert response.status_code == code
    assert response.json()[1]["address_1"] == '407 Radam Ln Ste F200'


@pytest.mark.parametrize(
    "dict_of_all_breweries",
    [
        {'total': '8323', 'page': '1', 'per_page': '50'}
    ],
    ids=["all breweries meta data"]
)
def test_show_all_breweries_meta_data_positive(url_openbrewer_meta, dict_of_all_breweries, code=200):
    response = requests.get(url_openbrewer_meta)
    assert response.status_code == code
    assert response.json() == dict_of_all_breweries


@pytest.mark.parametrize(
    "dict_of_all_breweries",
    [
        1,
        {'modal': '8', 'page': '1', 'per_page': '50'}
    ],
    ids=["type of data is wrong", "data total and total value is wrong"]
)
def test_show_all_breweries_meta_data_negative(url_openbrewer_meta, dict_of_all_breweries):
    response = requests.get(url_openbrewer_meta)
    with pytest.raises(AssertionError):
        assert response.json() == dict_of_all_breweries, f'per_page should be {response.json()["per_page"]}'



