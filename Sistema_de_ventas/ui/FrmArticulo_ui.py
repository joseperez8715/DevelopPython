# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\josep\Documents\DevelopPython\Sistema_de_ventas\ui\FrmArticulo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1019, 658)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #deede3;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label.setObjectName("label")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 30, 981, 581))
        self.tabs.setStyleSheet("QLineEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.tabs.setObjectName("tabs")
        self.tabListado = QtWidgets.QWidget()
        self.tabListado.setObjectName("tabListado")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabListado)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 931, 521))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 2px solid #1e362d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    color: #1e362d;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: none;\n"
"}\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(15, 20, 73, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.txtBuscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtBuscar.setGeometry(QtCore.QRect(100, 20, 120, 35))
        self.txtBuscar.setStyleSheet("QLineEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.txtBuscar.setObjectName("txtBuscar")
        self.btnBuscar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBuscar.setGeometry(QtCore.QRect(240, 20, 85, 37))
        self.btnBuscar.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnImprimir = QtWidgets.QPushButton(self.groupBox_2)
        self.btnImprimir.setGeometry(QtCore.QRect(340, 20, 85, 37))
        self.btnImprimir.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnImprimir.setObjectName("btnImprimir")
        self.tbDatos = QtWidgets.QTableView(self.groupBox_2)
        self.tbDatos.setGeometry(QtCore.QRect(15, 70, 891, 421))
        self.tbDatos.setStyleSheet("QTableView {\n"
"    background-color: #f2f7f4;\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #96bfaa;\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QTableView QHeaderView {\n"
"    background-color: #c0dacb;\n"
"    color: #333333;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableView QHeaderView::section {\n"
"    background-color: #deede3;\n"
"    color: #333333;\n"
"    padding: 6px;\n"
"    border: 1px solid #1e362d;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:checked {\n"
"    background-color: #96bfaa;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #96bfaa;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item:focus {\n"
"    background-color: #96bfaa;\n"
"    color: #ffffff;\n"
"    outline: none;\n"
"}")
        self.tbDatos.setObjectName("tbDatos")
        self.tabs.addTab(self.tabListado, "")
        self.tabUsuario = QtWidgets.QWidget()
        self.tabUsuario.setObjectName("tabUsuario")
        self.tabs.addTab(self.tabUsuario, "")
        self.tabEquipo = QtWidgets.QWidget()
        self.tabEquipo.setObjectName("tabEquipo")
        self.tabs.addTab(self.tabEquipo, "")
        self.tabImagenEquipo = QtWidgets.QWidget()
        self.tabImagenEquipo.setObjectName("tabImagenEquipo")
        self.tabs.addTab(self.tabImagenEquipo, "")
        self.tabContrato = QtWidgets.QWidget()
        self.tabContrato.setObjectName("tabContrato")
        self.groupBox = QtWidgets.QGroupBox(self.tabContrato)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 721, 351))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid #1e362d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    color: #1e362d;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border: none;\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_3.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 63, 21))
        self.label_4.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 101, 21))
        self.label_5.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.btnEditar = QtWidgets.QPushButton(self.groupBox)
        self.btnEditar.setGeometry(QtCore.QRect(220, 290, 85, 37))
        self.btnEditar.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnEditar.setObjectName("btnEditar")
        self.btnGuardar = QtWidgets.QPushButton(self.groupBox)
        self.btnGuardar.setGeometry(QtCore.QRect(120, 290, 85, 37))
        self.btnGuardar.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnGuardar.setObjectName("btnGuardar")
        self.txtCodigo = QtWidgets.QLineEdit(self.groupBox)
        self.txtCodigo.setGeometry(QtCore.QRect(120, 30, 120, 35))
        self.txtCodigo.setStyleSheet("QLineEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.txtCodigo.setReadOnly(True)
        self.txtCodigo.setObjectName("txtCodigo")
        self.txtNombre = QtWidgets.QLineEdit(self.groupBox)
        self.txtNombre.setGeometry(QtCore.QRect(120, 150, 221, 35))
        self.txtNombre.setStyleSheet("QLineEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.txtNombre.setObjectName("txtNombre")
        self.txtDescripcion = QtWidgets.QTextEdit(self.groupBox)
        self.txtDescripcion.setGeometry(QtCore.QRect(120, 210, 221, 51))
        self.txtDescripcion.setStyleSheet("QTextEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}")
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.txtCodArt = QtWidgets.QLineEdit(self.groupBox)
        self.txtCodArt.setGeometry(QtCore.QRect(120, 90, 120, 35))
        self.txtCodArt.setStyleSheet("QLineEdit {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.txtCodArt.setReadOnly(True)
        self.txtCodArt.setObjectName("txtCodArt")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 101, 21))
        self.label_6.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.gFoto = QtWidgets.QGraphicsView(self.groupBox)
        self.gFoto.setGeometry(QtCore.QRect(365, 150, 211, 181))
        self.gFoto.setStyleSheet("QGraphicsView {\n"
"    background-color: #f2f7f4;\n"
"    border: 1px solid #cccccc;\n"
"}")
        self.gFoto.setObjectName("gFoto")
        self.btnCargar = QtWidgets.QPushButton(self.groupBox)
        self.btnCargar.setGeometry(QtCore.QRect(600, 150, 85, 31))
        self.btnCargar.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnCargar.setObjectName("btnCargar")
        self.btnLimpiar = QtWidgets.QPushButton(self.groupBox)
        self.btnLimpiar.setGeometry(QtCore.QRect(600, 190, 85, 31))
        self.btnLimpiar.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #c0dacb, stop: 1 #96bfab);\n"
"    color: #ffffff;\n"
"    border: 1px solid #1e362d;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #689f84, stop: 1 #96bfaa);\n"
"    border: 1px solid #96bfaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #2a5242, stop: 1 #32624d);\n"
"    border: 1px solid #32624d;\n"
"}")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.cmbPresentacion = QtWidgets.QComboBox(self.groupBox)
        self.cmbPresentacion.setGeometry(QtCore.QRect(410, 90, 100, 25))
        self.cmbPresentacion.setStyleSheet("/* Estilos para QComboBox */\n"
"QComboBox {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.cmbPresentacion.setObjectName("cmbPresentacion")
        self.cmbCategoria = QtWidgets.QComboBox(self.groupBox)
        self.cmbCategoria.setGeometry(QtCore.QRect(410, 30, 100, 25))
        self.cmbCategoria.setStyleSheet("/* Estilos para QComboBox */\n"
"QComboBox {\n"
"    background-color: #96bfab;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #689f84;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #689f84;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::placeholder {\n"
"    color: #1e362d;\n"
"    font-weight: bold;\n"
"}")
        self.cmbCategoria.setObjectName("cmbCategoria")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(310, 30, 81, 21))
        self.label_7.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(290, 90, 111, 21))
        self.label_9.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_Categoria = QtWidgets.QLabel(self.groupBox)
        self.label_Categoria.setGeometry(QtCore.QRect(520, 30, 191, 21))
        self.label_Categoria.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_Categoria.setObjectName("label_Categoria")
        self.label_Presentacion = QtWidgets.QLabel(self.groupBox)
        self.label_Presentacion.setGeometry(QtCore.QRect(520, 90, 191, 21))
        self.label_Presentacion.setStyleSheet("QWidget {\n"
"    background-color: var(--jade-50);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: var(--jade-500);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_Presentacion.setObjectName("label_Presentacion")
        self.tabs.addTab(self.tabContrato, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contartos"))
        self.tabs.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.txtBuscar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inserte el nombre del articulo</p></body></html>"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.btnImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabListado), _translate("MainWindow", "Listado"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabUsuario), _translate("MainWindow", "Datos de usuario"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabEquipo), _translate("MainWindow", "Datos del equipo"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabImagenEquipo), _translate("MainWindow", "Imagenes"))
        self.label_3.setText(_translate("MainWindow", "Codigo"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Descripcion"))
        self.btnEditar.setText(_translate("MainWindow", "Editar"))
        self.btnGuardar.setText(_translate("MainWindow", " Guardar "))
        self.txtCodigo.setToolTip(_translate("MainWindow", "Insertar codigo de articulo"))
        self.label_6.setText(_translate("MainWindow", "Codigo Barr."))
        self.gFoto.setToolTip(_translate("MainWindow", "Imagen de articulo"))
        self.btnCargar.setText(_translate("MainWindow", "Cargar"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.label_7.setText(_translate("MainWindow", "Categoria"))
        self.label_9.setText(_translate("MainWindow", "Presentacion"))
        self.label_Categoria.setText(_translate("MainWindow", "Herramientas manuales"))
        self.label_Presentacion.setText(_translate("MainWindow", "Unidad"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabContrato), _translate("MainWindow", "Contrato"))
