# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_everyday_project.ui'
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

class Ui_add_everyday_project(object):
    def setupUi(self, add_everyday_project):
        if not add_everyday_project.objectName():
            add_everyday_project.setObjectName(u"add_everyday_project")
        add_everyday_project.resize(425, 443)
        self.everyday_project_add_button = QPushButton(add_everyday_project)
        self.everyday_project_add_button.setObjectName(u"everyday_project_add_button")
        self.everyday_project_add_button.setGeometry(QRect(20, 270, 381, 51))
        self.layoutWidget = QWidget(add_everyday_project)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 330, 381, 81))
        self.everyday_return_exit_layout = QHBoxLayout(self.layoutWidget)
        self.everyday_return_exit_layout.setObjectName(u"everyday_return_exit_layout")
        self.everyday_return_exit_layout.setContentsMargins(0, 0, 0, 0)
        self.everyday_return_button = QPushButton(self.layoutWidget)
        self.everyday_return_button.setObjectName(u"everyday_return_button")

        self.everyday_return_exit_layout.addWidget(self.everyday_return_button)

        self.everyday_exit_button = QPushButton(self.layoutWidget)
        self.everyday_exit_button.setObjectName(u"everyday_exit_button")

        self.everyday_return_exit_layout.addWidget(self.everyday_exit_button)

        self.layoutWidget1 = QWidget(add_everyday_project)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 381, 251))
        self.everyday_line_edits = QVBoxLayout(self.layoutWidget1)
        self.everyday_line_edits.setObjectName(u"everyday_line_edits")
        self.everyday_line_edits.setContentsMargins(0, 0, 0, 0)
        self.everyday_name_line_edit = QLineEdit(self.layoutWidget1)
        self.everyday_name_line_edit.setObjectName(u"everyday_name_line_edit")

        self.everyday_line_edits.addWidget(self.everyday_name_line_edit)

        self.everyday_start_line_edit = QLineEdit(self.layoutWidget1)
        self.everyday_start_line_edit.setObjectName(u"everyday_start_line_edit")

        self.everyday_line_edits.addWidget(self.everyday_start_line_edit)

        self.everyday_finish_line_edit = QLineEdit(self.layoutWidget1)
        self.everyday_finish_line_edit.setObjectName(u"everyday_finish_line_edit")

        self.everyday_line_edits.addWidget(self.everyday_finish_line_edit)

        self.everyday_progress_line_edit_2 = QLineEdit(self.layoutWidget1)
        self.everyday_progress_line_edit_2.setObjectName(u"everyday_progress_line_edit_2")

        self.everyday_line_edits.addWidget(self.everyday_progress_line_edit_2)

        self.everyday_progress_line_edit = QLineEdit(self.layoutWidget1)
        self.everyday_progress_line_edit.setObjectName(u"everyday_progress_line_edit")

        self.everyday_line_edits.addWidget(self.everyday_progress_line_edit)

        self.everyday_status_line_edit = QLineEdit(self.layoutWidget1)
        self.everyday_status_line_edit.setObjectName(u"everyday_status_line_edit")

        self.everyday_line_edits.addWidget(self.everyday_status_line_edit)


        self.retranslateUi(add_everyday_project)

        QMetaObject.connectSlotsByName(add_everyday_project)
    # setupUi

    def retranslateUi(self, add_everyday_project):
        add_everyday_project.setWindowTitle(QCoreApplication.translate("add_everyday_project", u"Form", None))
        self.everyday_project_add_button.setText(QCoreApplication.translate("add_everyday_project", u"Add project", None))
        self.everyday_return_button.setText(QCoreApplication.translate("add_everyday_project", u"Return to main menu", None))
        self.everyday_exit_button.setText(QCoreApplication.translate("add_everyday_project", u"Exit program", None))
        self.everyday_name_line_edit.setText(QCoreApplication.translate("add_everyday_project", u"Project name", None))
        self.everyday_start_line_edit.setText(QCoreApplication.translate("add_everyday_project", u"Start date", None))
        self.everyday_finish_line_edit.setText(QCoreApplication.translate("add_everyday_project", u"Projected finish date", None))
        self.everyday_progress_line_edit_2.setText(QCoreApplication.translate("add_everyday_project", u"Project notes", None))
        self.everyday_progress_line_edit.setText(QCoreApplication.translate("add_everyday_project", u"Progress %", None))
        self.everyday_status_line_edit.setText(QCoreApplication.translate("add_everyday_project", u"Status", None))
    # retranslateUi

