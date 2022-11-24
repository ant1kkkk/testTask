import pytest
import json
from Extensions.json_extension import JsonExtension
from configurator import REQUEST_URL


def _generate_full_url(path_to_file):
    with open(path_to_file, "r", encoding='UTF-8') as file:
        data = json.load(file)

    if data["search_type"] == "search":
        url = f"{REQUEST_URL}search?"
        del data["search_type"]
    elif data["search_type"] == "reverse":
        url = f"{REQUEST_URL}reverse?"
        del data["search_type"]

    for item in data:
        url = url + f"&{item}={data[item]}"
    return url


def _get_test_data_list_from_dict_search(path_to_file):
    test_data_values_list = JsonExtension(path_to_file).create_list_with_dict_search_values()
    return test_data_values_list


@pytest.fixture(scope="function")
def create_search_url():
    return _generate_full_url


@pytest.fixture(scope="function")
def get_test_data_list_from_dict_search():
    return _get_test_data_list_from_dict_search
