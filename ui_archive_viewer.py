# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archive_viewer.ui'
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

class Ui_archive_viewer(object):
    def setupUi(self, archive_viewer):
        if not archive_viewer.objectName():
            archive_viewer.setObjectName(u"archive_viewer")
        archive_viewer.resize(744, 321)
        self.layoutWidget = QWidget(archive_viewer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 190, 461, 111))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_button_archive = QPushButton(self.layoutWidget)
        self.main_menu_button_archive.setObjectName(u"main_menu_button_archive")
        self.main_menu_button_archive.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.main_menu_button_archive)

        self.exit_button_archive = QPushButton(self.layoutWidget)
        self.exit_button_archive.setObjectName(u"exit_button_archive")
        self.exit_button_archive.setMaximumSize(QSize(225, 55))

        self.horizontalLayout.addWidget(self.exit_button_archive)

        self.widget = QWidget(archive_viewer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 701, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_menu_button_archive_2 = QPushButton(self.widget)
        self.main_menu_button_archive_2.setObjectName(u"main_menu_button_archive_2")
        self.main_menu_button_archive_2.setMaximumSize(QSize(225, 55))

        self.horizontalLayout_2.addWidget(self.main_menu_button_archive_2)

        self.main_menu_button_archive_3 = QPushButton(self.widget)
        self.main_menu_button_archive_3.setObjectName(u"main_menu_button_archive_3")
        self.main_menu_button_archive_3.setMaximumSize(QSize(225, 55))

        self.horizontalLayout_2.addWidget(self.main_menu_button_archive_3)

        self.main_menu_button_archive_4 = QPushButton(self.widget)
        self.main_menu_button_archive_4.setObjectName(u"main_menu_button_archive_4")
        self.main_menu_button_archive_4.setMaximumSize(QSize(225, 55))

        self.horizontalLayout_2.addWidget(self.main_menu_button_archive_4)


        self.retranslateUi(archive_viewer)

        QMetaObject.connectSlotsByName(archive_viewer)
    # setupUi

    def retranslateUi(self, archive_viewer):
        archive_viewer.setWindowTitle(QCoreApplication.translate("archive_viewer", u"Form", None))
        self.main_menu_button_archive.setText(QCoreApplication.translate("archive_viewer", u"Return to main menu", None))
        self.exit_button_archive.setText(QCoreApplication.translate("archive_viewer", u"Exit program", None))
        self.main_menu_button_archive_2.setText(QCoreApplication.translate("archive_viewer", u"View programming archive", None))
        self.main_menu_button_archive_3.setText(QCoreApplication.translate("archive_viewer", u"View everyday archive", None))
        self.main_menu_button_archive_4.setText(QCoreApplication.translate("archive_viewer", u"View full archive", None))
    # retranslateUi

