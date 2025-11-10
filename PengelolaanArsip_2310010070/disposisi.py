# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class form_Disposisi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Disposisi")
        filenya = QFile('disposisi.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formDisposisi = muatfile.load(filenya,self)
