# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_project.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_add_new_project(object):
    def setupUi(self, add_new_project):
        if not add_new_project.objectName():
            add_new_project.setObjectName(u"add_new_project")
        add_new_project.resize(239, 371)
        self.widget = QWidget(add_new_project)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 170, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_programming_button = QPushButton(self.widget)
        self.add_programming_button.setObjectName(u"add_programming_button")
        self.add_programming_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.add_programming_button)

        self.add_everyday_button = QPushButton(self.widget)
        self.add_everyday_button.setObjectName(u"add_everyday_button")
        self.add_everyday_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.add_everyday_button)

        self.return_button = QPushButton(self.widget)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.return_button)

        self.exit_button_projects = QPushButton(self.widget)
        self.exit_button_projects.setObjectName(u"exit_button_projects")
        self.exit_button_projects.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.exit_button_projects)


        self.retranslateUi(add_new_project)

        QMetaObject.connectSlotsByName(add_new_project)
    # setupUi

    def retranslateUi(self, add_new_project):
        add_new_project.setWindowTitle(QCoreApplication.translate("add_new_project", u"Form", None))
        self.add_programming_button.setText(QCoreApplication.translate("add_new_project", u"Add programming project", None))
        self.add_everyday_button.setText(QCoreApplication.translate("add_new_project", u"Add everyday project", None))
        self.return_button.setText(QCoreApplication.translate("add_new_project", u"Return to main menu", None))
        self.exit_button_projects.setText(QCoreApplication.translate("add_new_project", u"Exit program", None))
    # retranslateUi

