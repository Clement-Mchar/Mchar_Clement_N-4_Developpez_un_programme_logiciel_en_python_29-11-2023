class PlayerView:

    @classmethod
    def display_player_creation(cls):
        while True:
            player_first_name = input("Entrez le prénom du joueur: ")
            player_last_name = input("Entrez le nom du joueur: ")
            player_birthdate = input(
                "Entrez la date de naissance du joueur: "
            )
            player_infos = [
                player_first_name,
                player_last_name,
                player_birthdate
            ]
            if not player_infos:
                print("Veuillez entrer des informations valides.")
            else:
                break
        return player_first_name, player_last_name, player_birthdate
