from msilib.schema import RadioButton
import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
import os
from os import listdir, path, startfile, stat
from mimetypes import MimeTypes
import io
from datetime import date
from funciones_blindaje import *

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("mainWindow.ui", self)
        self.ventanaAnalisis = calcBlindaje()
        # self.ventanaInformacion = Informacion()
        self.btnInitEnsayo.clicked.connect(self.abrirAnalisis)
        self.btnCerrar.clicked.connect(self.Cerrar)
        # self.btnInfo.clicked.connect(self.abrirInfo)
        # self.btnPrevEnsayos.clicked.connect(self.EnsayosPrevios)

    def abrirAnalisis(self):
        self.close()
        self.ventanaAnalisis.exec_()

    def Cerrar(self):
        self.close()
    
    # def abrirInfo(self):
    #     self.close()
    #     self.ventanaInformacion.exec_()
    
    # def EnsayosPrevios(self):
    #     self.close()
    #     EnsayosAnteriores().exec_()

class calcBlindaje(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("calculoBlindaje.ui", self)
        # self.ventanaAnalisis = calcBlindaje()
        # # self.ventanaInformacion = Informacion()
        # self.btnInitEnsayo.clicked.connect(self.abrirAnalisis)
        # self.btnCerrar.clicked.connect(self.Cerrar)
        self.Resultados = Resultados()
        # self.Menu = Ventana()
        self.btn_init.clicked.connect(self.Calculo)
        self.btn_menupp.clicked.connect(self.Menu_principal)

    def Calculo(self):
        Kp1 = float(self.lineEdit_kp1.text())
        N = float(self.lineEdit_N.text())
        U = float(self.lineEdit_U.text())
        dp = float(self.lineEdit_d.text())
        P = float(self.lineEdit_P.text())
        T = float(self.lineEdit_T.text())

        try:
            if self.radioButton_suelo.isChecked():
                superficie = 0
            elif self.radioButton_techo.isChecked():
                superficie = 1
            elif self.radioButton_pared.isChecked():
                superficie = 2
            
            if self.radioButton_primario.isChecked():
                orden = 0
            elif self.radioButton_secundario.isChecked():
                orden = 2

            if self.radioButton_all.isChecked():
                sala = 0
            elif self.radioButton_chesty.isChecked():
                sala = 1
            elif self.radioButton_suelo.isChecked():
                sala = 2
            
            if self.radioButton_mesa.isChecked():
                atenuacion = 0
            elif self.radioButton_cross.isChecked():
                atenuacion = 1
            
            if self.radioButton_plomo.isChecked():
                material = 0
                strmaterial = 'plomo'
            elif self.radioButton_concreto.isChecked():
                material = 1
                strmaterial = 'concreto'

            espesor = calculoBilndaje(Kp1, N, U, dp, superficie, P, T, orden, sala, atenuacion, material)

            self.Resultados.label_resultados.setText(f'El espesor para el material de {strmaterial} es de {espesor: 4f} mm')
            self.Resultados.label_kp1.setText(f'Kp1: {Kp1}')
            self.Resultados.label_N.setText(f'N: {N}')
            self.Resultados.label_U.setText(f'U: {U}')
            self.Resultados.label_dp.setText(f'dp: {dp}')
            self.Resultados.label_P.setText(f'P: {P}')
            self.Resultados.label_T.setText(f'T: {T}')
            self.Resultados.label_material.setText(f'Material: {strmaterial}')
            self.Resultados.exec_()
        except:
            self.label_error.setText('A ocurrido un error')
    
    def Menu_principal(self):
        self.close()
        Ventana().exec_()

class Resultados(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("resultados.ui", self)
        # self.ventanaAnalisis = calcBlindaje()
        # # self.ventanaInformacion = Informacion()
        self.btn_close.clicked.connect(self.Cerrar)
    
    def Cerrar(self):
        self.close()

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()