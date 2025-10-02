# Imports
import sys
import user_interface

from PySide6 import QtWidgets

from ui_add_everyday_project import Ui_add_everyday_project
from ui_add_new_project import Ui_add_new_project
from ui_add_programming_project import Ui_add_programming
from ui_archive_viewer import Ui_archive_viewer
from ui_everyday_viewer import Ui_everyday_viewer
from ui_programming_viewer import Ui_programming_viewer
# from user_interface import UserInterface


def open_add_project():
    print("Triggering add new project...")
    # app = QtWidgets.QApplication(sys.argv)
    # window = UserInterface()
    # window.show()
    # app.exec()
    # add_project = Ui_add_new_project()
    # self.ui = loader.load("add_new_project.ui")


def add_programming():
    ...

def edit_programming():
    ...

def view_programming():
    print("Triggering programming projects viewer...")

def add_everyday():
    ...

def edit_everyday():
    ...

def view_everyday():
    print("Triggering everyday projects viewer...")

def open_archives():
    print("Triggering archive viewer...")

def view_programming_archive():
    ...

def view_everyday_archive():
    ...

def view_full_archive():
    ...

def exit_program():
    print("Terminating program...")
    sys.exit()
    