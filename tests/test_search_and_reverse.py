import requests

from Extensions.response import Response
from Extensions.json_extension import JsonExtension
from schemas.open_street_map import OpenStreetMap
from enums.global_enums import GlobalErrorMessages
import configurator


class TestSearchAndReverse:

    def test_search(self, create_search_url, get_test_data_list_from_dict_search):
        response = requests.get(create_search_url(configurator.PATH_TO_TEST_DATA_SEARCH))

        Response(response).assert_status_code(200).validate(OpenStreetMap)

        test_data_values_list = get_test_data_list_from_dict_search(configurator.PATH_TO_TEST_DATA_SEARCH)

        response_data = str(Response(response).response_json[0]['display_name']).replace(",", "")

        for i in test_data_values_list:
            assert i in response_data, GlobalErrorMessages.DATA_DONT_MATCH

    def test_reverse(self, create_search_url, get_test_data_list_from_dict_search):
        response = requests.get(create_search_url(configurator.PATH_TO_TEST_DATA_REVERSE))

        Response(response).assert_status_code(200).validate(OpenStreetMap)

        test_data_values_list = get_test_data_list_from_dict_search(configurator.PATH_TO_TEST_DATA_REVERSE)

        result = JsonExtension(Response(response).response_json).crate_list_with_dict_values()

        for i in test_data_values_list:
            assert i in result, GlobalErrorMessages.DATA_DONT_MATCH
