from views.main_view import MenuView


class MainController:
    """Handles the menu
    Triggers all the other controllers"""

    @staticmethod
    def menu_controller():
        from controllers.player_controller import PlayerController
        from controllers.tournament_controller import TournamentController
        from controllers.reports_controller import ReportController

        while True:
            try:
                choice = MenuView.display_main_menu()
                if choice == 1:
                    PlayerController.create_player()
                elif choice == 2:
                    TournamentController.create_tournament()
                elif choice == 3:
                    ReportController.reports_menu()
                else:
                    print("Erreur : veuillez faire un choix valide.")
                    MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur {e}")
