import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton, QGridLayout, QLineEdit, QPlainTextEdit


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # self.setMinimumSize(int(cfg.get("Appearance", "min.width")), int(cfg.get("Appearance", "min.height")))
        # self.resize(int(cfg.get("Window", "width")), int(cfg.get("Window", "height")))
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()

        #self.button = QPushButton("Push")
        # TODO: remove push button
        # self.button.clicked.connect(self.set_rbutton)

        # TODO: enable line edit on radio button change
        self.modbusProtocolAscii = QRadioButton("ASCII")
        self.modbusProtocolAsciiSerial = QLineEdit()
        self.modbusProtocolAsciiSerial.setPlaceholderText("COM1:")
        self.modbusProtocolRtu = QRadioButton("RTU")
        self.modbusProtocolRtuSerial = QLineEdit()
        self.modbusProtocolRtuSerial.setPlaceholderText("COM1:")
        self.modbusProtocolTcp = QRadioButton("TCP")
        self.modbusProtocolTcpIp = QLineEdit()
        self.modbusProtocolTcpIp.setPlaceholderText("192.168.1.10")
        self.modbusProtocolUdp = QRadioButton("UDP")
        self.modbusProtocolUpdIp = QLineEdit()
        self.modbusProtocolUpdIp.setPlaceholderText("192.168.1.11")
        self.modbusProtocolEnc = QRadioButton("RTU over TCP")
        self.modbusProtocolEncIp = QLineEdit()
        self.modbusProtocolEncIp.setPlaceholderText("192.168.1.10")
        #
        # self.buttons_values = {
        #     "1": self.r1,
        #     "2": self.r2,
        #     "3": self.r3,
        #     "4": self.r4,
        # }

        self.generateButton = QPushButton("generate")
        self.generateButton.clicked.connect(self.generateCommandLine)

        self.commandLine = QPlainTextEdit()
        self.commandLine.setPlaceholderText("modpoll ...")
        self.commandLine.setReadOnly(True)

        g_layout = QGridLayout(self)
        #g_layout.addWidget(self.button, 1, 2)
        g_layout.addWidget(self.modbusProtocolAscii, 2, 1)
        g_layout.addWidget(self.modbusProtocolAsciiSerial, 2, 2)
        g_layout.addWidget(self.modbusProtocolRtu, 3, 1)
        g_layout.addWidget(self.modbusProtocolRtuSerial, 3, 2)
        g_layout.addWidget(self.modbusProtocolTcp, 4, 1)
        g_layout.addWidget(self.modbusProtocolTcpIp, 4, 2)
        g_layout.addWidget(self.modbusProtocolUdp, 5, 1)
        g_layout.addWidget(self.modbusProtocolUpdIp, 5, 2)
        g_layout.addWidget(self.modbusProtocolEnc, 6, 1)
        g_layout.addWidget(self.modbusProtocolEncIp, 6, 2)
        g_layout.addWidget(self.generateButton, 7, 1)
        g_layout.addWidget(self.commandLine, 8, 1, 1, 2)

        self.show()

    def generateCommandLine(self):
        line = "modpoll: " + self.generateModbusProtocol()

        self.commandLine.insertPlainText(line)
        pass

    def generateModbusProtocol(self):
        line = ""
        if self.modbusProtocolAscii.isChecked():
            line = line + "-m ascii " + self.modbusProtocolRtuSerial.text() + "\n"
        if self.modbusProtocolRtu.isChecked():
            line = line + "-m rtu " + self.modbusProtocolTcpIp.text() + "\n"
        if self.modbusProtocolTcp.isChecked():
            line = line + "-m tcp " + self.modbusProtocolTcpIp.text() + "\n"
        if self.modbusProtocolUdp.isChecked():
            line = line + "-m udp " + self.modbusProtocolTcpIp.text() + "\n"
        if self.modbusProtocolEnc.isChecked():
            line = line + "-m enc " + self.modbusProtocolTcpIp.text() + "\n"

        return line

    # TODO: block
    def blockProtocol(self):
        if self.modbusProtocolAscii.isChecked():
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = Main()
    sys.exit(app.exec_())
