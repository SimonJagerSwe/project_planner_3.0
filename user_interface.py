# Imports
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

# from actions import open_add_project
import actions
from ui_project_planner_3 import Ui_project_planner_main
from ui_add_new_project import Ui_add_new_project


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


'''
    def view_programming(self):
        print("Triggering programming projects viewer...")

    def view_everyday(self):
        print("Triggering everyday projects viewer...")

    def view_archive(self):
        print("Triggering archive viewer...")

    def exit_program(self):
        print("Terminating program...")
        sys.exit()
        

    def open_add_project(self):
        print("Triggering add new project...")
        # app = QtWidgets.QApplication(sys.argv)
        window = UserInterface()
        window.show()
        # app.exec()
        # add_project = Ui_add_new_project()
        # self.ui = loader.load("add_new_project.ui")'''

