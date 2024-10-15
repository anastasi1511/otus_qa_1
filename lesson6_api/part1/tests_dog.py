import pytest
from lesson6_api.part1.conftest import message_in_dog_list
import requests
from dogceo import DogCeo


@pytest.mark.parametrize(
    "add_url, code",
    [
        ("/breeds/image/random", 200),
        ("/breed/hound/list", 200)
    ],
    ids=["random dog url", "list of dogs url"]
)
def test_dog_code200_positive(url_dog, add_url, code):
    response = DogCeo(url_dog).get_response(add_url)
    assert response.status_code == code


@pytest.mark.parametrize("add_url, code", [("/breeds/image/random", 200),])
def test_dog_massage_text_positive(url_dog, add_url, code):
    response = DogCeo(url_dog).get_response(add_url)
    assert response.status_code == code
    assert 'message' in response.text


def test_list_dogs_positive(dog_list_url, code=200):
    assert requests.get(dog_list_url).status_code == code
    assert set(message_in_dog_list) == set(requests.get(dog_list_url).json().get("message"))
    assert len(message_in_dog_list) == len(requests.get(dog_list_url).json().get("message"))


def test_dog_message_negative(dog_list_url):
    with pytest.raises(AssertionError):
        assert requests.get(dog_list_url).json().get("message") == ["basset", "blood", "english", "ibizan", "plott",
                                                                    "walker"]


@pytest.mark.parametrize(
    "url, add_url, code",
    [
        ("https://dog.ceo/api", "/breeds/image/rando", 404),
        ("https://dog.ceo/api", "/breed/list", 404)
    ],
    ids=["wrong random dog url", "wrong list of dogs url"]
)
def test_dog_code_negative(url, add_url, code):
    response = DogCeo(url).get_response(add_url)
    assert response.status_code == code


