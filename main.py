from controllers.main_controller import MainController
from models.program_state import ProgramState

if __name__ == "__main__":
    """Initiates the program,
    loads every data"""

    program_state = ProgramState()
    program_state.load_initial_data()
    main_controller = MainController()
    main_controller.menu_controller(program_state)
