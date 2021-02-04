from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket


class ClickLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ip = QLineEdit(self)
        self.port = QLineEdit(self)

        self.ip.setText(socket.gethostbyname(socket.getfqdn()))
        self.port.setText("5050")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("IP", self.ip)
        layout.addRow("PORT", self.port)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self, what):
        if what == "ip":
            return self.ip.text()
        else:
            return self.port.text()