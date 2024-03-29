# File: main.py
import sys
import serial
import time
import resources
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QButtonGroup
from PySide6.QtCore import QFile, QIODevice , Qt
from CustomWidgetsPyhton.CustomSwitch import CSwitch

ser = serial.Serial()
global juntas
global juntas2
global des
global des2
global vel

juntas = [0, 0, 0, 0, 0, 0]
juntas2 =  [0, 0, 0, 0, 0, 0]
vel = 0
des = 1
des2 = 1
def holaMundo(val):
    print(f'hola {val}')

def serialInit():
    port = str(window.puerto.text()).upper()
    bau = group_baud.checkedButton()
    stop = group_stop.checkedButton()
    parity = group_parity.checkedButton()
    if (port.strip() != '' and str(bau) != 'None'):
        window.com_ser.setText(str(port))
        if str(bau.objectName()) == 'bau1':
            bau = 9600
            window.bau_ser.setText(str(9600))
        elif str(bau.objectName()) == 'bau2':
            bau = 19200
            window.bau_ser.setText(str(19200))
        elif str(bau.objectName()) == 'bau3':
            bau = 115200
            window.bau_ser.setText(str(115200))
        if str(stop.objectName()) == 'stop1':
            stop = serial.STOPBITS_ONE
            window.stop_ser.setText(str('STOPBITS_ONE'))
        elif str(stop.objectName()) == 'stop2':
            stop = serial.STOPBITS_TWO
            window.stop_ser.setText(str('STOPBITS_TWO'))
        if str(parity.objectName()) == 'par1':
            parity = serial.PARITY_NONE
            window.parity_ser.setText(str("NONE"))
        elif str(parity.objectName()) == 'par2':
            parity = serial.PARITY_EVEN
            window.parity_ser.setText(str("EVEN"))
        try:
            ser.baudrate = bau
            ser.port = port
            ser.parity = parity
            ser.stopbits = stop
            ser.bytesize = serial.EIGHTBITS
            ser.timeout = 1
            ser.open()
            print("se conecto")
        except PermissionError:
            print("algo ocurrio mal")
    else:
        print('empty')


def desconectar():
    ser.close()
    print("se desconecto")

def set_gripper(estado):
    if estado:
        ser.write(b'1;1;EXECHOPEN 1\r\n')
        line = ser.readline()
        print(line)
    else:
        ser.write(b'1;1;EXECHCLOSE 1\r\n')
        line = ser.readline()
        print(line)

def seleccionar_velocidad_modo1(velocidad):
    window.vel_value.setText(str(velocidad))
    string = '1;1;EXECJOVRD {}\r\n'.format(velocidad)
    ser.write(string.encode())
    print(velocidad)
    line = ser.readline()
    print(line)

def seleccionar_velocidad_modo2(velocidad):
    window.velocidad2.setText(str(velocidad))
    string = '1;1;EXECSPD {}\r\n'.format(velocidad)
    ser.write(string.encode())
    print(velocidad)
    line = ser.readline()
    print(line)



def enviarComando():
    cmd = window.lineComand.text()
    string = '{}\r\n'.format(cmd)
    print(cmd)
    ser.write(string.encode())
    line = ser.readline()
    print(line)


def selec_velocidad(velocidad):
    window.vel_value.setText(str(velocidad))
    print(velocidad)

def selec_desplazmiento2(desplazamiento):
    global  des2
    window.des_modo2.setText(str(desplazamiento))
    des2 = int(desplazamiento)
    print(desplazamiento)

def selec_desplazmiento(desplazamiento):
    global  des
    window.des_value.setText(str(desplazamiento))
    des = int(desplazamiento)
    print(desplazamiento)
def set_velocidad(velocidad):
    global vel
    vel = velocidad
def  funcion_1():
    ser.write(b'1;1;CNTLON\r\n')
    line = ser.readline()
    print(line)
