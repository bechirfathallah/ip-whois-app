"""Communication avec les APIs REST publiques (ipify et ipwho.is)."""
import requests


class ApiError(Exception):
    """Erreur de communication avec une API (réseau, délai, réponse invalide)."""


class IPApiClient:
    """Client des APIs REST : IP publique de la machine et recherche d'une IP."""

    # Constantes de classe : les adresses des APIs, modifiables à un seul endroit.
    IPV4_URL = "https://api.ipify.org?format=json"
    IPV6_URL = "https://api6.ipify.org?format=json"
    LOOKUP_URL = "https://ipwho.is/{ip}"

    def __init__(self, timeout=5):
        # Privé : le délai maximum d'attente d'une réponse, en secondes.
        self.__timeout = timeout

    def __get_json(self, url):
        """Envoie une requête GET et renvoie la réponse JSON (dict).

        Toutes les erreurs possibles sont converties en ApiError : le reste
        du programme n'a qu'un seul type d'erreur à gérer.
        """
        try:
            response = requests.get(url, timeout=self.__timeout)
            response.raise_for_status()  # lève une erreur si le code HTTP est 4xx ou 5xx
            return response.json()
        except requests.exceptions.Timeout:
            raise ApiError("Délai dépassé : le serveur ne répond pas.")
        except requests.exceptions.ConnectionError:
            raise ApiError("Pas de connexion à Internet (ou serveur injoignable).")
        except requests.exceptions.RequestException as error:
            raise ApiError(f"Erreur de requête : {error}")
        except ValueError:
            raise ApiError("La réponse du serveur n'est pas du JSON valide.")

    def get_my_ip(self, version=4):
        """Renvoie l'adresse IP publique de cette machine (version 4 ou 6)."""
        url = self.IPV4_URL if version == 4 else self.IPV6_URL
        data = self.__get_json(url)
        ip = data.get("ip")
        if not ip:
            raise ApiError("Réponse inattendue : adresse IP absente.")
        return ip

    def get_my_ips(self):
        """Renvoie {"ipv4": ..., "ipv6": ...}.

        L'IPv4 est obligatoire (erreur si absente). L'IPv6 est optionnelle :
        beaucoup de connexions n'en ont pas, ce n'est pas une erreur.
        """
        ipv4 = self.get_my_ip(4)
        try:
            ipv6 = self.get_my_ip(6)
        except ApiError:
            ipv6 = None
        return {"ipv4": ipv4, "ipv6": ipv6}

    def lookup(self, ip):
        """Renvoie le JSON brut (dict) des informations d'une adresse IP."""
        data = self.__get_json(self.LOOKUP_URL.format(ip=ip))
        if not data.get("success", False):
            raise ApiError(data.get("message", "Adresse introuvable."))
        return data