# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(638, 444)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ed_url = QLineEdit(Widget)
        self.ed_url.setObjectName(u"ed_url")
        self.ed_url.setEnabled(True)
        font = QFont()
        font.setPointSize(12)
        self.ed_url.setFont(font)

        self.horizontalLayout.addWidget(self.ed_url)

        self.btn_check = QPushButton(Widget)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(14)
        self.btn_check.setFont(font1)
        self.btn_check.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_check)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_file = QPushButton(Widget)
        self.btn_file.setObjectName(u"btn_file")

        self.horizontalLayout_2.addWidget(self.btn_file)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(True)
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)

        self.ed_format = QLineEdit(Widget)
        self.ed_format.setObjectName(u"ed_format")

        self.horizontalLayout_2.addWidget(self.ed_format)

        self.btn_down = QPushButton(Widget)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setEnabled(False)
        self.btn_down.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_down)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.sa_inform = QWidget()
        self.sa_inform.setObjectName(u"sa_inform")
        self.sa_inform.setGeometry(QRect(0, 0, 620, 360))
        self.scrollArea.setWidget(self.sa_inform)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.ed_url.setToolTip(QCoreApplication.translate("Widget", u"just input the url where the album is", None))
#endif // QT_CONFIG(tooltip)
        self.ed_url.setInputMask("")
        self.ed_url.setPlaceholderText(QCoreApplication.translate("Widget", u"https://downloads.khinsider.com/game-soundtracks/album/xxx", None))
#if QT_CONFIG(whatsthis)
        self.btn_check.setWhatsThis(QCoreApplication.translate("Widget", u"check", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_check.setText(QCoreApplication.translate("Widget", u"Check", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"by de8ug", None))
#if QT_CONFIG(tooltip)
        self.btn_file.setToolTip(QCoreApplication.translate("Widget", u"deafult is ./", None))
#endif // QT_CONFIG(tooltip)
        self.btn_file.setText(QCoreApplication.translate("Widget", u"save path", None))
        self.label.setText(QCoreApplication.translate("Widget", u"please input format", None))
        self.ed_format.setPlaceholderText(QCoreApplication.translate("Widget", u"FLAC", None))
        self.btn_down.setText(QCoreApplication.translate("Widget", u"Download", None))
    # retranslateUi

