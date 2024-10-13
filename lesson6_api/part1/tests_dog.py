import pytest
from lesson6_api.part1.conftest import message_in_dog_list
import requests

@pytest.mark.parametrize(
    "code",
    [
        200
    ],
    ids=["code success"]
)
def test_dog_code200_positive(url_dog, dog_list_url, code):
    assert requests.get(url_dog).status_code == code
    assert requests.get(dog_list_url).status_code == code


def test_dog_massage_text_positive(url_dog):
    assert 'message' in requests.get(url_dog).text


def test_list_dogs_positive(dog_list_url):
    assert message_in_dog_list == requests.get(dog_list_url).json().get("message")


def test_dog_message_negative(dog_list_url):
    with pytest.raises(AssertionError):
        assert requests.get(dog_list_url).json().get("message") == ["basset", "blood", "english", "ibizan", "plott",
                                                                    "walker"]


@pytest.mark.parametrize(
    "code",
    [
        404
    ],
    ids=["wrong url"]
)
def test_dog_code_negative(random_url_wrong1, dog_list_url_wrong1, dog_list_url, code):
    assert requests.get(random_url_wrong1).status_code == code
    assert requests.get(dog_list_url_wrong1).status_code == code

