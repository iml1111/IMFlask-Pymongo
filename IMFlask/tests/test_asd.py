import unittest
from unittest import mock
import requests
from requests.exceptions import HTTPError


def google_query(query):
    url = "https://www.google.com"
    params = {'q': query}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content


class TestRequestsGET(unittest.TestCase):
    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            raise_for_status=None):

        mock_resp = mock.Mock()

        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status

        mock_resp.status_code = status
        mock_resp.content = content

        return mock_resp

    @mock.patch('requests.get')
    def test_google_query(self, mock_get):
        print(mock_get)
        mock_resp = self._mock_response(content="qwer1234")
        mock_get.return_value = mock_resp

        result = google_query('qwer1234')
        self.assertEqual(result, 'qwer1234')
        self.assertTrue(mock_resp.raise_for_status.called)

    @mock.patch('requests.get')
    def test_failed_query(self, mock_get):
        mock_resp = self._mock_response(
            status=500, raise_for_status=HTTPError("google is down"))
        mock_get.return_value = mock_resp
        self.assertRaises(HTTPError, google_query, 'qwer1234')


if __name__ == '__main__':
    unittest.main()