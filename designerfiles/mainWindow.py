# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1917, 973)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#Backround{\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"#Sone1{\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"#Sone2{\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"#forceGraph{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"#stressGraph{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"#TitleBox{\n"
"        background-color: rgb(55,55,55);\n"
"}\n"
"#frame{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"#startButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#startButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#stopButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#stopButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#tensileButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#tensileButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#compressButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#compressButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#autoZeroButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"#strenghtRangeCbox{\n"
"        background-color: rgb(70,70,70);\n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"QListView{\n"
"        background-color: rgb(70,70,70);\n"
"        border-radius: 0px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"#autoZeroButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#resetGraphButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetGraphButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#releaseMatButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#releaseMatButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#saveGraphButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#saveGraphButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"#RWinitialForce{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWlengthRange{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWtensileSpeed{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWmaxForce{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#settingsWindow{\n"
"    background-color: rgb(232, 253, 255);\n"
"}\n"
"#directDataWindow{\n"
"    background-color: rgb(232, 253, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"#title{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_1{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_2{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_3{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_4{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_5{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_6{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_7{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_8{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_9{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_10{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_11{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_12{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_13{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_14{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_15{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_16{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_17{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Backround = QtWidgets.QWidget(self.centralwidget)
        self.Backround.setStyleSheet("")
        self.Backround.setObjectName("Backround")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Backround)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.Backround)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(450, 0))
        self.frame.setMaximumSize(QtCore.QSize(450, 962))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.TitleBox = QtWidgets.QWidget(self.frame)
        self.TitleBox.setMinimumSize(QtCore.QSize(0, 100))
        self.TitleBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleBox.setStyleSheet("")
        self.TitleBox.setObjectName("TitleBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TitleBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.title = QtWidgets.QLabel(self.TitleBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_5.addWidget(self.title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.TitleBox, 0, 0, 1, 1)
        self.Sone1 = QtWidgets.QWidget(self.frame)
        self.Sone1.setMaximumSize(QtCore.QSize(16777215, 600))
        self.Sone1.setStyleSheet("")
        self.Sone1.setObjectName("Sone1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Sone1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stopButton = QtWidgets.QPushButton(self.Sone1)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_3.addWidget(self.stopButton, 7, 0, 1, 1)
        self.compressButton = QtWidgets.QPushButton(self.Sone1)
        self.compressButton.setMinimumSize(QtCore.QSize(190, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.compressButton.setFont(font)
        self.compressButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compressButton.setObjectName("compressButton")
        self.gridLayout_3.addWidget(self.compressButton, 7, 1, 1, 1)
        self.tensileButton = QtWidgets.QPushButton(self.Sone1)
        self.tensileButton.setMinimumSize(QtCore.QSize(190, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.tensileButton.setFont(font)
        self.tensileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tensileButton.setObjectName("tensileButton")
        self.gridLayout_3.addWidget(self.tensileButton, 6, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.Sone1)
        self.startButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 6, 0, 1, 1)
        self.tensileButton.raise_()
        self.compressButton.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()
        self.gridLayout_8.addWidget(self.Sone1, 1, 0, 1, 1)
        self.Sone2 = QtWidgets.QWidget(self.frame)
        self.Sone2.setMaximumSize(QtCore.QSize(16777215, 900))
        self.Sone2.setStyleSheet("#timeRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#epsilonRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#forceRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#lengthRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#stressRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetTimeButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetTimeButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#setZeroButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#setZeroButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"")
        self.Sone2.setObjectName("Sone2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Sone2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timeRead = QtWidgets.QSpinBox(self.Sone2)
        self.timeRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.timeRead.setFont(font)
        self.timeRead.setAlignment(QtCore.Qt.AlignCenter)
        self.timeRead.setReadOnly(True)
        self.timeRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeRead.setMinimum(0)
        self.timeRead.setMaximum(999999999)
        self.timeRead.setObjectName("timeRead")
        self.gridLayout_4.addWidget(self.timeRead, 3, 5, 1, 1)
        self.forceRead = QtWidgets.QSpinBox(self.Sone2)
        self.forceRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.forceRead.setFont(font)
        self.forceRead.setAlignment(QtCore.Qt.AlignCenter)
        self.forceRead.setReadOnly(True)
        self.forceRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.forceRead.setPrefix("")
        self.forceRead.setMinimum(-999999999)
        self.forceRead.setMaximum(999999999)
        self.forceRead.setObjectName("forceRead")
        self.gridLayout_4.addWidget(self.forceRead, 10, 2, 1, 1)
        self.lengthRead = QtWidgets.QSpinBox(self.Sone2)
        self.lengthRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lengthRead.setFont(font)
        self.lengthRead.setAlignment(QtCore.Qt.AlignCenter)
        self.lengthRead.setReadOnly(True)
        self.lengthRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.lengthRead.setMinimum(-999999999)
        self.lengthRead.setMaximum(999999999)
        self.lengthRead.setObjectName("lengthRead")
        self.gridLayout_4.addWidget(self.lengthRead, 10, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 9, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.epsilonRead = QtWidgets.QSpinBox(self.Sone2)
        self.epsilonRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.epsilonRead.setFont(font)
        self.epsilonRead.setAlignment(QtCore.Qt.AlignCenter)
        self.epsilonRead.setReadOnly(True)
        self.epsilonRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.epsilonRead.setMinimum(-999999999)
        self.epsilonRead.setMaximum(999999999)
        self.epsilonRead.setObjectName("epsilonRead")
        self.gridLayout_4.addWidget(self.epsilonRead, 3, 3, 1, 1)
        self.setZeroButton = QtWidgets.QPushButton(self.Sone2)
        self.setZeroButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        self.setZeroButton.setFont(font)
        self.setZeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setZeroButton.setObjectName("setZeroButton")
        self.gridLayout_4.addWidget(self.setZeroButton, 11, 3, 1, 1)
        self.stressRead = QtWidgets.QSpinBox(self.Sone2)
        self.stressRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.stressRead.setFont(font)
        self.stressRead.setAlignment(QtCore.Qt.AlignCenter)
        self.stressRead.setReadOnly(True)
        self.stressRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stressRead.setMinimum(-999999999)
        self.stressRead.setMaximum(999999999)
        self.stressRead.setObjectName("stressRead")
        self.gridLayout_4.addWidget(self.stressRead, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 3, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 9, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.Sone2, 5, 0, 1, 1)
        self.sone1_1 = QtWidgets.QWidget(self.frame)
        self.sone1_1.setMinimumSize(QtCore.QSize(0, 280))
        self.sone1_1.setMaximumSize(QtCore.QSize(16777215, 280))
        self.sone1_1.setObjectName("sone1_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sone1_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.sone1_1)
        self.widget.setMinimumSize(QtCore.QSize(0, 140))
        self.widget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 4, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.sone1_1)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_4.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_12.addWidget(self.label, 1, 0, 1, 1)
        self.RWlengthRange = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWlengthRange.setFont(font)
        self.RWlengthRange.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWlengthRange.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWlengthRange.setMaximum(999999999.0)
        self.RWlengthRange.setObjectName("RWlengthRange")
        self.gridLayout_12.addWidget(self.RWlengthRange, 2, 1, 1, 1)
        self.RWmaxForce = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.RWmaxForce.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWmaxForce.setFont(font)
        self.RWmaxForce.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWmaxForce.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWmaxForce.setMaximum(2500.0)
        self.RWmaxForce.setObjectName("RWmaxForce")
        self.gridLayout_12.addWidget(self.RWmaxForce, 0, 1, 1, 1)
        self.RWinitialForce = QtWidgets.QDoubleSpinBox(self.widget_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RWinitialForce.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWinitialForce.setFont(font)
        self.RWinitialForce.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWinitialForce.setFrame(False)
        self.RWinitialForce.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RWinitialForce.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWinitialForce.setKeyboardTracking(True)
        self.RWinitialForce.setMaximum(10000.0)
        self.RWinitialForce.setObjectName("RWinitialForce")
        self.gridLayout_12.addWidget(self.RWinitialForce, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 3, 0, 1, 1)
        self.RWtensileSpeed = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWtensileSpeed.setFont(font)
        self.RWtensileSpeed.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWtensileSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWtensileSpeed.setObjectName("RWtensileSpeed")
        self.gridLayout_12.addWidget(self.RWtensileSpeed, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 4, 0, 1, 1)
        self.strenghtRangeCbox = QtWidgets.QComboBox(self.widget_4)
        self.strenghtRangeCbox.setEnabled(True)
        self.strenghtRangeCbox.setMinimumSize(QtCore.QSize(0, 0))
        self.strenghtRangeCbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strenghtRangeCbox.setFont(font)
        self.strenghtRangeCbox.setAutoFillBackground(False)
        self.strenghtRangeCbox.setDuplicatesEnabled(False)
        self.strenghtRangeCbox.setFrame(True)
        self.strenghtRangeCbox.setObjectName("strenghtRangeCbox")
        self.strenghtRangeCbox.addItem("")
        self.strenghtRangeCbox.addItem("")
        self.strenghtRangeCbox.addItem("")
        self.gridLayout_12.addWidget(self.strenghtRangeCbox, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_4, 4, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.sone1_1)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.releaseMatButton = QtWidgets.QPushButton(self.widget_3)
        self.releaseMatButton.setMinimumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.releaseMatButton.setFont(font)
        self.releaseMatButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.releaseMatButton.setObjectName("releaseMatButton")
        self.gridLayout_11.addWidget(self.releaseMatButton, 0, 2, 1, 2)
        self.autoZeroButton = QtWidgets.QPushButton(self.widget_3)
        self.autoZeroButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.autoZeroButton.setFont(font)
        self.autoZeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.autoZeroButton.setObjectName("autoZeroButton")
        self.gridLayout_11.addWidget(self.autoZeroButton, 0, 0, 1, 2)
        self.resetGraphButton = QtWidgets.QPushButton(self.widget_3)
        self.resetGraphButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.resetGraphButton.setFont(font)
        self.resetGraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetGraphButton.setObjectName("resetGraphButton")
        self.gridLayout_11.addWidget(self.resetGraphButton, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.widget_3, 5, 0, 1, 2)
        self.gridLayout_8.addWidget(self.sone1_1, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame)
        self.widget_2 = QtWidgets.QWidget(self.Backround)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.forceGraph = QtWidgets.QWidget(self.widget_2)
        self.forceGraph.setStyleSheet("")
        self.forceGraph.setObjectName("forceGraph")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.forceGraph)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.forceWidget = QtWidgets.QWidget(self.forceGraph)
        self.forceWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.forceWidget.setObjectName("forceWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.forceWidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.forceWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_10.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.forceWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.forceGraph)
        self.stressGraph = QtWidgets.QWidget(self.widget_2)
        self.stressGraph.setMinimumSize(QtCore.QSize(600, 0))
        self.stressGraph.setStyleSheet("")
        self.stressGraph.setObjectName("stressGraph")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.stressGraph)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stressWidget = QtWidgets.QWidget(self.stressGraph)
        self.stressWidget.setObjectName("stressWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.stressWidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.stressWidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_9.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.stressWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.stressGraph)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.Backround, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1917, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuCOM_Port = QtWidgets.QMenu(self.menuTools)
        self.menuCOM_Port.setObjectName("menuCOM_Port")
        MainWindow.setMenuBar(self.menubar)
        self.actionGeometry = QtWidgets.QAction(MainWindow)
        self.actionGeometry.setObjectName("actionGeometry")
        self.actionCOM1 = QtWidgets.QAction(MainWindow)
        self.actionCOM1.setObjectName("actionCOM1")
        self.actionCOM9 = QtWidgets.QAction(MainWindow)
        self.actionCOM9.setObjectName("actionCOM9")
        self.actionReset_ADC = QtWidgets.QAction(MainWindow)
        self.actionReset_ADC.setObjectName("actionReset_ADC")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionExport)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuCOM_Port.menuAction())
        self.menuTools.addAction(self.actionGeometry)
        self.menuTools.addAction(self.actionReset_ADC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Tensile Testing</span></p></body></html>"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.compressButton.setText(_translate("MainWindow", "Compress"))
        self.tensileButton.setText(_translate("MainWindow", "Tensile"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.timeRead.setSuffix(_translate("MainWindow", " s"))
        self.forceRead.setSuffix(_translate("MainWindow", " N"))
        self.lengthRead.setSuffix(_translate("MainWindow", " μm"))
        self.label_6.setText(_translate("MainWindow", "Length"))
        self.epsilonRead.setSuffix(_translate("MainWindow", " ɛ "))
        self.setZeroButton.setText(_translate("MainWindow", "Set zero"))
        self.stressRead.setSuffix(_translate("MainWindow", " Mpa"))
        self.label_8.setText(_translate("MainWindow", "Strain"))
        self.label_9.setText(_translate("MainWindow", "Stress"))
        self.label_5.setText(_translate("MainWindow", "Force"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.label.setText(_translate("MainWindow", "Tensile-speed:"))
        self.RWlengthRange.setSuffix(_translate("MainWindow", " μm"))
        self.RWmaxForce.setSuffix(_translate("MainWindow", " N"))
        self.RWinitialForce.setSuffix(_translate("MainWindow", " N"))
        self.label_2.setText(_translate("MainWindow", "Max force:"))
        self.label_4.setText(_translate("MainWindow", "Initial force:"))
        self.RWtensileSpeed.setSuffix(_translate("MainWindow", " μm/s"))
        self.label_3.setText(_translate("MainWindow", "Length range:"))
        self.label_10.setText(_translate("MainWindow", "Strength range:"))
        self.strenghtRangeCbox.setItemText(0, _translate("MainWindow", "S1 - 3KN"))
        self.strenghtRangeCbox.setItemText(1, _translate("MainWindow", "S2 - 5KN"))
        self.strenghtRangeCbox.setItemText(2, _translate("MainWindow", "S3 - 10KN"))
        self.releaseMatButton.setText(_translate("MainWindow", "Release"))
        self.autoZeroButton.setText(_translate("MainWindow", "Auto zero"))
        self.resetGraphButton.setText(_translate("MainWindow", "Reset graph"))
        self.label_17.setText(_translate("MainWindow", "Direct data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuCOM_Port.setTitle(_translate("MainWindow", "Port"))
        self.actionGeometry.setText(_translate("MainWindow", "Geometry"))
        self.actionCOM1.setText(_translate("MainWindow", "COM1"))
        self.actionCOM9.setText(_translate("MainWindow", "COM9"))
        self.actionReset_ADC.setText(_translate("MainWindow", "Reset ADC"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
