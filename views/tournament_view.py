class TournamentView:

    @classmethod
    def display_tournament_creation(cls):

        tournament_name = input("Nom du tournoi : ")
        tournament_place = input("Lieu du tournoi : ")
        tournament_players = input("Nombre de joueurs : ")
        tournament_rounds = input("Nombre de rounds : ")
        tournament_description = input("Description : ")

        return [
                tournament_name,
                tournament_place,
                int(tournament_players),
                int(tournament_rounds),
                tournament_description
                ]

    @classmethod
    def display_players_registration(cls):

        player_first_name = input("Entrez le prénom du joueur : ")
        player_last_name = input("Entrez le nom du joueur : ")

        return player_first_name, player_last_name
