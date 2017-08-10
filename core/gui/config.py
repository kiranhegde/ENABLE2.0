# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configuration(object):
    def setupUi(self, configuration):
        configuration.setObjectName("configuration")
        configuration.resize(741, 275)
        self.verticalLayout = QtWidgets.QVBoxLayout(configuration)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(configuration)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(configuration)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.admin_pass = QtWidgets.QLineEdit(configuration)
        self.admin_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_pass.setObjectName("admin_pass")
        self.horizontalLayout.addWidget(self.admin_pass)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(configuration)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.bl_directory = QtWidgets.QLineEdit(configuration)
        self.bl_directory.setEnabled(False)
        self.bl_directory.setObjectName("bl_directory")
        self.horizontalLayout_3.addWidget(self.bl_directory)
        self.btn_bl_directory = QtWidgets.QPushButton(configuration)
        self.btn_bl_directory.setObjectName("btn_bl_directory")
        self.horizontalLayout_3.addWidget(self.btn_bl_directory)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(configuration)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.output_directory = QtWidgets.QLineEdit(configuration)
        self.output_directory.setEnabled(False)
        self.output_directory.setObjectName("output_directory")
        self.horizontalLayout_4.addWidget(self.output_directory)
        self.btn_output_directory = QtWidgets.QPushButton(configuration)
        self.btn_output_directory.setObjectName("btn_output_directory")
        self.horizontalLayout_4.addWidget(self.btn_output_directory)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(configuration)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.db_path = QtWidgets.QLineEdit(configuration)
        self.db_path.setEnabled(False)
        self.db_path.setText("")
        self.db_path.setObjectName("db_path")
        self.horizontalLayout_5.addWidget(self.db_path)
        self.btn_db_path = QtWidgets.QPushButton(configuration)
        self.btn_db_path.setEnabled(False)
        self.btn_db_path.setObjectName("btn_db_path")
        self.horizontalLayout_5.addWidget(self.btn_db_path)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(configuration)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.combo_measurement_unit = QtWidgets.QComboBox(configuration)
        self.combo_measurement_unit.setEnabled(False)
        self.combo_measurement_unit.setObjectName("combo_measurement_unit")
        self.combo_measurement_unit.addItem("")
        self.combo_measurement_unit.addItem("")
        self.horizontalLayout_8.addWidget(self.combo_measurement_unit)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(configuration)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.combo_number_decimals = QtWidgets.QComboBox(configuration)
        self.combo_number_decimals.setObjectName("combo_number_decimals")
        self.combo_number_decimals.addItem("")
        self.combo_number_decimals.addItem("")
        self.horizontalLayout_9.addWidget(self.combo_number_decimals)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(configuration)
        QtCore.QMetaObject.connectSlotsByName(configuration)

    def retranslateUi(self, configuration):
        _translate = QtCore.QCoreApplication.translate
        configuration.setWindowTitle(_translate("configuration", "Configure Settings"))
        self.label.setText(_translate("configuration", "Settings:"))
        self.label_2.setText(_translate("configuration", "Admin password:"))
        self.label_3.setText(_translate("configuration", "Bookmark List Directory:"))
        self.btn_bl_directory.setText(_translate("configuration", "Select"))
        self.label_4.setText(_translate("configuration", "Output Directory:"))
        self.btn_output_directory.setText(_translate("configuration", "Select"))
        self.label_5.setText(_translate("configuration", "Database Path:"))
        self.btn_db_path.setText(_translate("configuration", "Set"))
        self.label_6.setText(_translate("configuration", "Units:"))
        self.combo_measurement_unit.setItemText(0, _translate("configuration", "cm"))
        self.combo_measurement_unit.setItemText(1, _translate("configuration", "mm"))
        self.label_7.setText(_translate("configuration", "Rouding:"))
        self.combo_number_decimals.setItemText(0, _translate("configuration", "0.1"))
        self.combo_number_decimals.setItemText(1, _translate("configuration", "0.01"))

