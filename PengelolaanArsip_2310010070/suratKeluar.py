# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_SuratKeluar(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Surat Keluar")
        filenya = QFile('suratKeluar.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuratKeluar = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formSuratKeluar.BtnSimpan.clicked.connect(self.simpanSuratKeluar)
        self.formSuratKeluar.BtnUbah.clicked.connect(self.ubahSuratKeluar)
        self.formSuratKeluar.BtnHapus.clicked.connect(self.hapusSuratKeluar)

    def simpanSuratKeluar(self):
        id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
        id_admin = self.formSuratKeluar.idAdminLineEdit.text()
        dinas_instansi = self.formSuratKeluar.dinasInstansiLineEdit.text()
        tanggal_keluar = self.formSuratKeluar.tanggalKeluarDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formSuratKeluar.noSuratLineEdit.text()
        tanggal_surat = self.formSuratKeluar.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formSuratKeluar.uraianLineEdit.text()
        self.aksi.tambahSuratKeluar(id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian)

    def ubahSuratKeluar(self):
        id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
        id_admin = self.formSuratKeluar.idAdminLineEdit.text()
        dinas_instansi = self.formSuratKeluar.dinasInstansiLineEdit.text()
        tanggal_keluar = self.formSuratKeluar.tanggalKeluarDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formSuratKeluar.noSuratLineEdit.text()
        tanggal_surat = self.formSuratKeluar.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formSuratKeluar.uraianLineEdit.text()
        self.aksi.gantiSuratKeluar(id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian)

    def hapusSuratKeluar(self):
        id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
        self.aksi.hapusSuratKeluar(id_surat_keluar)
