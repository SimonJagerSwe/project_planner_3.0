# Imports
import sys

from PySide6 import QtWidgets
from  user_interface import UserInterface

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()

    # window.setWindowTitle("Project Planner 3.0 - Start Menu")

    '''window.ui.add_project_button.clicked.connect(UserInterface.add_project)
    window.ui.view_programming_button.clicked.connect(UserInterface.view_programming)
    window.ui.view_everyday_button.clicked.connect(UserInterface.view_everyday)
    window.ui.view_archived_button.clicked.connect(UserInterface.view_archive)
    window.ui.exit_button_main.clicked.connect(UserInterface.exit_program)'''
    window.show()
    app.exec()


if __name__ == "__main__":
    main()