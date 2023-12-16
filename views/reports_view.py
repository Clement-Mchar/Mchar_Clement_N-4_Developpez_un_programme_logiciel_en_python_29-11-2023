from rich.console import Console


class ReportsView:
    """Display the main menu"""

    console = Console()

    @classmethod
    def display_reports_menu(cls):
        cls.console.print("Veuillez sélectionner le rapport à afficher :")
        cls.console.print("1 : Afficher la liste des joueurs enregistrés")
        cls.console.print("2 : Afficher la liste de tous les tournois")
        cls.console.print("3: Afficher les noms et dates d'un tournoi")

        try:
            choice = input()
            return int(choice)
        except ValueError:
            print("Erreur: veuillez faire un choix valide")
            return cls.display_reports_menu()
