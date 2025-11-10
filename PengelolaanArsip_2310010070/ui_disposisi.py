# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disposisi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(583, 511)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(170, 60, 251, 383))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.idDisposisiLabel = QLabel(self.formLayoutWidget)
        self.idDisposisiLabel.setObjectName(u"idDisposisiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idDisposisiLabel)

        self.idDisposisiLineEdit = QLineEdit(self.formLayoutWidget)
        self.idDisposisiLineEdit.setObjectName(u"idDisposisiLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idDisposisiLineEdit)

        self.idAdminLabel = QLabel(self.formLayoutWidget)
        self.idAdminLabel.setObjectName(u"idAdminLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.idAdminLabel)

        self.idAdminLineEdit = QLineEdit(self.formLayoutWidget)
        self.idAdminLineEdit.setObjectName(u"idAdminLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.idAdminLineEdit)

        self.dinasInstansiLabel = QLabel(self.formLayoutWidget)
        self.dinasInstansiLabel.setObjectName(u"dinasInstansiLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.dinasInstansiLabel)

        self.dinasInstansiLineEdit = QLineEdit(self.formLayoutWidget)
        self.dinasInstansiLineEdit.setObjectName(u"dinasInstansiLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dinasInstansiLineEdit)

        self.tanggalMasukLabel = QLabel(self.formLayoutWidget)
        self.tanggalMasukLabel.setObjectName(u"tanggalMasukLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalMasukLabel)

        self.tanggalMasukDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalMasukDateEdit.setObjectName(u"tanggalMasukDateEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tanggalMasukDateEdit)

        self.noTanggalSuratLabel = QLabel(self.formLayoutWidget)
        self.noTanggalSuratLabel.setObjectName(u"noTanggalSuratLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.noTanggalSuratLabel)

        self.noTanggalSuratLineEdit = QLineEdit(self.formLayoutWidget)
        self.noTanggalSuratLineEdit.setObjectName(u"noTanggalSuratLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.noTanggalSuratLineEdit)

        self.isiDisposisiLabel = QLabel(self.formLayoutWidget)
        self.isiDisposisiLabel.setObjectName(u"isiDisposisiLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.isiDisposisiLabel)

        self.isiDisposisiLineEdit = QLineEdit(self.formLayoutWidget)
        self.isiDisposisiLineEdit.setObjectName(u"isiDisposisiLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.isiDisposisiLineEdit)

        self.uraianLabel = QLabel(self.formLayoutWidget)
        self.uraianLabel.setObjectName(u"uraianLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.uraianLabel)

        self.uraianLineEdit = QLineEdit(self.formLayoutWidget)
        self.uraianLineEdit.setObjectName(u"uraianLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.uraianLineEdit)

        self.lanjutKeLabel = QLabel(self.formLayoutWidget)
        self.lanjutKeLabel.setObjectName(u"lanjutKeLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lanjutKeLabel)

        self.lanjutKeLineEdit = QLineEdit(self.formLayoutWidget)
        self.lanjutKeLineEdit.setObjectName(u"lanjutKeLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lanjutKeLineEdit)

        self.tandaTerimaLabel = QLabel(self.formLayoutWidget)
        self.tandaTerimaLabel.setObjectName(u"tandaTerimaLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.tandaTerimaLabel)

        self.tandaTerimaLineEdit = QLineEdit(self.formLayoutWidget)
        self.tandaTerimaLineEdit.setObjectName(u"tandaTerimaLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.tandaTerimaLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.idDisposisiLabel.setText(QCoreApplication.translate("Form", u"Id Disposisi", None))
        self.idAdminLabel.setText(QCoreApplication.translate("Form", u"Id Admin", None))
        self.dinasInstansiLabel.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None))
        self.tanggalMasukLabel.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.noTanggalSuratLabel.setText(QCoreApplication.translate("Form", u"No Tanggal Surat", None))
        self.isiDisposisiLabel.setText(QCoreApplication.translate("Form", u"Isi Disposisi", None))
        self.uraianLabel.setText(QCoreApplication.translate("Form", u"Uraian", None))
        self.lanjutKeLabel.setText(QCoreApplication.translate("Form", u"Lanjut Ke", None))
        self.tandaTerimaLabel.setText(QCoreApplication.translate("Form", u"Tanda Terima", None))
    # retranslateUi