def  funcion_2():
    ser.write(b'1;1;SRVON\r\n')
    line = ser.readline()
    print(line)
def  funcion_3():
    ser.write(b'1;1;SRVOFF\r\n')
    line = ser.readline()
    print(line)
def  funcion_4():
    ser.write(b'1;1;RSTALRM\r\n')
    line = ser.readline()
    print(line)
def home_modo1():
    global juntas
    ser.write(b'1;1;EXECJCOSIROP=(4,11.07,79.9,0,18.02,0)\r\n')
    time.sleep(1)
    ser.write(b'1;1;EXECMOV JCOSIROP\r\n')
    juntas = [4,11.07,79.9,0,18.02,0]
    line = ser.readline()
    print(line)
    window.stackedWidget.setCurrentWidget(window.page2)
def home_modo2():
    global juntas2
    ser.write(b'1;1;EXECPCOSIROP=(365,25.5,488.25,-1.3,109,6,0)\r\n')
    time.sleep(1)
    ser.write(b'1;1;EXECMVS PCOSIROP\r\n')
    juntas2 = [365,25.5,488.25,-1.3,109,6,0]
    line = ser.readline()
    print(line)
    window.stackedWidget.setCurrentWidget(window.page3)
def  funcion_5():
    global juntas
    ser.write(b'1;1;EXECJCOSIROP=(0.0,0.0,0.0,0.0,0.0,0.0)\r\n')
    time.sleep(1)
    ser.write(b'1;1;EXECMOV JCOSIROP\r\n')
    juntas = [0, 0, 0, 0, 0, 0]
    line = ser.readline()
    print(line)
def  funcion_6():
    ser.write(b'1;1;STOP\r\n')
    line = ser.readline()
    print(line)
def moverJoints_modo2(joint,i):
    global juntas2
    global des2
    if joint == "a":
        if juntas2[i] < 600:
            juntas2[i] = juntas2[i] + des2
        else:
            juntas2[i] = 600
    elif joint == "b":
        if juntas2[i] > -600:
            juntas2[i] = juntas2[i] - des2
        else:
            juntas2[i] = -600
    mensaje = "1;1;EXECPCOSIROP=({},{},{},{},{},6,0)".format(juntas2[0], juntas2[1], juntas2[2], juntas2[3], juntas2[4])
    string = '{}\r\n'.format(mensaje)
    print(string)
    ser.write(string.encode())
    window.posicion_modo2.setText(str(juntas2))
    time.sleep(1)
    ser.write(b'1;1;EXECMVS PCOSIROP\r\n')
    # 1;1;EXECJCOSIROP=(50.00,50.00,30.00,0.00,50.00,10.00)

