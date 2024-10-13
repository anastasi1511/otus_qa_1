import pytest
import requests
from jsonplaceholder import Jsonplaceholder


@pytest.mark.parametrize('data_', [{
    'title': 'Привет',
    'body': 'kuku',
    'userId': 1
},
    {
        'title': 'Пока',
        'body': 'bue',
        'userId': 1
    }
])
def test_jsonplaceholder_code_positive(url_jsonplaceholder, data_, code=201):
    request = Jsonplaceholder(url_jsonplaceholder).post_data(data=data_)
    assert request.status_code == code



def test_jsonplaceholder_getting_resource_positive(url_jsonplaceholder, add_url="/posts/1"):
    response = Jsonplaceholder(url_jsonplaceholder).get_response(add_url)
    assert response.json()["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


@pytest.mark.parametrize('add_url', ["/posts/1", "/posts/10", "/posts/50"])
def test_jsonplaceholder_delete_positive(url_jsonplaceholder, add_url):
    request = Jsonplaceholder(url_jsonplaceholder).delete_data(add_url)
    assert request.status_code

def test_jsonplaceholder_filter_resource_positive(url_jsonplaceholder):
    param = {"userId": 1}
    response = Jsonplaceholder(url_jsonplaceholder).filter_data(param)
    assert len(response.json()) == 10


@pytest.mark.parametrize('data_', ["eyfiuehiue", 2, "1"])
def test_jsonplaceholder_getting_resource_negative(url_jsonplaceholder, data_, add_url="/posts/10"):
    response = Jsonplaceholder(url_jsonplaceholder).get_response(add_url)
    with pytest.raises(AssertionError):
        assert response.json()["userId"] == data_





