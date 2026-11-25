
from src.api_client import IPApiClient, ApiError
from src.models import IPInfo
from src.validator import IPValidator
from src.display import ConsoleDisplay


class IPWhoisApp:

    def __init__(self):
        self.client = IPApiClient()
        self.display = ConsoleDisplay()

    def show_my_ips(self):
        try:
            ips = self.client.get_my_ips()

            self.display.show_my_ips(
                ips.get("ipv4"),
                ips.get("ipv6")
            )

        except ApiError as error:
            self.display.show_error(str(error))

    def search_ip(self):
        ip = self.display.ask("Entrez une adresse IP : ").strip()

        if not IPValidator.is_valid(ip):
            self.display.show_error("Adresse IP invalide.")
            return

        try:
            data = self.client.lookup(ip)
            info = IPInfo.from_json(data)

            self.display.show_info(info)

        except ApiError as error:
            self.display.show_error(str(error))

    def run(self):
        while True:
            self.display.show_menu()

            choice = self.display.ask("Votre choix : ").strip()

            if choice == "1":
                self.show_my_ips()

            elif choice == "2":
                self.search_ip()

            elif choice == "3":
                print("\nMerci d'avoir utilisé notre application !")
                break

            else:
                self.display.show_error(
                    "Choix invalide. Veuillez choisir entre 1 et 3."
                )


def main():
    app = IPWhoisApp()
    app.run()


if __name__ == "__main__":
    main()
