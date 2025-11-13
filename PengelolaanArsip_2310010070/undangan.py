# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Undangan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Undangan")
        filenya = QFile('undangan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formUndangan = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formUndangan.BtnSimpan.clicked.connect(self.simpanUndangan)
        self.formUndangan.BtnUbah.clicked.connect(self.ubahUndangan)
        self.formUndangan.BtnHapus.clicked.connect(self.hapusUndangan)

    def simpanUndangan(self):
        id_undangan = self.formUndangan.idUndanganLineEdit.text()
        id_admin = self.formUndangan.idAdminLineEdit.text()
        dinas_instansi = self.formUndangan.dinasInstansiLineEdit.text()
        tanggal_masuk = self.formUndangan.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formUndangan.noSuratLineEdit.text()
        tanggal_surat = self.formUndangan.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formUndangan.uraianLineEdit.text()
        lanjut_ke = self.formUndangan.lanjutKeLineEdit.text()
        tanda_terima = self.formUndangan.tandaTerimaLineEdit.text()

        self.aksi.tambahUndangan(id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima)

    def ubahUndangan(self):
        id_undangan = self.formUndangan.idUndanganLineEdit.text()
        id_admin = self.formUndangan.idAdminLineEdit.text()
        dinas_instansi = self.formUndangan.dinasInstansiLineEdit.text()
        tanggal_masuk = self.formUndangan.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formUndangan.noSuratLineEdit.text()
        tanggal_surat = self.formUndangan.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formUndangan.uraianLineEdit.text()
        lanjut_ke = self.formUndangan.lanjutKeLineEdit.text()
        tanda_terima = self.formUndangan.tandaTerimaLineEdit.text()

        self.aksi.gantiUndangan(id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima)

    def hapusUndangan(self):
        id_undangan = self.formUndangan.idUndanganLineEdit.text()
        self.aksi.hapusUndangan(id_undangan)
