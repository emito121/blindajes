# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculoBlindaje.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 581)
        Dialog.setStyleSheet("QDialog{background-color:rgb(255, 255, 0);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(620, 300, 411, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/kisspng-biological-hazard-clip-art-sticker-symbol-decal-clone-of-syria-map-umap-5d09b2efa22570.5321987615609167196642 (1).png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_superficie = QtWidgets.QGroupBox(Dialog)
        self.groupBox_superficie.setGeometry(QtCore.QRect(50, 170, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_superficie.setFont(font)
        self.groupBox_superficie.setCheckable(False)
        self.groupBox_superficie.setObjectName("groupBox_superficie")
        self.radioButton_suelo = QtWidgets.QRadioButton(self.groupBox_superficie)
        self.radioButton_suelo.setGeometry(QtCore.QRect(20, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_suelo.setFont(font)
        self.radioButton_suelo.setChecked(True)
        self.radioButton_suelo.setObjectName("radioButton_suelo")
        self.radioButton_pared = QtWidgets.QRadioButton(self.groupBox_superficie)
        self.radioButton_pared.setGeometry(QtCore.QRect(20, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_pared.setFont(font)
        self.radioButton_pared.setObjectName("radioButton_pared")
        self.radioButton_techo = QtWidgets.QRadioButton(self.groupBox_superficie)
        self.radioButton_techo.setGeometry(QtCore.QRect(20, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_techo.setFont(font)
        self.radioButton_techo.setObjectName("radioButton_techo")
        self.groupBox_orden = QtWidgets.QGroupBox(Dialog)
        self.groupBox_orden.setGeometry(QtCore.QRect(50, 290, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_orden.setFont(font)
        self.groupBox_orden.setObjectName("groupBox_orden")
        self.radioButton_secundario = QtWidgets.QRadioButton(self.groupBox_orden)
        self.radioButton_secundario.setGeometry(QtCore.QRect(20, 60, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_secundario.setFont(font)
        self.radioButton_secundario.setObjectName("radioButton_secundario")
        self.radioButton_primario = QtWidgets.QRadioButton(self.groupBox_orden)
        self.radioButton_primario.setGeometry(QtCore.QRect(20, 30, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_primario.setFont(font)
        self.radioButton_primario.setChecked(True)
        self.radioButton_primario.setObjectName("radioButton_primario")
        self.groupBox_atenuacion = QtWidgets.QGroupBox(Dialog)
        self.groupBox_atenuacion.setGeometry(QtCore.QRect(400, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_atenuacion.setFont(font)
        self.groupBox_atenuacion.setObjectName("groupBox_atenuacion")
        self.radioButton_mesa = QtWidgets.QRadioButton(self.groupBox_atenuacion)
        self.radioButton_mesa.setGeometry(QtCore.QRect(30, 30, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_mesa.setFont(font)
        self.radioButton_mesa.setChecked(True)
        self.radioButton_mesa.setObjectName("radioButton_mesa")
        self.radioButton_cross = QtWidgets.QRadioButton(self.groupBox_atenuacion)
        self.radioButton_cross.setGeometry(QtCore.QRect(30, 60, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_cross.setFont(font)
        self.radioButton_cross.setObjectName("radioButton_cross")
        self.groupBox_material = QtWidgets.QGroupBox(Dialog)
        self.groupBox_material.setGeometry(QtCore.QRect(400, 400, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_material.setFont(font)
        self.groupBox_material.setObjectName("groupBox_material")
        self.radioButton_concreto = QtWidgets.QRadioButton(self.groupBox_material)
        self.radioButton_concreto.setGeometry(QtCore.QRect(30, 60, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_concreto.setFont(font)
        self.radioButton_concreto.setObjectName("radioButton_concreto")
        self.radioButton_plomo = QtWidgets.QRadioButton(self.groupBox_material)
        self.radioButton_plomo.setGeometry(QtCore.QRect(30, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_plomo.setFont(font)
        self.radioButton_plomo.setChecked(True)
        self.radioButton_plomo.setObjectName("radioButton_plomo")
        self.btn_init = QtWidgets.QPushButton(Dialog)
        self.btn_init.setGeometry(QtCore.QRect(20, 520, 589, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_init.setFont(font)
        self.btn_init.setStyleSheet("QPushButton{background-color:rgb(85, 255, 0);}\n"
"\n"
"QPushButton:hover{background-color:orange;}")
        self.btn_init.setObjectName("btn_init")
        self.btn_menupp = QtWidgets.QPushButton(Dialog)
        self.btn_menupp.setGeometry(QtCore.QRect(20, 550, 589, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_menupp.setFont(font)
        self.btn_menupp.setStyleSheet("QPushButton{background-color:rgb(85, 255, 0);}\n"
"\n"
"QPushButton:hover{background-color:orange;}")
        self.btn_menupp.setObjectName("btn_menupp")
        self.groupBox_atenuacion_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_atenuacion_2.setGeometry(QtCore.QRect(50, 380, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_atenuacion_2.setFont(font)
        self.groupBox_atenuacion_2.setObjectName("groupBox_atenuacion_2")
        self.radioButton_chesty = QtWidgets.QRadioButton(self.groupBox_atenuacion_2)
        self.radioButton_chesty.setGeometry(QtCore.QRect(20, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_chesty.setFont(font)
        self.radioButton_chesty.setObjectName("radioButton_chesty")
        self.radioButton_all = QtWidgets.QRadioButton(self.groupBox_atenuacion_2)
        self.radioButton_all.setGeometry(QtCore.QRect(20, 30, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_all.setFont(font)
        self.radioButton_all.setChecked(True)
        self.radioButton_all.setObjectName("radioButton_all")
        self.radioButton_piso = QtWidgets.QRadioButton(self.groupBox_atenuacion_2)
        self.radioButton_piso.setGeometry(QtCore.QRect(20, 90, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_piso.setFont(font)
        self.radioButton_piso.setObjectName("radioButton_piso")
        self.label_error = QtWidgets.QLabel(Dialog)
        self.label_error.setGeometry(QtCore.QRect(20, 500, 591, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("QLabel{color:red;}")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 50, 451, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_T = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_T.setFont(font)
        self.lineEdit_T.setObjectName("lineEdit_T")
        self.gridLayout.addWidget(self.lineEdit_T, 3, 1, 1, 1)
        self.lineEdit_N = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_N.setFont(font)
        self.lineEdit_N.setObjectName("lineEdit_N")
        self.gridLayout.addWidget(self.lineEdit_N, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_d = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_d.setFont(font)
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.gridLayout.addWidget(self.lineEdit_d, 1, 1, 1, 1)
        self.lineEdit_P = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_P.setFont(font)
        self.lineEdit_P.setObjectName("lineEdit_P")
        self.gridLayout.addWidget(self.lineEdit_P, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_kp1 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_kp1.setFont(font)
        self.lineEdit_kp1.setText("")
        self.lineEdit_kp1.setObjectName("lineEdit_kp1")
        self.gridLayout_2.addWidget(self.lineEdit_kp1, 0, 1, 1, 1)
        self.lineEdit_U = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_U.setFont(font)
        self.lineEdit_U.setObjectName("lineEdit_U")
        self.gridLayout_2.addWidget(self.lineEdit_U, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.groupBox_atenuacion.raise_()
        self.label.raise_()
        self.groupBox_superficie.raise_()
        self.groupBox_orden.raise_()
        self.groupBox_material.raise_()
        self.label_2.raise_()
        self.btn_init.raise_()
        self.btn_menupp.raise_()
        self.groupBox_atenuacion_2.raise_()
        self.label_error.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Calculadora de blindaje para rayos X"))
        self.groupBox_superficie.setTitle(_translate("Dialog", "Superficie"))
        self.radioButton_suelo.setText(_translate("Dialog", "Suelo"))
        self.radioButton_pared.setText(_translate("Dialog", "Pared"))
        self.radioButton_techo.setText(_translate("Dialog", "Techo"))
        self.groupBox_orden.setTitle(_translate("Dialog", "Orden"))
        self.radioButton_secundario.setText(_translate("Dialog", "Secundario"))
        self.radioButton_primario.setText(_translate("Dialog", "Primario"))
        self.groupBox_atenuacion.setTitle(_translate("Dialog", "Atenuación"))
        self.radioButton_mesa.setText(_translate("Dialog", "Mesa"))
        self.radioButton_cross.setText(_translate("Dialog", "Cross  table"))
        self.groupBox_material.setTitle(_translate("Dialog", "Material"))
        self.radioButton_concreto.setText(_translate("Dialog", "Concreto"))
        self.radioButton_plomo.setText(_translate("Dialog", "Plomo"))
        self.btn_init.setText(_translate("Dialog", "Iniciar Cálculo"))
        self.btn_menupp.setText(_translate("Dialog", "Regresar al Menú Principal"))
        self.groupBox_atenuacion_2.setTitle(_translate("Dialog", "Tipo de Estudio"))
        self.radioButton_chesty.setText(_translate("Dialog", "Chesty bucky"))
        self.radioButton_all.setText(_translate("Dialog", "All barriers"))
        self.radioButton_piso.setText(_translate("Dialog", "Piso"))
        self.label_6.setText(_translate("Dialog", "Distancia al punto de interés:"))
        self.label_8.setText(_translate("Dialog", "Kerma limitante permitido (P):"))
        self.label_4.setText(_translate("Dialog", "Promedio de pacientes por semana (N):"))
        self.label_9.setText(_translate("Dialog", "Factor de ocupación (T):"))
        self.label_3.setText(_translate("Dialog", "Kerma en aire a un metro (Kp1):"))
        self.label_5.setText(_translate("Dialog", "Factor de uso (U):"))
