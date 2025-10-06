# Imports
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

from main_menu import MainMenu
from new_project_menu import NewProjectMenu
# from ui_add_new_project import Ui_add_new_project

loader = QUiLoader()

def new_window(ui):
    print(ui)
    print(type(ui))
    # window = loader.load(ui)

def open_add_project():    
    print("Triggering add new project...")
    main = MainMenu()
    # main.
    app = QtWidgets.QApplication(sys.argv)
    window = NewProjectMenu()
    window.show()
    app.exec()



def add_programming():
    print("Triggering add new programming project...")
    ui = "ui_add_programming_project.py"

def edit_programming():
    print("Triggering edit programming project...")

def view_programming():
    print("Triggering programming projects viewer...")

def add_everyday():
    print("Triggering add everyday project...")

def edit_everyday():
    print("Triggering edit everyday project...")

def view_everyday():
    print("Triggering everyday projects viewer...")

def open_archives():
    print("Triggering archive viewer...")

def view_programming_archive():
    print("Triggering view programming archive...")

def view_everyday_archive():
    print("Triggering view everyday archive...")

def view_full_archive():
    print("Triggering view full archive...")

def exit_program():
    print("Terminating program...")
    sys.exit()
    