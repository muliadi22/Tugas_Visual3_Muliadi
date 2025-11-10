# This Python file uses the following encoding: utf-8
import mysql.connector

class crud_surat:
    def _init_(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sistem_surat'   # ganti jika berbeda
        )

    # ==================== LOGIN_USER ====================
    # id_user AUTO_INCREMENT → INSERT tanpa id_user
    def tambahUser(self, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO login_user (username, password) VALUES (%s, %s)",
            (username, password)
        )
        self.koneksi.commit()
        aksi.close()

    def ubahUser(self, id_user, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "UPDATE login_user SET username=%s, password=%s WHERE id_user=%s",
            (username, password, id_user)
        )
        self.koneksi.commit()
        aksi.close()

    def hapusUser(self, id_user):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM login_user WHERE id_user=%s", (id_user,))
        self.koneksi.commit()
        aksi.close()

    # ==================== SURAT MASUK ====================
    # Kolom: id_sm(AI), id_user(FK), tgl_masuk, no_surat, tgl_surat, uraian,
    #        lanjut_ke, dinas_instansi, tanda_terima
    def tambahSuratMasuk(self, id_user, tgl_masuk, no_surat, tgl_surat,
                          uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            INSERT INTO surat_masuk
            (id_user, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (id_user, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def ubahSuratMasuk(self, id_sm, id_user, tgl_masuk, no_surat, tgl_surat,
                        uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            UPDATE surat_masuk SET
                id_user=%s, tgl_masuk=%s, no_surat=%s, tgl_surat=%s,
                uraian=%s, lanjut_ke=%s, dinas_instansi=%s, tanda_terima=%s
            WHERE id_sm=%s
        """, (id_user, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima, id_sm))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratMasuk(self, id_sm):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_masuk WHERE id_sm=%s", (id_sm,))
        self.koneksi.commit()
        aksi.close()

    # ==================== SURAT KELUAR ====================
    # Kolom: id_sk(AI), id_user(FK), dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian
    def tambahSuratKeluar(self, id_user, dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            INSERT INTO surat_keluar
            (id_user, dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (id_user, dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian))
        self.koneksi.commit()
        aksi.close()

    def ubahSuratKeluar(self, id_sk, id_user, dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            UPDATE surat_keluar SET
                id_user=%s, dinas_instansi=%s, tgl_keluar=%s, no_surat=%s, tgl_surat=%s, uraian=%s
            WHERE id_sk=%s
        """, (id_user, dinas_instansi, tgl_keluar, no_surat, tgl_surat, uraian, id_sk))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratKeluar(self, id_sk):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_keluar WHERE id_sk=%s", (id_sk,))
        self.koneksi.commit()
        aksi.close()

    # ==================== DISPOSISI ====================
    # Kolom: id_disposisi(AI), id_user(FK), dinas_instansi, tgl_masuk, id_sm(FK),
    #        no_surat, uraian, lanjut_ke, tanda_terima
    def tambahDisposisi(self, id_user, dinas_instansi, tgl_masuk, id_sm,
                        no_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            INSERT INTO disposisi
            (id_user, dinas_instansi, tgl_masuk, id_sm, no_surat, uraian, lanjut_ke, tanda_terima)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (id_user, dinas_instansi, tgl_masuk, id_sm, no_surat, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def ubahDisposisi(self, id_disposisi, id_user, dinas_instansi, tgl_masuk, id_sm,
                       no_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            UPDATE disposisi SET
                id_user=%s, dinas_instansi=%s, tgl_masuk=%s, id_sm=%s,
                no_surat=%s, uraian=%s, lanjut_ke=%s, tanda_terima=%s
            WHERE id_disposisi=%s
        """, (id_user, dinas_instansi, tgl_masuk, id_sm, no_surat, uraian, lanjut_ke, tanda_terima, id_disposisi))
        self.koneksi.commit()
        aksi.close()

    def hapusDisposisi(self, id_disposisi):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM disposisi WHERE id_disposisi=%s", (id_disposisi,))
        self.koneksi.commit()
        aksi.close()

    # ==================== UNDANGAN ====================
    # Kolom: id_undangan(AI), id_user(FK), dinas_instansi, tgl_masuk,
    #        no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima
    def tambahUndangan(self, id_user, dinas_instansi, tgl_masuk,
                       no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            INSERT INTO undangan
            (id_user, dinas_instansi, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (id_user, dinas_instansi, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def ubahUndangan(self, id_undangan, id_user, dinas_instansi, tgl_masuk,
                      no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            UPDATE undangan SET
                id_user=%s, dinas_instansi=%s, tgl_masuk=%s, no_surat=%s, tgl_surat=%s,
                uraian=%s, lanjut_ke=%s, tanda_terima=%s
            WHERE id_undangan=%s
        """, (id_user, dinas_instansi, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima, id_undangan))
        self.koneksi.commit()
        aksi.close()

    def hapusUndangan(self, id_undangan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM undangan WHERE id_undangan=%s", (id_undangan,))
        self.koneksi.commit()
        aksi.close()

    # ==================== JENIS_SURAT ====================
    # Kolom: id_jenis(AI), nama_jenis
    def tambahJenisSurat(self, nama_jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("INSERT INTO jenis_surat (nama_jenis) VALUES (%s)", (nama_jenis,))
        self.koneksi.commit()
        aksi.close()

    def ubahJenisSurat(self, id_jenis, nama_jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE jenis_surat SET nama_jenis=%s WHERE id_jenis=%s",
                     (nama_jenis, id_jenis))
        self.koneksi.commit()
        aksi.close()

    def hapusJenisSurat(self, id_jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM jenis_surat WHERE id_jenis=%s", (id_jenis,))
        self.koneksi.commit()
        aksi.close()
