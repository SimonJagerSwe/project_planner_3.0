# Imports
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class NewProjectMenu(QtCore.QObject):
    def __init__(self):
        super().__init__
        self.ui = loader.load("add_new_project.ui")
        self.ui.setWindowTitle("Project Planner 3.0 - Add new project")
        # self.ui.add_programming_button.clicked.connect()

    def show(self):
        self.ui.show()