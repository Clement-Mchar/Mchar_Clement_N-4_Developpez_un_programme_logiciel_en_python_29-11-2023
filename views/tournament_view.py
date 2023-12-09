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
    def display_players_registration(cls, existing_players):

        print(existing_players)

        player_id = int(input("Entrez l'id du joueur à inscrire au tournoi: "))

        return player_id
