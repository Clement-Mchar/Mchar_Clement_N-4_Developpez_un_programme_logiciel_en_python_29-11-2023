class PlayerView:

    @classmethod
    def display_player_creation(cls):
        while True:
            player_first_name = input("Entrez le prénom du joueur :")
            player_last_name = input("Entrez le nom du joueur :")
            player_birthdate = input("Entrez la date de naissance du joueur :")

            if not player_first_name or not player_last_name or not player_birthdate :
                print("Veuillez entrer des informations valides pour le joueur.")
            else:
                break
        return player_first_name, player_last_name, player_birthdate
