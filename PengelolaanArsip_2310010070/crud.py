# This Python file uses the following encoding: utf-8
import mysql.connector

class crud_arsip:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pengelolaanarsip_2310010070'
        )

    # ===== CRUD ADMIN =====
    def tambahAdmin(self, id, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("INSERT INTO admin (id_admin, username, password) VALUES (%s, %s, %s)",
                    (id, username, password))
        self.koneksi.commit()
        aksi.close()

    def gantiAdmin(self, id, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE admin SET username=%s, password=%s WHERE id_admin=%s",
                    (username, password, id))
        self.koneksi.commit()
        aksi.close()

    def hapusAdmin(self, id):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM admin WHERE id_admin=%s", (id,))
        self.koneksi.commit()
        aksi.close()

    # ===== CRUD SURAT MASUK =====
    def tambahSuratMasuk(self, id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO surat_masuk (id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiSuratMasuk(self, id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE surat_masuk SET id_admin=%s, tanggal_masuk=%s, no_surat=%s,
                    tanggal_surat=%s, uraian=%s, lanjut_ke=%s, dinas_instansi=%s, tanda_terima=%s WHERE id_surat_masuk=%s"""
        aksi.execute(sql, (id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima, id_surat_masuk))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratMasuk(self, id_surat_masuk):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_masuk WHERE id_surat_masuk=%s", (id_surat_masuk,))
        self.koneksi.commit()
        aksi.close()

    # ===== CRUD SURAT KELUAR =====
    def tambahSuratKeluar(self, id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO surat_keluar
                    (id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian))
        self.koneksi.commit()
        aksi.close()

    def gantiSuratKeluar(self, id_surat_keluar, id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian):
        aksi = self.koneksi.cursor()
        sql = """UPDATE surat_keluar SET id_admin=%s, dinas_instansi=%s, tanggal_keluar=%s,
                    no_surat=%s, tanggal_surat=%s, uraian=%s WHERE id_surat_keluar=%s"""
        aksi.execute(sql, (id_admin, dinas_instansi, tanggal_keluar, no_surat, tanggal_surat, uraian, id_surat_keluar))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratKeluar(self, id_surat_keluar):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_keluar WHERE id_surat_keluar=%s", (id_surat_keluar,))
        self.koneksi.commit()
        aksi.close()

    # ===== CRUD DISPOSISI =====
    def tambahDisposisi(self, id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO disposisi (id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiDisposisi(self, id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE disposisi SET id_admin=%s, dinas_instansi=%s, tanggal_masuk=%s, no_tanggal_surat=%s,
                    isi_disposisi=%s, uraian=%s, lanjut_ke=%s, tanda_terima=%s WHERE id_disposisi=%s"""
        aksi.execute(sql, (id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima, id_disposisi))
        self.koneksi.commit()
        aksi.close()

    def hapusDisposisi(self, id_disposisi):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM disposisi WHERE id_disposisi=%s", (id_disposisi,))
        self.koneksi.commit()
        aksi.close()

    # ===== CRUD UNDANGAN =====
    def tambahUndangan(self, id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO undangan
                    (id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiUndangan(self, id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE undangan SET id_admin=%s, dinas_instansi=%s, tanggal_masuk=%s,
                    no_surat=%s, tanggal_surat=%s, uraian=%s, lanjut_ke=%s, tanda_terima=%s WHERE id_undangan=%s"""
        aksi.execute(sql, (id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima, id_undangan))
        self.koneksi.commit()
        aksi.close()

    def hapusUndangan(self, id_undangan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM undangan WHERE id_undangan=%s", (id_undangan,))
        self.koneksi.commit()
        aksi.close()
