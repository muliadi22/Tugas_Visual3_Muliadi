# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class form_SuratMasuk(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Surat Masuk")
        filenya = QFile('suratMasuk.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuratMasuk = muatfile.load(filenya,self)
