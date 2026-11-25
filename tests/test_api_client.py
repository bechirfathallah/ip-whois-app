import unittest
from unittest.mock import patch, Mock

from src.api_client import IPApiClient, ApiError

class TestIPApiClient(unittest.TestCase):

    def setUp(self):
        self.client = IPApiClient()

    @patch("src.api_client.requests.get")
    def test_get_my_ip_ipv4(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"ip": "8.8.8.8"}
        mock_get.return_value = mock_response

        result = self.client.get_my_ip(4)

        self.assertEqual(result, "8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_my_ip_ipv6(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"ip": "2001:4860:4860::8888"}
        mock_get.return_value = mock_response

        result = self.client.get_my_ip(6)

        self.assertEqual(result, "2001:4860:4860::8888")

    @patch("src.api_client.requests.get")
    def test_get_my_ips(self, mock_get):
        response_ipv4 = Mock()
        response_ipv4.json.return_value = {"ip": "8.8.8.8"}

        response_ipv6 = Mock()
        response_ipv6.json.return_value = {"ip": "2001:4860:4860::8888"}

        mock_get.side_effect = [response_ipv4, response_ipv6]

        result = self.client.get_my_ips()

        self.assertEqual(result["ipv4"], "8.8.8.8")
        self.assertEqual(result["ipv6"], "2001:4860:4860::8888")

    @patch("src.api_client.requests.get")
    def test_lookup_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "ip": "8.8.8.8",
            "country": "United States"
        }
        mock_get.return_value = mock_response

        result = self.client.lookup("8.8.8.8")

        self.assertTrue(result["success"])
        self.assertEqual(result["ip"], "8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_lookup_failure(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": False,
            "message": "Invalid IP address"
        }
        mock_get.return_value = mock_response

        with self.assertRaises(ApiError):
            self.client.lookup("invalid-ip")


if __name__ == "__main__":
    unittest.main()
