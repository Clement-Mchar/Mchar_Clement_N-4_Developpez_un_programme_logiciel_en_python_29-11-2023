from views.main_view import MenuView

class MainController:

    @staticmethod
    def menu_controller():

        from controllers.player_controller import PlayerController

        while True:
            try:
                choice = MenuView.display_main_menu()
                if choice == 1:
                    PlayerController.create_player()
                else :
                    MenuView.display_main_menu()
            except ValueError as e :
                print(f"Erreur {e}")

        
