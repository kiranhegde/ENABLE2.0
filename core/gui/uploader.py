# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadform.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_databaseuploaddialog(object):
    def setupUi(self, databaseuploaddialog):
        databaseuploaddialog.setObjectName("databaseuploaddialog")
        databaseuploaddialog.resize(913, 604)
        self.horizontalLayoutWidget = QtWidgets.QWidget(databaseuploaddialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 851, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 40, 251, 116))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.labmatrixUser = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.labmatrixUser.setObjectName("labmatrixUser")
        self.horizontalLayout_5.addWidget(self.labmatrixUser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.labmatrixPass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.labmatrixPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.labmatrixPass.setObjectName("labmatrixPass")
        self.horizontalLayout_4.addWidget(self.labmatrixPass)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.labmatrixLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.labmatrixLogin.setObjectName("labmatrixLogin")
        self.verticalLayout_3.addWidget(self.labmatrixLogin)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 160, 251, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.labmatrixPtList = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.labmatrixPtList.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.labmatrixPtList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.labmatrixPtList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.labmatrixPtList.setObjectName("labmatrixPtList")
        self.verticalLayout_6.addWidget(self.labmatrixPtList)
        self.labmatrixUpload = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.labmatrixUpload.setObjectName("labmatrixUpload")
        self.verticalLayout_6.addWidget(self.labmatrixUpload)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 251, 116))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.crisUser = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.crisUser.setObjectName("crisUser")
        self.horizontalLayout_6.addWidget(self.crisUser)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.crisPass = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.crisPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.crisPass.setObjectName("crisPass")
        self.horizontalLayout_7.addWidget(self.crisPass)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.crisLogin = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.crisLogin.setObjectName("crisLogin")
        self.verticalLayout_7.addWidget(self.crisLogin)
        self.groupBox_3.raise_()
        self.groupBox_3.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.horizontalLayout.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 251, 116))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.c3dUser = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.c3dUser.setObjectName("c3dUser")
        self.horizontalLayout_8.addWidget(self.c3dUser)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.c3dPass = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.c3dPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.c3dPass.setObjectName("c3dPass")
        self.horizontalLayout_9.addWidget(self.c3dPass)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.c3dLogin = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.c3dLogin.setObjectName("c3dLogin")
        self.verticalLayout_8.addWidget(self.c3dLogin)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(databaseuploaddialog)
        QtCore.QMetaObject.connectSlotsByName(databaseuploaddialog)

    def retranslateUi(self, databaseuploaddialog):
        _translate = QtCore.QCoreApplication.translate
        databaseuploaddialog.setWindowTitle(_translate("databaseuploaddialog", "Database Uploader"))
        self.groupBox_3.setTitle(_translate("databaseuploaddialog", "Labmatrix"))
        self.label_2.setText(_translate("databaseuploaddialog", "Username:"))
        self.label.setText(_translate("databaseuploaddialog", "Password:"))
        self.labmatrixLogin.setText(_translate("databaseuploaddialog", "Log in"))
        self.label_3.setText(_translate("databaseuploaddialog", "Patient selection:"))
        self.labmatrixUpload.setText(_translate("databaseuploaddialog", "Upload"))
        self.groupBox.setTitle(_translate("databaseuploaddialog", "CRIS"))
        self.label_4.setText(_translate("databaseuploaddialog", "Username:"))
        self.label_5.setText(_translate("databaseuploaddialog", "Password:"))
        self.crisLogin.setText(_translate("databaseuploaddialog", "Log in"))
        self.groupBox_2.setTitle(_translate("databaseuploaddialog", "C3D"))
        self.label_6.setText(_translate("databaseuploaddialog", "Username:"))
        self.label_7.setText(_translate("databaseuploaddialog", "Password:"))
        self.c3dLogin.setText(_translate("databaseuploaddialog", "Log in"))
