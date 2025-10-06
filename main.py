# Imports
import sys

from PySide6 import QtWidgets
from  main_menu import MainMenu

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainMenu()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()