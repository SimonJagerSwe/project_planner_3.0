# Imports
import sys

from PySide6 import QtWidgets
from  user_interface import UserInterface

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()