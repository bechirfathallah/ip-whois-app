
class ConsoleDisplay:
    LINE = "=" * 46

    def show_menu(self):
        print()
        print(self.LINE)
        print("        WHOIS IP - Application Python")
        print(self.LINE)
        print("  1. Afficher mon adresse IP publique")
        print("  2. Rechercher les infos d'une adresse IP")
        print("  3. Quitter")
        print(self.LINE)

    def ask(self, prompt):
        return input(prompt)

    def show_my_ips(self, ipv4, ipv6):
        print()
        print("--- Votre adresse IP publique ---")
        print(f"IPv4 : {ipv4 if ipv4 else 'non disponible'}")
        print(f"IPv6 : {ipv6 if ipv6 else 'non disponible'}")

    def show_info(self, info):
        print()
        print(f"--- Informations sur {info.ip} ---")
        print(f"Version   : {info.version}")
        print(f"Pays      : {info.country}")
        print(f"Région    : {info.region}")
        print(f"Ville     : {info.city}")
        print(f"Opérateur : {info.isp}")
        print(f"Fuseau    : {info.timezone}")
        if info.latitude is not None and info.longitude is not None:
            print(f"Position  : {info.latitude}, {info.longitude}")

    def show_error(self, message):
        print(f"\n[Erreur] {message}")