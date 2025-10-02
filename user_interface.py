# Imports
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

import actions


loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("project_planner_3.0.ui", None)
        self.ui.setWindowTitle("Project Planner 3.0 - Main menu")
        self.ui.add_project_button.clicked.connect(actions.open_add_project)
        self.ui.view_programming_button.clicked.connect(actions.view_programming)
        self.ui.view_everyday_button.clicked.connect(actions.view_everyday)
        self.ui.view_archived_button.clicked.connect(actions.open_archives)
        self.ui.exit_button_main.clicked.connect(actions.exit_program)

    def show(self):
        self.ui.show()

