# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Disposisi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Disposisi")
        filenya = QFile('disposisi.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formDisposisi = muatfile.load(filenya, self)
        self.aksi = crud_arsip()

        self.formDisposisi.BtnSimpan.clicked.connect(self.simpanDisposisi)
        self.formDisposisi.BtnUbah.clicked.connect(self.ubahDisposisi)
        self.formDisposisi.BtnHapus.clicked.connect(self.hapusDisposisi)

    def simpanDisposisi(self):
        id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
        id_admin = self.formDisposisi.idAdminLineEdit.text()
        dinas_instansi = self.formDisposisi.dinasInstansiLineEdit.text()
        tanggal_masuk = self.formDisposisi.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_tanggal_surat = self.formDisposisi.noTanggalSuratLineEdit.text()
        isi_disposisi = self.formDisposisi.isiDisposisiLineEdit.text()
        uraian = self.formDisposisi.uraianLineEdit.text()
        lanjut_ke = self.formDisposisi.lanjutKeLineEdit.text()
        tanda_terima = self.formDisposisi.tandaTerimaLineEdit.text()

        self.aksi.tambahDisposisi(id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)

    def ubahDisposisi(self):
        id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
        id_admin = self.formDisposisi.idAdminLineEdit.text()
        dinas_instansi = self.formDisposisi.dinasInstansiLineEdit.text()
        tanggal_masuk = self.formDisposisi.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_tanggal_surat = self.formDisposisi.noTanggalSuratLineEdit.text()
        isi_disposisi = self.formDisposisi.isiDisposisiLineEdit.text()
        uraian = self.formDisposisi.uraianLineEdit.text()
        lanjut_ke = self.formDisposisi.lanjutKeLineEdit.text()
        tanda_terima = self.formDisposisi.tandaTerimaLineEdit.text()

        self.aksi.gantiDisposisi(id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)

    def hapusDisposisi(self):
        id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
        self.aksi.hapusDisposisi(id_disposisi)
