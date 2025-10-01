# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_everyday_project.ui'
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

class Ui_edit_everyday_project(object):
    def setupUi(self, edit_everyday_project):
        if not edit_everyday_project.objectName():
            edit_everyday_project.setObjectName(u"edit_everyday_project")
        edit_everyday_project.resize(425, 443)
        self.everyday_project_edit_button = QPushButton(edit_everyday_project)
        self.everyday_project_edit_button.setObjectName(u"everyday_project_edit_button")
        self.everyday_project_edit_button.setGeometry(QRect(20, 270, 381, 51))
        self.layoutWidget = QWidget(edit_everyday_project)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 381, 251))
        self.edit_everyday_line_edits = QVBoxLayout(self.layoutWidget)
        self.edit_everyday_line_edits.setObjectName(u"edit_everyday_line_edits")
        self.edit_everyday_line_edits.setContentsMargins(0, 0, 0, 0)
        self.edit_everyday_name_line_edit = QLineEdit(self.layoutWidget)
        self.edit_everyday_name_line_edit.setObjectName(u"edit_everyday_name_line_edit")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_name_line_edit)

        self.edit_everyday_start_line_edit = QLineEdit(self.layoutWidget)
        self.edit_everyday_start_line_edit.setObjectName(u"edit_everyday_start_line_edit")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_start_line_edit)

        self.edit_everyday_finish_line_edit = QLineEdit(self.layoutWidget)
        self.edit_everyday_finish_line_edit.setObjectName(u"edit_everyday_finish_line_edit")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_finish_line_edit)

        self.edit_everyday_progress_line_edit_2 = QLineEdit(self.layoutWidget)
        self.edit_everyday_progress_line_edit_2.setObjectName(u"edit_everyday_progress_line_edit_2")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_progress_line_edit_2)

        self.edit_everyday_progress_line_edit = QLineEdit(self.layoutWidget)
        self.edit_everyday_progress_line_edit.setObjectName(u"edit_everyday_progress_line_edit")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_progress_line_edit)

        self.edit_everyday_status_line_edit = QLineEdit(self.layoutWidget)
        self.edit_everyday_status_line_edit.setObjectName(u"edit_everyday_status_line_edit")

        self.edit_everyday_line_edits.addWidget(self.edit_everyday_status_line_edit)

        self.layoutWidget_2 = QWidget(edit_everyday_project)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 330, 381, 81))
        self.everyday_return_exit_layout = QHBoxLayout(self.layoutWidget_2)
        self.everyday_return_exit_layout.setObjectName(u"everyday_return_exit_layout")
        self.everyday_return_exit_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_everyday_return_button = QPushButton(self.layoutWidget_2)
        self.edit_everyday_return_button.setObjectName(u"edit_everyday_return_button")

        self.everyday_return_exit_layout.addWidget(self.edit_everyday_return_button)

        self.edit_everyday_exit_button = QPushButton(self.layoutWidget_2)
        self.edit_everyday_exit_button.setObjectName(u"edit_everyday_exit_button")

        self.everyday_return_exit_layout.addWidget(self.edit_everyday_exit_button)


        self.retranslateUi(edit_everyday_project)

        QMetaObject.connectSlotsByName(edit_everyday_project)
    # setupUi

    def retranslateUi(self, edit_everyday_project):
        edit_everyday_project.setWindowTitle(QCoreApplication.translate("edit_everyday_project", u"Form", None))
        self.everyday_project_edit_button.setText(QCoreApplication.translate("edit_everyday_project", u"Edit project", None))
        self.edit_everyday_name_line_edit.setText(QCoreApplication.translate("edit_everyday_project", u"Project name", None))
        self.edit_everyday_start_line_edit.setText(QCoreApplication.translate("edit_everyday_project", u"Start date", None))
        self.edit_everyday_finish_line_edit.setText(QCoreApplication.translate("edit_everyday_project", u"Projected finish date", None))
        self.edit_everyday_progress_line_edit_2.setText(QCoreApplication.translate("edit_everyday_project", u"Project notes", None))
        self.edit_everyday_progress_line_edit.setText(QCoreApplication.translate("edit_everyday_project", u"Progress %", None))
        self.edit_everyday_status_line_edit.setText(QCoreApplication.translate("edit_everyday_project", u"Status", None))
        self.edit_everyday_return_button.setText(QCoreApplication.translate("edit_everyday_project", u"Return to main menu", None))
        self.edit_everyday_exit_button.setText(QCoreApplication.translate("edit_everyday_project", u"Exit program", None))
    # retranslateUi

