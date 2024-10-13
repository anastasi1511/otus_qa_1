import pytest

message_in_dog_list = ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]


#for dogceo


def pytest_addoption(parser):
    parser.addoption(
        "--url_dog",
        default='https://dog.ceo/api/breeds/image/random',
        help="This is dog url for random"
    )
    parser.addoption(
        "--random_url_wrong1",
        default="https://dog.ceo/api/breeds/image/rando",
        help="This is wrong dog url for random"
    )
    parser.addoption(
        "--dog_list_url",
        default="https://dog.ceo/api/breed/hound/list",
        help="This is dog list url"
    )
    parser.addoption(
        "--dog_list_url_wrong1",
        default="https://dog.ceo/api/breed/hound/lis",
        help="This is wrong dog list url"
    )
    parser.addoption(
        "--url_openbrewer",
        default="https://api.openbrewerydb.org/v1/breweries",
        help="This is dog url for www.openbrewerydb.org"
    )
    parser.addoption(
        "--url_openbrewer_meta",
        default="https://api.openbrewerydb.org/v1/breweries/meta",
        help="This is dog url for www.openbrewerydb.org for meta data"
    )
    parser.addoption(
        "--url_search_breweries",
        default="https://api.openbrewerydb.org/v1/breweries/autocomplete",
        help="This is dog url for www.openbrewerydb.org search breweries"
    )
    parser.addoption(
        "--url_jsonplaceholder",
        default="https://jsonplaceholder.typicode.com",
        help="This is dog url for for https://jsonplaceholder"
    )



@pytest.fixture
def url_dog(request):
    return request.config.getoption("--url_dog")


@pytest.fixture
def random_url_wrong1(request):
    return request.config.getoption("--random_url_wrong1")


@pytest.fixture
def dog_list_url(request):
    return request.config.getoption("--dog_list_url")


@pytest.fixture
def dog_list_url_wrong1(request):
    return request.config.getoption("--dog_list_url_wrong1")


#for https://www.openbrewerydb.org/

@pytest.fixture
def url_openbrewer(request):
    return request.config.getoption("--url_openbrewer")


@pytest.fixture
def url_openbrewer_meta(request):
    return request.config.getoption("--url_openbrewer_meta")


@pytest.fixture
def url_search_breweries(request):
    return request.config.getoption("--url_search_breweries")



#for https://jsonplaceholder


@pytest.fixture
def url_jsonplaceholder(request):
    return request.config.getoption("--url_jsonplaceholder")
