# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suratKeluar.ui'
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
        Form.resize(341, 467)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 251, 409))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.idSuratKeluarLabel = QLabel(self.formLayoutWidget)
        self.idSuratKeluarLabel.setObjectName(u"idSuratKeluarLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idSuratKeluarLabel)

        self.idSuratKeluarLineEdit = QLineEdit(self.formLayoutWidget)
        self.idSuratKeluarLineEdit.setObjectName(u"idSuratKeluarLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idSuratKeluarLineEdit)

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

        self.tanggalKeluarLabel = QLabel(self.formLayoutWidget)
        self.tanggalKeluarLabel.setObjectName(u"tanggalKeluarLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalKeluarLabel)

        self.tanggalKeluarDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalKeluarDateEdit.setObjectName(u"tanggalKeluarDateEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tanggalKeluarDateEdit)

        self.noSuratLabel = QLabel(self.formLayoutWidget)
        self.noSuratLabel.setObjectName(u"noSuratLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.noSuratLabel)

        self.noSuratLineEdit = QLineEdit(self.formLayoutWidget)
        self.noSuratLineEdit.setObjectName(u"noSuratLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.noSuratLineEdit)

        self.tanggalSuratLabel = QLabel(self.formLayoutWidget)
        self.tanggalSuratLabel.setObjectName(u"tanggalSuratLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.tanggalSuratLabel)

        self.tanggalSuratDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalSuratDateEdit.setObjectName(u"tanggalSuratDateEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tanggalSuratDateEdit)

        self.uraianLabel = QLabel(self.formLayoutWidget)
        self.uraianLabel.setObjectName(u"uraianLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.uraianLabel)

        self.uraianLineEdit = QLineEdit(self.formLayoutWidget)
        self.uraianLineEdit.setObjectName(u"uraianLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.uraianLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.idSuratKeluarLabel.setText(QCoreApplication.translate("Form", u"Id Surat Keluar", None))
        self.idAdminLabel.setText(QCoreApplication.translate("Form", u"Id Admin", None))
        self.dinasInstansiLabel.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None))
        self.tanggalKeluarLabel.setText(QCoreApplication.translate("Form", u"Tanggal Keluar", None))
        self.noSuratLabel.setText(QCoreApplication.translate("Form", u"No Surat", None))
        self.tanggalSuratLabel.setText(QCoreApplication.translate("Form", u"Tanggal Surat", None))
        self.uraianLabel.setText(QCoreApplication.translate("Form", u"Uraian", None))
    # retranslateUi

