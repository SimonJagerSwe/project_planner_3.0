# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_planner_3.0.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_project_planner_main(object):
    def setupUi(self, project_planner_main):
        if not project_planner_main.objectName():
            project_planner_main.setObjectName(u"project_planner_main")
        project_planner_main.resize(590, 433)
        self.centralwidget = QWidget(project_planner_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(360, 20, 182, 371))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_project_button = QPushButton(self.widget)
        self.add_project_button.setObjectName(u"add_project_button")
        self.add_project_button.setMinimumSize(QSize(180, 0))
        self.add_project_button.setMaximumSize(QSize(220, 55))

        self.verticalLayout.addWidget(self.add_project_button)

        self.view_programming_button = QPushButton(self.widget)
        self.view_programming_button.setObjectName(u"view_programming_button")
        self.view_programming_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.view_programming_button)

        self.view_everyday_button = QPushButton(self.widget)
        self.view_everyday_button.setObjectName(u"view_everyday_button")
        self.view_everyday_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.view_everyday_button)

        self.view_archived_button = QPushButton(self.widget)
        self.view_archived_button.setObjectName(u"view_archived_button")
        self.view_archived_button.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.view_archived_button)

        self.exit_button_main = QPushButton(self.widget)
        self.exit_button_main.setObjectName(u"exit_button_main")
        self.exit_button_main.setMaximumSize(QSize(225, 55))

        self.verticalLayout.addWidget(self.exit_button_main)

        project_planner_main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(project_planner_main)
        self.statusbar.setObjectName(u"statusbar")
        project_planner_main.setStatusBar(self.statusbar)

        self.retranslateUi(project_planner_main)

        QMetaObject.connectSlotsByName(project_planner_main)
    # setupUi

    def retranslateUi(self, project_planner_main):
        project_planner_main.setWindowTitle(QCoreApplication.translate("project_planner_main", u"MainWindow", None))
        self.add_project_button.setText(QCoreApplication.translate("project_planner_main", u"Add new project", None))
        self.view_programming_button.setText(QCoreApplication.translate("project_planner_main", u"View programming projects", None))
        self.view_everyday_button.setText(QCoreApplication.translate("project_planner_main", u"View everyday projects", None))
        self.view_archived_button.setText(QCoreApplication.translate("project_planner_main", u"View archived projects", None))
        self.exit_button_main.setText(QCoreApplication.translate("project_planner_main", u"Exit program", None))
    # retranslateUi