def moverJoints(joint, i):
    global juntas
    global des
    if joint == "a":
        if juntas[i] < 200:
            juntas[i] = juntas[i] + des
        else:
            juntas[i] = 200
    elif joint == "b":
        if juntas[i] > -200:
            juntas[i] = juntas[i] - des
        else:
            juntas[i] = -200
    mensaje = "1;1;EXECJCOSIROP=({},{},{},{},{},{})".format(juntas[0], juntas[1], juntas[2], juntas[3], juntas[4],
                                                            juntas[5])
    string = '{}\r\n'.format(mensaje)
    print(string)
    ser.write(string.encode())
    window.posicion_modo1.setText(str(juntas))
    time.sleep(1)
    ser.write(b'1;1;EXECMOV JCOSIROP\r\n')
    # 1;1;EXECJCOSIROP=(50.00,50.00,30.00,0.00,50.00,10.00)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "mainWindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    gripper1 = CSwitch(active_color="#17A589")
    gripper2 = CSwitch(active_color="#17A589")
    #monu lateral
    window.gripper_container.addWidget(gripper1,0,Qt.AlignCenter)
    window.gripContainer.addWidget(gripper2,0,Qt.AlignLeft)
    window.op1.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.page1))
    window.op2.clicked.connect(lambda:home_modo1())
    window.op3.clicked.connect(lambda: home_modo2())
    window.op4.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.page4))
    #modo1
    window.btnJoint1pos.clicked.connect(lambda: moverJoints("a", 0))
    window.btnJoint1neg.clicked.connect(lambda: moverJoints("b", 0))
    window.btnJoint2pos.clicked.connect(lambda: moverJoints("a", 1))
    window.btnJoint2neg.clicked.connect(lambda: moverJoints("b", 1))
    window.btnJoint3pos.clicked.connect(lambda: moverJoints("a", 2))
    window.btnJoint3neg.clicked.connect(lambda: moverJoints("b", 2))
    window.btnJoint5pos.clicked.connect(lambda: moverJoints("a", 4))
    window.btnJoint5neg.clicked.connect(lambda: moverJoints("b", 4))
    window.btnJoint6pos.clicked.connect(lambda: moverJoints("a", 5))
    window.btnJoint6neg.clicked.connect(lambda: moverJoints("b", 5))
    window.velSlider.sliderReleased.connect(lambda : seleccionar_velocidad_modo1(window.velSlider.value()))
    window.reset1.clicked.connect(lambda: funcion_4())
    window.emergencia1.clicked.connect(lambda: funcion_6())
    #modo 2

    window.posx.clicked.connect(lambda: moverJoints_modo2('a',0))
    window.negx.clicked.connect(lambda: moverJoints_modo2('b',0))
    window.posy.clicked.connect(lambda: moverJoints_modo2('a',1))
    window.negy.clicked.connect(lambda: moverJoints_modo2('b',1))
    window.posz.clicked.connect(lambda: moverJoints_modo2('a',2))
    window.negz.clicked.connect(lambda: moverJoints_modo2('b',2))
    window.posa.clicked.connect(lambda: moverJoints_modo2('a',3))
    window.nega.clicked.connect(lambda: moverJoints_modo2('b',3))
    window.posb.clicked.connect(lambda: moverJoints_modo2('a',4))
    window.negb.clicked.connect(lambda: moverJoints_modo2('b',4))
    window.reset2.clicked.connect(lambda: funcion_4())
    window.emergencia2.clicked.connect(lambda: funcion_6())

    #modo 3
    window.fun1.clicked.connect(lambda: funcion_1())
    window.fun2.clicked.connect(lambda: funcion_2())
    window.fun3.clicked.connect(lambda: funcion_3())
    window.fun4.clicked.connect(lambda: funcion_4())
    window.fun5.clicked.connect(lambda: funcion_5())
    window.fun6.clicked.connect(lambda: funcion_6())
    window.desplazamiento_modo2.sliderReleased.connect(lambda : selec_desplazmiento2(window.desplazamiento_modo2.value()))
    window.velocidad_modo2.sliderReleased.connect(lambda : seleccionar_velocidad_modo2(window.velocidad_modo2.value()))

    gripper1.clicked.connect(lambda: set_gripper(gripper1.isChecked()))
    gripper2.clicked.connect(lambda: set_gripper(gripper2.isChecked()))
    group_baud = QButtonGroup()
    group_baud.addButton(window.bau1)
    group_baud.addButton(window.bau2)
    group_baud.addButton(window.bau3)
    group_stop = QButtonGroup()
    group_stop.addButton(window.stop1)
    group_stop.addButton(window.stop2)
    group_parity = QButtonGroup()
    group_parity.addButton(window.par1)
    group_parity.addButton(window.par2)

    window.btnConnect.clicked.connect(lambda: serialInit())
    window.btnDisconnect.clicked.connect(lambda: desconectar())
    window.sendBtn.clicked.connect(lambda: enviarComando())
    window.velSlider.sliderReleased.connect(lambda: selec_velocidad(window.velSlider.value()))
    window.despSlider.sliderReleased.connect(lambda: selec_desplazmiento(window.despSlider.value()))
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())
