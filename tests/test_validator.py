import unittest

from src.validator import IPValidator


class TestIPValidator(unittest.TestCase):

    def test_valid_ipv4(self):
        self.assertTrue(IPValidator.is_valid("8.8.8.8"))

    def test_valid_ipv6(self):
        self.assertTrue(
            IPValidator.is_valid("2001:4860:4860::8888")
        )

    def test_invalid_ip(self):
        self.assertFalse(IPValidator.is_valid("999.999.999.999"))

    def test_get_version_ipv4(self):
        self.assertEqual(
            IPValidator.get_version("8.8.8.8"),
            4
        )

    def test_get_version_ipv6(self):
        self.assertEqual(
            IPValidator.get_version("2001:4860:4860::8888"),
            6
        )

    def test_is_private(self):
        self.assertTrue(IPValidator.is_private("192.168.1.1"))
        self.assertFalse(IPValidator.is_private("8.8.8.8"))


if __name__ == "__main__":
    unittest.main()

