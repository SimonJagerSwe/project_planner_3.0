# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_programming_project.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_add_programming(object):
    def setupUi(self, add_programming):
        if not add_programming.objectName():
            add_programming.setObjectName(u"add_programming")
        add_programming.resize(423, 489)
        self.programming_add_project_button = QPushButton(add_programming)
        self.programming_add_project_button.setObjectName(u"programming_add_project_button")
        self.programming_add_project_button.setGeometry(QRect(20, 320, 381, 51))
        self.widget = QWidget(add_programming)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 380, 381, 81))
        self.programming_return_exit_layout = QHBoxLayout(self.widget)
        self.programming_return_exit_layout.setObjectName(u"programming_return_exit_layout")
        self.programming_return_exit_layout.setContentsMargins(0, 0, 0, 0)
        self.programming_return_button = QPushButton(self.widget)
        self.programming_return_button.setObjectName(u"programming_return_button")

        self.programming_return_exit_layout.addWidget(self.programming_return_button)

        self.programming_exit_button = QPushButton(self.widget)
        self.programming_exit_button.setObjectName(u"programming_exit_button")

        self.programming_return_exit_layout.addWidget(self.programming_exit_button)

        self.widget1 = QWidget(add_programming)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 22, 381, 281))
        self.programming_line_edits_layout = QVBoxLayout(self.widget1)
        self.programming_line_edits_layout.setObjectName(u"programming_line_edits_layout")
        self.programming_line_edits_layout.setContentsMargins(0, 0, 0, 0)
        self.programming_name_line_edit = QLineEdit(self.widget1)
        self.programming_name_line_edit.setObjectName(u"programming_name_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_name_line_edit)

        self.programming_start_line_edit = QLineEdit(self.widget1)
        self.programming_start_line_edit.setObjectName(u"programming_start_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_start_line_edit)

        self.programming_finish_line_edit = QLineEdit(self.widget1)
        self.programming_finish_line_edit.setObjectName(u"programming_finish_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_finish_line_edit)

        self.programming_language_line_edit = QLineEdit(self.widget1)
        self.programming_language_line_edit.setObjectName(u"programming_language_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_language_line_edit)

        self.programming_link_line_edit = QLineEdit(self.widget1)
        self.programming_link_line_edit.setObjectName(u"programming_link_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_link_line_edit)

        self.programming_notes_line_edit = QLineEdit(self.widget1)
        self.programming_notes_line_edit.setObjectName(u"programming_notes_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_notes_line_edit)

        self.programming_progress_line_edit = QLineEdit(self.widget1)
        self.programming_progress_line_edit.setObjectName(u"programming_progress_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_progress_line_edit)

        self.programming_status_line_edit = QLineEdit(self.widget1)
        self.programming_status_line_edit.setObjectName(u"programming_status_line_edit")

        self.programming_line_edits_layout.addWidget(self.programming_status_line_edit)


        self.retranslateUi(add_programming)

        QMetaObject.connectSlotsByName(add_programming)
    # setupUi

    def retranslateUi(self, add_programming):
        add_programming.setWindowTitle(QCoreApplication.translate("add_programming", u"Form", None))
        self.programming_add_project_button.setText(QCoreApplication.translate("add_programming", u"Add project", None))
        self.programming_return_button.setText(QCoreApplication.translate("add_programming", u"Return to main menu", None))
        self.programming_exit_button.setText(QCoreApplication.translate("add_programming", u"Exit program", None))
        self.programming_name_line_edit.setText(QCoreApplication.translate("add_programming", u"Project name", None))
        self.programming_start_line_edit.setText(QCoreApplication.translate("add_programming", u"Start date", None))
        self.programming_finish_line_edit.setText(QCoreApplication.translate("add_programming", u"Projected finish date", None))
        self.programming_language_line_edit.setText(QCoreApplication.translate("add_programming", u"Language(s)", None))
        self.programming_link_line_edit.setText(QCoreApplication.translate("add_programming", u"Project link", None))
        self.programming_notes_line_edit.setText(QCoreApplication.translate("add_programming", u"Project notes", None))
        self.programming_progress_line_edit.setText(QCoreApplication.translate("add_programming", u"Progress %", None))
        self.programming_status_line_edit.setText(QCoreApplication.translate("add_programming", u"Status", None))
    # retranslateUi

