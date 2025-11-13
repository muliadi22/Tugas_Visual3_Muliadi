# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Admin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Admin")
        filenya = QFile('admin.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formAdmin = muatfile.load(filenya, self)
        self.aksi = crud_arsip()

        self.formAdmin.BtnSimpan.clicked.connect(self.simpanAdmin)
        self.formAdmin.BtnUbah.clicked.connect(self.ubahAdmin)
        self.formAdmin.BtnHapus.clicked.connect(self.hapusAdmin)

    def simpanAdmin(self):
                id_admin = self.formAdmin.idAdminLineEdit.text()
                username = self.formAdmin.usernameLineEdit.text()
                password = self.formAdmin.passwordLineEdit.text()
                self.aksi.tambahAdmin(id_admin, username, password)

    def ubahAdmin(self):
                id_admin = self.formAdmin.idAdminLineEdit.text()
                username = self.formAdmin.usernameLineEdit.text()
                password = self.formAdmin.passwordLineEdit.text()
                self.aksi.gantiAdmin(id_admin, username, password)

    def hapusAdmin(self):
                id_admin = self.formAdmin.idAdminLineEdit.text()
                self.aksi.hapusAdmin(id_admin)
