# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataentry.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1600, 700)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 321, 421))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.patientList = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.patientList.setObjectName("patientList")
        self.verticalLayout_2.addWidget(self.patientList)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.baselineExamSelect = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.baselineExamSelect.setObjectName("baselineExamSelect")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baselineExamSelect)
        self.btn_set_baseline = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_set_baseline.setObjectName("btn_set_baseline")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_set_baseline)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 450, 311, 111))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 30, 259, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 19, 61, 21))
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 50, 1201, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.tree_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.tree_container.setContentsMargins(0, 0, 0, 0)
        self.tree_container.setObjectName("tree_container")
        self.lineedit_patient_name = QtWidgets.QLineEdit(Form)
        self.lineedit_patient_name.setEnabled(False)
        self.lineedit_patient_name.setGeometry(QtCore.QRect(430, 20, 361, 22))
        self.lineedit_patient_name.setObjectName("lineedit_patient_name")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(40, 570, 311, 100))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_set_params = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_set_params.setObjectName("btn_set_params")
        self.verticalLayout_5.addWidget(self.btn_set_params)
        self.btn_reset = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout_5.addWidget(self.btn_reset)
        self.returnToHome = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.returnToHome.setObjectName("returnToHome")
        self.verticalLayout_5.addWidget(self.returnToHome)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Patient Data Overrides"))
        self.label_4.setText(_translate("Form", "Patient Selection (highlight patient to modify):"))
        self.label_3.setText(_translate("Form", "Baseline Exam:"))
        self.btn_set_baseline.setText(_translate("Form", "Set Baseline"))
        self.groupBox.setTitle(_translate("Form", "Additional Controls"))
        self.label_5.setText(_translate("Form", "Course:"))
        self.label_6.setText(_translate("Form", "Day:"))
        self.label_7.setText(_translate("Form", "Patient:"))
        self.btn_set_params.setText(_translate("Form", "Set Updated Patient Parameters"))
        self.btn_reset.setText(_translate("Form", "Reset Patient"))
        self.returnToHome.setText(_translate("Form", "Return Home (will automatically apply all changes!)"))

