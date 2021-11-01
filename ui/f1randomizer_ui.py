# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'f1randomizer_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import images_qrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1061, 649)
        MainWindow.setStyleSheet(u"# background-color: rgb(30, 30, 30);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.header_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u":/images/images/formula-1-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(120, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bauhaus 93"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimize_button = QPushButton(self.frame_6)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(25, 25))
        self.minimize_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/minimize_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.frame_6)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.track_widget = QTableWidget(self.frame_13)
        if (self.track_widget.columnCount() < 3):
            self.track_widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.track_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.track_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.track_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.track_widget.rowCount() < 22):
            self.track_widget.setRowCount(22)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(20, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.track_widget.setVerticalHeaderItem(21, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.track_widget.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.track_widget.setItem(0, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(1, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.track_widget.setItem(1, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.track_widget.setItem(1, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(2, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.track_widget.setItem(2, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.track_widget.setItem(2, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(3, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.track_widget.setItem(3, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.track_widget.setItem(3, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(4, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.track_widget.setItem(4, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.track_widget.setItem(4, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(5, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.track_widget.setItem(5, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.track_widget.setItem(5, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(6, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.track_widget.setItem(6, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.track_widget.setItem(6, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(7, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.track_widget.setItem(7, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.track_widget.setItem(7, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(8, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.track_widget.setItem(8, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.track_widget.setItem(8, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(9, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.track_widget.setItem(9, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.track_widget.setItem(9, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(10, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.track_widget.setItem(10, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.track_widget.setItem(10, 2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(11, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.track_widget.setItem(11, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.track_widget.setItem(11, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(12, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.track_widget.setItem(12, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.track_widget.setItem(12, 2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(13, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.track_widget.setItem(13, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.track_widget.setItem(13, 2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(14, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.track_widget.setItem(14, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.track_widget.setItem(14, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(15, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.track_widget.setItem(15, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.track_widget.setItem(15, 2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(16, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.track_widget.setItem(16, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.track_widget.setItem(16, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(17, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.track_widget.setItem(17, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.track_widget.setItem(17, 2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(18, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.track_widget.setItem(18, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.track_widget.setItem(18, 2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(19, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.track_widget.setItem(19, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.track_widget.setItem(19, 2, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(20, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.track_widget.setItem(20, 1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.track_widget.setItem(20, 2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setCheckState(Qt.Unchecked);
        self.track_widget.setItem(21, 0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.track_widget.setItem(21, 1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.track_widget.setItem(21, 2, __qtablewidgetitem90)
        self.track_widget.setObjectName(u"track_widget")
        self.track_widget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.track_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.track_widget.horizontalHeader().setDefaultSectionSize(158)

        self.verticalLayout_6.addWidget(self.track_widget)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_14)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.frame_22)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_6)


        self.horizontalLayout_11.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.multiple_tracks = QCheckBox(self.frame_21)
        self.multiple_tracks.setObjectName(u"multiple_tracks")
        self.multiple_tracks.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.multiple_tracks)


        self.horizontalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_5.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.spinBox = QSpinBox(self.frame_19)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.spinBox)


        self.verticalLayout_5.addWidget(self.frame_19)


        self.horizontalLayout_8.addWidget(self.frame)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.generate_button = QPushButton(self.frame_18)
        self.generate_button.setObjectName(u"generate_button")
        font2 = QFont()
        font2.setFamilies([u"Bauhaus 93"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.generate_button.setFont(font2)
        self.generate_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.generate_button)


        self.horizontalLayout_8.addWidget(self.frame_18)


        self.verticalLayout_3.addWidget(self.frame_14, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_15, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy2.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy2)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.result_table_widget = QTableWidget(self.frame_16)
        if (self.result_table_widget.columnCount() < 2):
            self.result_table_widget.setColumnCount(2)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.result_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.result_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem92)
        self.result_table_widget.setObjectName(u"result_table_widget")
        self.result_table_widget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.result_table_widget.horizontalHeader().setDefaultSectionSize(250)

        self.verticalLayout_7.addWidget(self.result_table_widget)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_17)


        self.horizontalLayout_5.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Randomizer", None))
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbare Strecken", None))
        ___qtablewidgetitem = self.track_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Unbedingt", None));
        ___qtablewidgetitem1 = self.track_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Land", None));
        ___qtablewidgetitem2 = self.track_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Streckenname", None));
        ___qtablewidgetitem3 = self.track_widget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.track_widget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.track_widget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.track_widget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem7 = self.track_widget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem8 = self.track_widget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.track_widget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem10 = self.track_widget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem11 = self.track_widget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem12 = self.track_widget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem13 = self.track_widget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem14 = self.track_widget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem15 = self.track_widget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem16 = self.track_widget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem17 = self.track_widget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem18 = self.track_widget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem19 = self.track_widget.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem20 = self.track_widget.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem21 = self.track_widget.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem22 = self.track_widget.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem23 = self.track_widget.verticalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem24 = self.track_widget.verticalHeaderItem(21)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"22", None));

        __sortingEnabled = self.track_widget.isSortingEnabled()
        self.track_widget.setSortingEnabled(False)
        ___qtablewidgetitem25 = self.track_widget.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Australia", None));
        ___qtablewidgetitem26 = self.track_widget.item(0, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Albert Park Circuit", None));
        ___qtablewidgetitem27 = self.track_widget.item(1, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bahrain", None));
        ___qtablewidgetitem28 = self.track_widget.item(1, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Bahrain International Circuit", None));
        ___qtablewidgetitem29 = self.track_widget.item(2, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Vietnam", None));
        ___qtablewidgetitem30 = self.track_widget.item(2, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Hanoi Street Circuit", None));
        ___qtablewidgetitem31 = self.track_widget.item(3, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"China", None));
        ___qtablewidgetitem32 = self.track_widget.item(3, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Shanghai International Circuit", None));
        ___qtablewidgetitem33 = self.track_widget.item(4, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Netherlands", None));
        ___qtablewidgetitem34 = self.track_widget.item(4, 2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Circuit Park Zandvoort", None));
        ___qtablewidgetitem35 = self.track_widget.item(5, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Spain", None));
        ___qtablewidgetitem36 = self.track_widget.item(5, 2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Circuit de Barcelona-Catalunya", None));
        ___qtablewidgetitem37 = self.track_widget.item(6, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Monaco", None));
        ___qtablewidgetitem38 = self.track_widget.item(6, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Circuit de Monaco", None));
        ___qtablewidgetitem39 = self.track_widget.item(7, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Azerbaijan", None));
        ___qtablewidgetitem40 = self.track_widget.item(7, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Baku City Circuit", None));
        ___qtablewidgetitem41 = self.track_widget.item(8, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Canada", None));
        ___qtablewidgetitem42 = self.track_widget.item(8, 2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Circuit Gilles-Villeneuve", None));
        ___qtablewidgetitem43 = self.track_widget.item(9, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"France", None));
        ___qtablewidgetitem44 = self.track_widget.item(9, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Circuit Paul Ricard", None));
        ___qtablewidgetitem45 = self.track_widget.item(10, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Austria", None));
        ___qtablewidgetitem46 = self.track_widget.item(10, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Red Bull Ring", None));
        ___qtablewidgetitem47 = self.track_widget.item(11, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Britain", None));
        ___qtablewidgetitem48 = self.track_widget.item(11, 2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Silverstone Circuit", None));
        ___qtablewidgetitem49 = self.track_widget.item(12, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Hungary", None));
        ___qtablewidgetitem50 = self.track_widget.item(12, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Hungaroring", None));
        ___qtablewidgetitem51 = self.track_widget.item(13, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Belgium", None));
        ___qtablewidgetitem52 = self.track_widget.item(13, 2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Circuit de Spa-Francorchamps", None));
        ___qtablewidgetitem53 = self.track_widget.item(14, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Italy", None));
        ___qtablewidgetitem54 = self.track_widget.item(14, 2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Autodromo Nazionale Monza", None));
        ___qtablewidgetitem55 = self.track_widget.item(15, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Singapore", None));
        ___qtablewidgetitem56 = self.track_widget.item(15, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Marina Bay Street Circuit", None));
        ___qtablewidgetitem57 = self.track_widget.item(16, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Russia", None));
        ___qtablewidgetitem58 = self.track_widget.item(16, 2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Sochi Autodrom", None));
        ___qtablewidgetitem59 = self.track_widget.item(17, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Japan", None));
        ___qtablewidgetitem60 = self.track_widget.item(17, 2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Suzuka International Racing Course", None));
        ___qtablewidgetitem61 = self.track_widget.item(18, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"USA", None));
        ___qtablewidgetitem62 = self.track_widget.item(18, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Circuit of the Americas", None));
        ___qtablewidgetitem63 = self.track_widget.item(19, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Mexico", None));
        ___qtablewidgetitem64 = self.track_widget.item(19, 2)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Aut\u00f3dromo Hermanos Rodr\u00edguez", None));
        ___qtablewidgetitem65 = self.track_widget.item(20, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Brazil", None));
        ___qtablewidgetitem66 = self.track_widget.item(20, 2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Aut\u00f3dromo Jos\u00e9 Carlos Pace", None));
        ___qtablewidgetitem67 = self.track_widget.item(21, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Abu Dhabi", None));
        ___qtablewidgetitem68 = self.track_widget.item(21, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Yas Marina Circuit", None));
        self.track_widget.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Strecken mehrfach einf\u00fcgen", None))
        self.multiple_tracks.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Anzahl Rennen", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generieren", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ergebnis", None))
        ___qtablewidgetitem69 = self.result_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Land", None));
        ___qtablewidgetitem70 = self.result_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Streckenname", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2021, Steve Hamann & Marcel Peplies", None))
    # retranslateUi

