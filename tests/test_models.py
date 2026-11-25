import unittest

from src.models import IPInfo


class TestIPInfo(unittest.TestCase):

    def setUp(self):
        self.data = {
            "success": True,
            "ip": "8.8.8.8",
            "type": "IPv4",
            "continent": "North America",
            "country": "United States",
            "region": "California",
            "city": "Mountain View",
            "latitude": 37.386,
            "longitude": -122.0838,
            "isp": "Google LLC"
        }

    def test_from_json(self):
        info = IPInfo.from_json(self.data)

        self.assertEqual(info.ip, "8.8.8.8")
        self.assertEqual(info.country, "United States")
        self.assertEqual(info.city, "Mountain View")

    def test_to_dict(self):
        info = IPInfo.from_json(self.data)

        result = info.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["ip"], "8.8.8.8")

    def test_string_representation(self):
        info = IPInfo.from_json(self.data)

        result = str(info)

        self.assertIsInstance(result, str)
        self.assertIn("8.8.8.8", result)


if __name__ == "__main__":
    unittest.main()
