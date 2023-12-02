from views.main_view import MenuView


class MainController:
    """Handles the menu
    Triggers all the other controllers"""

    @staticmethod
    def menu_controller():

        from controllers.player_controller import PlayerController
        from controllers.tournament_controller import TournamentController

        while True:
            try:
                choice = MenuView.display_main_menu()
                if choice == 1:
                    PlayerController.create_player()
                elif choice == 2:
                    TournamentController.create_tournament()
                else:
                    print("Erreur : veuillez faire un choix valide.")
                    MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur {e}")
