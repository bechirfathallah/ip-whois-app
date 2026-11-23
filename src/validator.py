
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
        return IPValidator._parse(ip) is not None

    @staticmethod
    def get_version(ip):
        parsed = IPValidator._parse(ip)
        return parsed.version if parsed else None

    @staticmethod
    def is_private(ip):
        parsed = IPValidator._parse(ip)
        return parsed.is_private if parsed else None
