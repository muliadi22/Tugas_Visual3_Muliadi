# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip


class form_SuratMasuk(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Surat Masuk")
        filenya = QFile('suratMasuk.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuratMasuk = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formSuratMasuk.BtnSimpan.clicked.connect(self.simpanSuratMasuk)
        self.formSuratMasuk.BtnUbah.clicked.connect(self.ubahSuratMasuk)
        self.formSuratMasuk.BtnHapus.clicked.connect(self.hapusSuratMasuk)

    def simpanSuratMasuk(self):
            id_surat_masuk = self.formSuratMasuk.idSuratMasukLineEdit.text()
            id_admin = self.formSuratMasuk.idAdminLineEdit.text()
            tanggal_masuk = self.formSuratMasuk.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
            no_surat = self.formSuratMasuk.noSuratLineEdit.text()
            tanggal_surat = self.formSuratMasuk.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
            uraian = self.formSuratMasuk.uraianLineEdit.text()
            lanjut_ke = self.formSuratMasuk.lanjutKeLineEdit.text()
            dinas_instansi = self.formSuratMasuk.dinasInstansiLineEdit.text()
            tanda_terima = self.formSuratMasuk.tandaTerimaLineEdit.text()

            self.aksi.tambahSuratMasuk(id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima)

    def ubahSuratMasuk(self):
            id_surat_masuk = self.formSuratMasuk.idSuratMasukLineEdit.text()
            id_admin = self.formSuratMasuk.idAdminLineEdit.text()
            tanggal_masuk = self.formSuratMasuk.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
            no_surat = self.formSuratMasuk.noSuratLineEdit.text()
            tanggal_surat = self.formSuratMasuk.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
            uraian = self.formSuratMasuk.uraianLineEdit.text()
            lanjut_ke = self.formSuratMasuk.lanjutKeLineEdit.text()
            dinas_instansi = self.formSuratMasuk.dinasInstansiLineEdit.text()
            tanda_terima = self.formSuratMasuk.tandaTerimaLineEdit.text()

            self.aksi.gantiSuratMasuk(id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima)

    def hapusSuratMasuk(self):
            id_surat_masuk = self.formSuratMasuk.idSuratMasukLineEdit.text()
            self.aksi.hapusSuratMasuk(id_surat_masuk)
