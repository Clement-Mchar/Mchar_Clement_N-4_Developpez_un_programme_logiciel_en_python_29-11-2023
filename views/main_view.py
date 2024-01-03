from rich.console import Console


class MenuView:
    """Displays the main menu"""

    console = Console()

    @classmethod
    def display_main_menu(cls):
        cls.console.print("Veuillez sélectionner une option :")
        cls.console.print("1 : Créer un joueur")
        cls.console.print("2 : Créer un tournoi")
        cls.console.print("3 : Afficher les rapports")
        try:
            choice = input()
            return int(choice)
        except ValueError:
            print("Erreur: veuillez faire un choix valide")
            return cls.display_main_menu()
