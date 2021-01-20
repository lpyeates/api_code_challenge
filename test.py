import pytest
import mock
from main import get_data


class testClass:

    # I had trouble getting the tests set up correctly
    # I've never built a python anything to consume from another API so this was new for me
    # I built it close to how I wanted it but I am ran out of time and valued hitting your deadline
    @patch.object('main.requests.get')
    def test_500(self):
        mock_get = mock.MagicMock()
        type(mock_get).status_code = mock.PropertyMock(return_value=500)
        mock_get.json.return_value = "{'err':'err'}"
        result = get_data()
        assert result == "{'err':'err'}"

    # For the second test I remebered from mocking DB responses that I would need to mock it twice
    # once to give it the 429 response and once with a 200 response so it would not remain stuck in
    # an infinite loop
    @patch('main.request.get')
    @patch('main.request.get')
    def test_429(self):
        mock_get = mock.MagicMock()
        type(mock_get).status_code = mock.PropertyMock(return_value=429)
        mock_get.json.return_value = "{'err':'err'}"
        mock_get = mock.MagicMock()
        type(mock_get).status_code = mock.PropertyMock(return_value=200)
        mock_get.json.return_value = "{'data':'rows'}"
        result = get_data()
        assert result == "{'data':'rows'}"
