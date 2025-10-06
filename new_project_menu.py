# Imports
import actions

from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class NewProjectMenu(QtCore.QObject):
    def __init__(self):
        super().__init__
        self.ui = loader.load("add_new_project.ui", None)
        self.ui.setWindowTitle("Project Planner 3.0 - Add new project")
        self.ui.add_programming_button.clicked.connect(actions.add_programming)
        self.ui.add_everyday_button.clicked.connect(actions.add_everyday)
        self.ui.return_button.clicked.connect(actions.open_main_menu)
        self.ui.exit_button_projects.clicked.connect(actions.exit_program)

    def show(self):
        self.ui.show()