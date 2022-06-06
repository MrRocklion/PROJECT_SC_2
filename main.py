# File: main.py
import sys
import serial
import time
import resources
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QButtonGroup
from PySide6.QtCore import QFile, QIODevice
ser = serial.Serial()
def serialInit():
    port = str(window.puerto.text()).upper()
    radio = group2.checkedButton()
    bau = 0
    if(port.strip() != '' and str(radio) != 'None'):
        if str(radio.objectName()) == 'bau1':
            bau = 9600
        if str(radio.objectName()) == 'bau2':
            bau = 19200
        if str(radio.objectName()) == 'bau3':
            bau = 115200
        try:
            ser.baudrate = bau
            ser.port = port
            ser.parity = serial.PARITY_EVEN
            ser.stopbits = serial.STOPBITS_TWO
            ser.bytesize = serial.EIGHTBITS

            ser.open()
            print("se conecto")
        except PermissionError:
            print("algo ocurrio mal")
    else:
        print('empty')
def desconectar():
    ser.close()
    print("se desconecto")
def enviarComando():
    cmd = window.lineComand.text()
    string = '{}\r\n'.format(cmd)
    print(cmd)
    ser.write(string.encode())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "mainWindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.op1.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page1))
    window.op2.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page2))
    window.op3.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page3))
    window.op4.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page4))
    group1 = QButtonGroup()
    group2 = QButtonGroup()
    group1.addButton(window.stop1)
    group1.addButton(window.stop2)
    group1.addButton(window.stop3)
    group2.addButton(window.bau1)
    group2.addButton(window.bau2)
    group2.addButton(window.bau3)
    window.btnConnect.clicked.connect(lambda: serialInit())
    window.btnDisconnect.clicked.connect(lambda: desconectar())
    window.sendBtn.clicked.connect(lambda: enviarComando())
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())