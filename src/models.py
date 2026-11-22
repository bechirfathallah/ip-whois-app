class IPInfo:
   
    def __init__(self, ip, version, country, region, city, isp, timezone,
                 latitude=None, longitude=None):
        self.__ip = ip
        self.__version = version
        self.__country = country
        self.__region = region
        self.__city = city
        self.__isp = isp
        self.__timezone = timezone
        self.__latitude = latitude
        self.__longitude = longitude

    # Lecture seule : @property permet d'écrire info.ip au lieu de info.get_ip()
    @property
    def ip(self):
        return self.__ip

    @property
    def version(self):
        return self.__version

    @property
    def country(self):
        return self.__country

    @property
    def region(self):
        return self.__region

    @property
    def city(self):
        return self.__city

    @property
    def isp(self):
        return self.__isp

    @property
    def timezone(self):
        return self.__timezone

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @classmethod
    def from_json(cls, data):
 
        connection = data.get("connection") or {}
        timezone = data.get("timezone") or {}
        return cls(
            ip=data.get("ip") or "Inconnu",
            version=data.get("type") or "Inconnu",
            country=data.get("country") or "Inconnu",
            region=data.get("region") or "Inconnu",
            city=data.get("city") or "Inconnu",
            isp=connection.get("isp") or "Inconnu",
            timezone=timezone.get("id") or "Inconnu",
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
        )

    def to_dict(self):
        return {
            "ip": self.ip,
            "version": self.version,
            "country": self.country,
            "region": self.region,
            "city": self.city,
            "isp": self.isp,
            "timezone": self.timezone,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def __str__(self):
        return f"{self.ip} ({self.version}) - {self.city}, {self.country} - {self.isp}"