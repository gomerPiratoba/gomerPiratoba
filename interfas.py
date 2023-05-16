import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ventana1 = uic.loadUi("SoyMuyPro.ui")

def realizar_operacion(operacion):
    try:
        a = float(ventana1.txtNum1.text())
        b = float(ventana1.txtNum2.text())
        resultado = operacion(a, b)
        ventana1.txtResultado.setText(str(resultado))
    except ValueError:
        ventana1.txtResultado.setText("Error: Entrada inválida")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potencia(a, b):
    return a ** b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        ventana1.txtResultado.setText("Error: División por cero")
        return None

def cerrar():
    ventana1.close()

def borrar():
    ventana1.txtNum1.setText("")
    ventana1.txtNum2.setText("")
    ventana1.txtResultado.setText("")

ventana1.botonSumar.clicked.connect(lambda: realizar_operacion(sumar))
ventana1.botonRestar.clicked.connect(lambda: realizar_operacion(restar))
ventana1.botonMul.clicked.connect(lambda: realizar_operacion(multiplicar))
ventana1.botonPotencia.clicked.connect(lambda: realizar_operacion(potencia))
ventana1.botonDividir.clicked.connect(lambda: realizar_operacion(dividir))
ventana1.botonBorrar.clicked.connect(borrar)
ventana1.botonCerrar.clicked.connect(cerrar)

ventana1.show()
app.exec_()

