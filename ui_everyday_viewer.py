# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'everyday_viewer.ui'
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

class Ui_everyday_viewer(object):
    def setupUi(self, everyday_viewer):
        if not everyday_viewer.objectName():
            everyday_viewer.setObjectName(u"everyday_viewer")
        everyday_viewer.resize(590, 549)
        self.layoutWidget = QWidget(everyday_viewer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 410, 461, 111))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_button_everyday = QPushButton(self.layoutWidget)
        self.main_menu_button_everyday.setObjectName(u"main_menu_button_everyday")
        self.main_menu_button_everyday.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.main_menu_button_everyday)

        self.exit_button_everyday = QPushButton(self.layoutWidget)
        self.exit_button_everyday.setObjectName(u"exit_button_everyday")
        self.exit_button_everyday.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.exit_button_everyday)


        self.retranslateUi(everyday_viewer)

        QMetaObject.connectSlotsByName(everyday_viewer)
    # setupUi

    def retranslateUi(self, everyday_viewer):
        everyday_viewer.setWindowTitle(QCoreApplication.translate("everyday_viewer", u"Form", None))
        self.main_menu_button_everyday.setText(QCoreApplication.translate("everyday_viewer", u"Return to main menu", None))
        self.exit_button_everyday.setText(QCoreApplication.translate("everyday_viewer", u"Exit program", None))
    # retranslateUi

