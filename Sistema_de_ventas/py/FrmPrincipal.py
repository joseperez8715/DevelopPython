import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QMessageBox, QGraphicsDropShadowEffect
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from FrmEmpleado import VentanaEmpleado
from FrmCategoria import VentanaCategoria
from FrmArticulo import VentanaArticulo
from FrmPresentacion import VentanaPresentacion
from FrmProveedor import VentanaProveedor
from FrmCliente import VentanaCliente
from FrmIngreso import VentanaIngresoAlmacen
from FrmVentas import VentanaVentas
from FrmCotizaciones import VentanaCotizaciones
from FrmStock import VentanaStock
from Consultas_db import backup_database

class VentanaPrincipal(QMainWindow):      
    def __init__(self,):
        super().__init__()        
        uic.loadUi('Sistema_de_ventas/ui/FrmPrincipal.ui',self)
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------        
        
        
                
        # Configuraiones de la ventana principal.
        self.setWindowTitle('.:. Sistema_de_ventas .:.')
        #self.setFixedSize(self.size())
        self.setWindowIcon(QtGui.QIcon('Sistema_de_ventas/imagenes/login.jpg'))
        
    # Obtiene nombre s=de usuario y rol del inicio de sesion y los mustra en los label
    # del formulario principal para identificar el usuario que esta trabajando.
    def etiqueta_usuario(self, rol, usuario):
        self.lblUsuario.setText(rol + ":")
        self.lblEmpleado.setText(usuario)
        

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------        
        
    def administrador(self):
            self.actionSalir.triggered.connect(self.fn_Salir)
            self.actionEmpleados.triggered.connect(self.abrirFrmEmpleados)
            self.actionCategorias.triggered.connect(self.abrirFrmCategoria)
            self.actionArticulos.triggered.connect(self.abrirFrmArticulo)
            self.actionPresentaciones.triggered.connect(self.abrirFrmPresentacion)
            self.actionProveedores.triggered.connect(self.abrirFrmProveedor)
            self.actionClientes.triggered.connect(self.abrirFrmClientes)
            self.actionIngresos.triggered.connect(self.abrirFrmIngresos)
            self.actionVentas.triggered.connect(self.abrirFrmVentas)
            self.actionCambiar_de_usuario.triggered.connect(self.cerrar_sesion)
            self.actionCotizacion.triggered.connect(self.abrirFrmCotizaciones)
            self.actionStock_de_articulos.triggered.connect(self.abrirFrmStock)
            
            #self.actionBack_up.triggered.connect(self.database_backup)       
            
            
    def vendedor(self):
            self.actionSalir.triggered.connect(self.fn_Salir)
            self.actionEmpleados.setEnabled(False)
            self.actionCategorias.setEnabled(False)
            self.actionArticulos.setEnabled(False)
            self.actionPresentaciones.setEnabled(False)
            self.actionProveedores.setEnabled(False)
            self.actionClientes.triggered.connect(self.abrirFrmClientes)
            self.actionVentas.triggered.connect(self.abrirFrmVentas)
            self.actionIngresos.setEnabled(False)
            self.actionCambiar_de_usuario.triggered.connect(self.cerrar_sesion)
            self.actionCotizacion.triggered.connect(self.abrirFrmCotizaciones)
            self.actionStock_de_articulos.triggered.connect(self.abrirFrmStock)
            #self.nemuHerramientas
                    
            
            
    def almacen(self):
            self.actionSalir.triggered.connect(self.fn_Salir)
            self.actionEmpleados.setEnabled(False)
            self.actionCategorias.triggered.connect(self.abrirFrmCategoria)
            self.actionArticulos.triggered.connect(self.abrirFrmArticulo)
            self.actionPresentaciones.triggered.connect(self.abrirFrmPresentacion)
            self.actionProveedores.triggered.connect(self.abrirFrmProveedor)
            self.actionClientes.setEnabled(False)
            self.actionVentas.setEnabled(False)
            self.actionCotizacion.setEnabled(False)
            self.actionIngresos.triggered.connect(self.abrirFrmIngresos)
            self.actionCambiar_de_usuario.triggered.connect(self.cerrar_sesion)
            self.actionStock_de_articulos.triggered.connect(self.abrirFrmStock)
            #self.menuConsultas
            #self.nemuHerramientas
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    def database_backup(self):
        backup_database()
        

    def abrirFrmStock(self):
        
        if not VentanaStock.ventana_abierta:           
            frmCotizaciones = VentanaStock()
            VentanaStock.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmCotizaciones)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
            
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()

    def abrirFrmCotizaciones(self):
        
        if not VentanaCotizaciones.ventana_abierta:           
            frmCotizaciones = VentanaCotizaciones()
            VentanaCotizaciones.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmCotizaciones)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
            
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()


    def abrirFrmEmpleados(self):
        
        if not VentanaEmpleado.ventana_abierta:           
            frmEmpleado = VentanaEmpleado()
            VentanaEmpleado.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmEmpleado)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
            
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
            
            
            
    def abrirFrmCategoria(self):
        
        if not VentanaCategoria.ventana_abierta:
            frmCategoria = VentanaCategoria()
            VentanaCategoria.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmCategoria)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
        
    def abrirFrmPresentacion(self):
        
        if not VentanaPresentacion.ventana_abierta:
            frmPresentacion = VentanaPresentacion()
            VentanaPresentacion.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmPresentacion)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
            
    def abrirFrmIngresos(self):
        
        if not VentanaIngresoAlmacen.ventana_abierta:
            frmIngreso = VentanaIngresoAlmacen()
            VentanaIngresoAlmacen.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmIngreso)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
                
    def abrirFrmArticulo(self):
        
        if not VentanaArticulo.ventana_abierta:
            frmArticulo = VentanaArticulo()
            VentanaArticulo.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmArticulo)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
        
    def abrirFrmProveedor(self):
        
        if not VentanaProveedor.ventana_abierta:
            frmProveedor = VentanaProveedor()
            VentanaProveedor.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmProveedor)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
    
    def abrirFrmVentas(self):
        
        if not VentanaVentas.ventana_abierta:
            frmVentas = VentanaVentas()
            VentanaVentas.ventana_abierta = True
            subWindow = QMdiSubWindow()
            subWindow.setWidget(frmVentas)
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)
            subWindow.show()
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
        
        
    def abrirFrmClientes(self):
        
        if not VentanaCliente.ventana_abierta:
            frmCliente = VentanaCliente()  # Crea una instancia de VentanaCliente
            VentanaCliente.ventana_abierta = True
            subWindow = QMdiSubWindow()  # Crea una ventana secundaria para VentanaCliente
            subWindow.setWidget(frmCliente)  # Establece VentanaCliente como contenido de la ventana secundaria
            subWindow.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore # Configura para que la ventana secundaria se elimine al cerrarse
            subWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint) # type: ignore
            self.mdiArea.addSubWindow(subWindow)  # Agrega la ventana secundaria al mdiArea
            subWindow.show()  # Muestra la ventana secundaria
        else:
            #mensaje al usuario
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setWindowTitle("Ventana duplicada")
            mensaje.setText("La ventana ya esta abierta.")
            mensaje.exec_()
            
    def cerrar_sesion(self):
        # Cierra la sesión del usuario actual
        from FrmLogin import VentanaLogin
        self.ventana_login = VentanaLogin()
        self.ventana_login.show()
        self.close()
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    def fn_Salir(self):
        self.close()
        
    def showEvent(self, event):
        super().showEvent(event)
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)       
    GUI = VentanaPrincipal()
    GUI.showMaximized()
    sys.exit(app.exec_())