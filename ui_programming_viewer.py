# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programming_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_programming_viewer(object):
    def setupUi(self, programming_viewer):
        if not programming_viewer.objectName():
            programming_viewer.setObjectName(u"programming_viewer")
        programming_viewer.resize(590, 549)
        self.widget = QWidget(programming_viewer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 410, 461, 111))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_button_programming = QPushButton(self.widget)
        self.main_menu_button_programming.setObjectName(u"main_menu_button_programming")
        self.main_menu_button_programming.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.main_menu_button_programming)

        self.exit_button_programming = QPushButton(self.widget)
        self.exit_button_programming.setObjectName(u"exit_button_programming")
        self.exit_button_programming.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.exit_button_programming)


        self.retranslateUi(programming_viewer)

        QMetaObject.connectSlotsByName(programming_viewer)
    # setupUi

    def retranslateUi(self, programming_viewer):
        programming_viewer.setWindowTitle(QCoreApplication.translate("programming_viewer", u"Form", None))
        self.main_menu_button_programming.setText(QCoreApplication.translate("programming_viewer", u"Return to main menu", None))
        self.exit_button_programming.setText(QCoreApplication.translate("programming_viewer", u"Exit program", None))
    # retranslateUi

