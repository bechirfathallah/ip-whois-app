# IP Whois App

Application Python en programmation orientée objet qui affiche l'adresse IP
publique (IPv4 et IPv6) de la machine et permet de rechercher les informations
d'une adresse IP, à la manière de whois. Elle utilise des APIs REST publiques.


# Équipe

bechir fathallah : Scrum Leader, développeur backend (client API, application principale) 
omar cherni : Développeur données et interface (validation, modèle, affichage, export) 
yassine ben fatma :  Testeur, documentation (tests) 

# Fonctionnalités

- Afficher son adresse IP publique (IPv4 et IPv6 si disponible)
- Rechercher pays, région, ville, opérateur et fuseau horaire d'une IP
- Validation des adresses saisies (IPv4, IPv6, adresses privées refusées)
- Gestion des erreurs : pas de réseau, délai dépassé, réponse invalide

# APIs utilisées

- ipify : https://api.ipify.org (IP publique)
- ipwho.is : https://ipwho.is (informations sur une IP)
