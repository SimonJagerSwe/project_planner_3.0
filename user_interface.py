# Imports
import sys

from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("project_planner_3.0.ui", None)
        self.ui.setWindowTitle("Project Planner 3.0 - Main menu")
        self.ui.add_project_button.clicked.connect(self.add_project)
        self.ui.view_programming_button.clicked.connect(self.view_programming)
        self.ui.view_everyday_button.clicked.connect(self.view_everyday)
        self.ui.view_archived_button.clicked.connect(self.view_archive)
        self.ui.exit_button_main.clicked.connect(self.exit_program)

    def show(self):
        self.ui.show()

    def add_project(self):
        print("Triggering add new project...")

    def view_programming(self):
        print("Triggering programming projects viewer...")

    def view_everyday(self):
        print("Triggering everyday projects viewer...")

    def view_archive(self):
        print("Triggering archive viewer...")

    def exit_program(self):
        print("Terminating program...")
        sys.exit()
        