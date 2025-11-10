# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_surat   # gunakan kelas CRUD yang sesuai dengan DB sistem_surat

class form_admin(QWidget):
    def _init_(self, parent=None):
        super()._init_(parent)

        # Ganti nama file .ui sesuai file-mu
        filenya = QFile('admin.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()

        # konsisten: self.formadmin
        self.formadmin = muatfile.load(filenya, self)
        filenya.close()

        # inisialisasi CRUD
        self.aksi = crud_surat()

        # hubungkan tombol
        self.formadmin.BtnSimpan.clicked.connect(self.simpanAdmin)
        self.formadmin.BtnUbah.clicked.connect(self.ubahAdmin)
        self.formadmin.BtnHapus.clicked.connect(self.hapusAdmin)

    def simpanAdmin(self):
        # id_user auto-increment → tidak diisikan saat INSERT
        username = self.formadmin.usernameLineEdit.text()
        password = self.formadmin.passwordLineEdit.text()
        self.aksi.tambahUser(username, password)

    def ubahAdmin(self):
        # untuk UPDATE butuh id_user
        id_user  = self.formadmin.idAdminLineEdit.text()
        username = self.formadmin.usernameLineEdit.text()
        password = self.formadmin.passwordLineEdit.text()
        self.aksi.ubahUser(id_user, username, password)

    def hapusAdmin(self):
        id_user = self.formadmin.idAdminLineEdit.text()
        self.aksi.hapusUser(id_user)
