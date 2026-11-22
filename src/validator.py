
import ipaddress


class IPValidator:
    

    @staticmethod
    def _parse(ip):
        try:
            return ipaddress.ip_address(str(ip).strip())
        except ValueError:
            return None

    @staticmethod
    def is_valid(ip):
        """Renvoie True si ip est une adresse IPv4 ou IPv6 valide."""
        return IPValidator._parse(ip) is not None

    @staticmethod
    def get_version(ip):
        """Renvoie 4, 6, ou None si l'adresse est invalide."""
        parsed = IPValidator._parse(ip)
        return parsed.version if parsed else None

    @staticmethod
    def is_private(ip):
        parsed = IPValidator._parse(ip)
        return parsed.is_private if parsed else None