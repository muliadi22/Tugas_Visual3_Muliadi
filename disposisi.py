# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_surat

class form_disposisi(QWidget):
    def _init_(self, parent=None):
        super()._init_(parent)

        # Ganti sesuai nama file UI kamu
        f = QFile('disposisi.ui')
        f.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formdisposisi = loader.load(f, self)
        f.close()

        # CRUD handler
        self.aksi = crud_surat()

        # hubungkan tombol
        self.formdisposisi.BtnSimpan.clicked.connect(self.simpanDisposisi)
        self.formdisposisi.BtnUbah.clicked.connect(self.ubahDisposisi)
        self.formdisposisi.BtnHapus.clicked.connect(self.hapusDisposisi)

    # ---------------- helper ----------------
    def _ambilInput(self):
        id_user = self.formdisposisi.idAdminLineEdit.text().strip()
        # jika kamu punya field id_sm di UI, beri objectName: idSmLineEdit
        id_sm = getattr(self.formdisposisi, "idSmLineEdit", None)
        id_sm = id_sm.text().strip() if id_sm else None

        dinas_instansi = self.formdisposisi.dinasInstansiLineEdit.text().strip()
        tgl_masuk = self.formdisposisi.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formdisposisi.noTanggalSuratLineEdit.text().strip()
        uraian = self.formdisposisi.uraianLineEdit.text().strip()
        lanjut_ke = self.formdisposisi.lanjutKeLineEdit.text().strip()
        tanda_terima = self.formdisposisi.tandaTerimaLineEdit.text().strip()
        return id_user, id_sm, dinas_instansi, tgl_masuk, no_surat, uraian, lanjut_ke, tanda_terima

    # ---------------- CRUD ----------------
    def simpanDisposisi(self):
        id_user, id_sm, dinas_instansi, tgl_masuk, no_surat, uraian, lanjut_ke, tanda_terima = self._ambilInput()
        # Jika skema DB mewajibkan id_sm (FK), pastikan field idSmLineEdit ada di UI
        if id_sm is None or id_sm == "":
            id_sm = None  # kirim None; sesuaikan dengan constraint DB kamu
        self.aksi.tambahDisposisi(id_user, dinas_instansi, tgl_masuk, id_sm,
                                   no_surat, uraian, lanjut_ke, tanda_terima)

    def ubahDisposisi(self):
        # butuh id_disposisi untuk UPDATE
        id_disposisi = self.formdisposisi.idDisposisiLineEdit.text().strip()
        id_user, id_sm, dinas_instansi, tgl_masuk, no_surat, uraian, lanjut_ke, tanda_terima = self._ambilInput()
        if id_sm is None or id_sm == "":
            id_sm = None
        self.aksi.ubahDisposisi(id_disposisi, id_user, dinas_instansi, tgl_masuk, id_sm,
                                 no_surat, uraian, lanjut_ke, tanda_terima)

    def hapusDisposisi(self):
        id_disposisi = self.formdisposisi.idDisposisiLineEdit.text().strip()
        self.aksi.hapusDisposisi(id_disposisi)
