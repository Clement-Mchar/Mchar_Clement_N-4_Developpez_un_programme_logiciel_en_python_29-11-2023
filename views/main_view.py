from rich.console import Console

class MenuView:
    """Display the main menu"""
    
    console = Console()

    @classmethod
    def display_main_menu(cls):
        cls.console.print("Veuillez sélectionner une option :")
        cls.console.print("1 : Créer un joueur")
        cls.console.print("2 : Créer un tournoi")
        try:
            choice = input()
            return int(choice)
        except ValueError as e:
            print(f"Erreur: veuillez faire un choix valide")
            return cls.display_main_menu()