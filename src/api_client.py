
import requests


class ApiError(Exception):
    pass


class IPApiClient:

    IPV4_URL = "https://api.ipify.org?format=json"
    IPV6_URL = "https://api6.ipify.org?format=json"
    LOOKUP_URL = "https://ipwho.is/{}"

    def __init__(self, timeout=5):
        self.__timeout = timeout

    def __get_json(self, url):
        try:
            response = requests.get(url, timeout=self.__timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise ApiError("Délai dépassé.")

        except requests.exceptions.ConnectionError:
            raise ApiError("Connexion Internet impossible.")

        except requests.exceptions.RequestException:
            raise ApiError("Erreur de communication avec l'API.")

        except ValueError:
            raise ApiError("Réponse JSON invalide.")

    def get_my_ip(self, version=4):
        if version not in (4, 6):
            raise ApiError("Version IP invalide.")

        url = self.IPV4_URL if version == 4 else self.IPV6_URL
        data = self.__get_json(url)

        if not data.get("ip"):
            raise ApiError("Adresse IP introuvable.")

        return data["ip"]

    def get_my_ips(self):
        ipv4 = self.get_my_ip(4)

        try:
            ipv6 = self.get_my_ip(6)
        except ApiError:
            ipv6 = None

        return {
            "ipv4": ipv4,
            "ipv6": ipv6
        }

    def lookup(self, ip):
        data = self.__get_json(self.LOOKUP_URL.format(ip))

        if not data.get("success"):
            raise ApiError(data.get("message", "Adresse introuvable."))

        return data
