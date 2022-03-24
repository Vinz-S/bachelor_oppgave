# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResetgraphDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import dia_img_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 115)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("#Dialog{\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"#label{\n"
"    color: rgb(249,249,249);\n"
"}\n"
"#pushButton{\n"
"    background-color: rgb(40, 40, 40);\n"
"    border : none\n"
"}\n"
"#yesButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#yesButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#noButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#noButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#widget{\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-radius: 4px;\n"
"}")
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yesButton = QtWidgets.QPushButton(self.widget)
        self.yesButton.setMinimumSize(QtCore.QSize(0, 20))
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtWidgets.QPushButton(self.widget)
        self.noButton.setMinimumSize(QtCore.QSize(0, 20))
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/yellow_warning.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Do you want to reset graphplot?"))
        self.yesButton.setText(_translate("Dialog", "Yes"))
        self.noButton.setText(_translate("Dialog", "No"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
