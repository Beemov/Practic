import sys
import subprocess

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton, QGridLayout, QLineEdit, QPlainTextEdit, QCheckBox


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # self.setMinimumSize(int(cfg.get("Appearance", "min.width")), int(cfg.get("Appearance", "min.height")))
        # self.resize(int(cfg.get("Window", "width")), int(cfg.get("Window", "height")))
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()

        # self.button = QPushButton("Push")
        # TODO: remove push button
        # self.button.clicked.connect(self.set_rbutton)

        # TODO: enable line edit on radio button change
        # self.modbusProtocolAscii = QRadioButton("ASCII")
        # self.modbusProtocolAsciiSerial = QLineEdit()
        # self.modbusProtocolAsciiSerial.setPlaceholderText("COM1:")
        # self.modbusProtocolRtu = QRadioButton("RTU")
        # self.modbusProtocolRtuSerial = QLineEdit()
        # self.modbusProtocolRtuSerial.setPlaceholderText("COM1:")
        self.modbusProtocolTcp = QRadioButton("TCP")
        self.modbusProtocolTcpIp = QLineEdit()
        self.modbusProtocolTcpIp.setPlaceholderText("127.0.0.1")
        # self.modbusProtocolUdp = QRadioButton("UDP")
        # self.modbusProtocolUpdIp = QLineEdit()
        # self.modbusProtocolUpdIp.setPlaceholderText("192.168.1.11")
        # self.modbusProtocolEnc = QRadioButton("RTU over TCP")
        # self.modbusProtocolEncIp = QLineEdit()
        # self.modbusProtocolEncIp.setPlaceholderText("192.168.1.10")

        # self.pathtoM = "path to modpoll"
        # self.pathtoModpoll.setPlaceholderText('D:\win\modpoll.exe')
        # self.pathtoModpoll = QLineEdit()
        # self.pathtoD = "path to diagslave"
        # self.pathtoDiagslave.setPlaceholderText("D:\win\diagslave.exe")
        # self.pathtoDiagslave = QLineEdit()
        self.commandR = QCheckBox("-r")
        self.command_R = QLineEdit()
        self.command_R.setPlaceholderText("100")
        self.commandC = QCheckBox("-c")
        self.command_C = QLineEdit()
        self.command_C.setPlaceholderText("5")

        self.generateButton = QPushButton("generate")
        self.generateButton.clicked.connect(self.insertCommandLine)

        self.StartButton = QPushButton("start")
        self.StartButton.clicked.connect(self.insertResult)

        self.commandLine = QPlainTextEdit()
        self.commandLine.setPlaceholderText("modpoll ...")
        self.commandLine.setReadOnly(True)

        g_layout = QGridLayout(self)
        # g_layout.addWidget(self.pathtoM, 1, 1)
        # g_layout.addWidget(self.pathtoModpoll, 1, 2)
        # g_layout.addWidget(self.pathtoD, 2, 1)
        # g_layout.addWidget(self.pathtoDiagslave, 2, 2)
        # g_layout.addWidget(self.modbusProtocolAsciiSerial, 2, 2)
        g_layout.addWidget(self.commandR, 5, 1)
        g_layout.addWidget(self.command_R, 5, 2)
        g_layout.addWidget(self.commandC, 6, 1)
        g_layout.addWidget(self.command_C, 6, 2)
        g_layout.addWidget(self.modbusProtocolTcp, 4, 1)
        g_layout.addWidget(self.modbusProtocolTcpIp, 4, 2)
        # g_layout.addWidget(self.modbusProtocolUdp, 5, 1)
        # g_layout.addWidget(self.modbusProtocolUpdIp, 5, 2)
        # g_layout.addWidget(self.modbusProtocolEnc, 6, 1)
        # g_layout.addWidget(self.modbusProtocolEncIp, 6, 2)
        g_layout.addWidget(self.generateButton, 7, 1)
        g_layout.addWidget(self.StartButton, 7, 2)
        g_layout.addWidget(self.commandLine, 8, 1, 2, 2)

        self.show()

    def insertCommandLine(self):
        line = "modpoll " + self.generateCommandLine()
        self.commandLine.insertPlainText(line)
        # self.insertResultinLine()
        pass

    # def insertResultinLine(self):
    #     res = self.Modpoll()
    #     self.commandLine.insertPlainText(res)
    #     pass

    def generateCommandLine(self):
        line = self.generateCommands() + self.generateModbusProtocol() + "\n"
        return line

    def generateModbusProtocol(self):
        line = ""
        i = 0
        # if self.modbusProtocolAscii.isChecked():
        #     line = line + "-m ascii " + self.modbusProtocolRtuSerial.text() + "\n"
        # if self.modbusProtocolRtu.isChecked():
        #     line = line + "-m rtu " + self.modbusProtocolTcpIp.text() + "\n"
        if self.modbusProtocolTcp.isChecked():
            i += 1
            if not self.modbusProtocolTcpIp.text():
                self.modbusProtocolTcpIp.setText("127.0.0.1")
            line = line + "-m tcp " + self.modbusProtocolTcpIp.text() + "\n"
        # if self.modbusProtocolUdp.isChecked():
        #     line = line + "-m udp " + self.modbusProtocolTcpIp.text() + "\n"
        # if self.modbusProtocolEnc.isChecked():
        #     line = line + "-m enc " + self.modbusProtocolTcpIp.text() + "\n"
        if i != 1:
            self.modbusProtocolTcpIp.setText("127.0.0.1")
            line = line + "-m tcp " + self.modbusProtocolTcpIp.text() + "\n"

        return line

    def generateCommands(self):
        line = ""
        if self.commandC.isChecked():
            if not self.command_C.text():
                self.command_C.setText("5")
            line = line + "-c " + self.command_C.text() + " "
        if self.commandR.isChecked():
            if not self.command_R.text():
                self.command_R.setText("100")
            line = line + "-r " + self.command_R.text() + " "
        line = line + "-1 "
        return line

    # todo: запустить modpoll и передать в него команду
    def Modpoll(self):
        i = 0
        # subprocess.Popen(["D:\win\modpoll.exe",'self.generateCommandLine()'])
        # print(subprocess.check_output(["D:\win\modpoll.exe", self.generateCommandLine()]))
        args = self.generateCommandLine().split()
        cmd = ['D:\win\modpoll.exe']
        cmd = cmd + args
        res = subprocess.check_output(cmd).splitlines()
        # subprocess.Popen.kill(cmd)
        # print(res)
        # self.commandLine.insertPlainText(res)
        # subprocess.check_output.kill(cmd)
        return res

    def insertResult(self):
        i = 0
        result = self.Modpoll()
        while i <= len(result):
            print(result[i])
            # self.commandLine.setPlainText(result[i])
            i += 1

        pass

if __name__ == "__main__":
    p = subprocess.Popen("D:\win\diagslave.exe")
    app = QtWidgets.QApplication(sys.argv)
    game = Main()
    sys.exit(app.exec_())
    subprocess.Popen.kill(p)
