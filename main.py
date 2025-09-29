# Imports
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("project_planner_3.0.ui")

def add_project():
    print("Triggering add new project...")

def view_programming():
    print("Triggering programming projects viewer...")

def view_everyday():
    print("Triggering everyday projects viewer...")

def view_archive():
    print("Triggering archive viewer...")

def exit_program():
    print("Terminating program...")
    sys.exit()

window.setWindowTitle("Project Planner 3.0 - Start Menu")

window.add_project_button.clicked.connect(add_project)
window.view_programming_button.clicked.connect(view_programming)
window.view_everyday_button.clicked.connect(view_everyday)
window.view_archived_button.clicked.connect(view_archive)
window.exit_button_main.clicked.connect(exit_program)
window.show()
app.exec()


