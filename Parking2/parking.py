import json
import sqlite3


class ParkingAppBackend:
    def __init__(self):
        self.conn = sqlite3.connect("parking.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open(
            "parking.sql", "r"
        ) as sqlfile:  # Pastikan nama file dan pathnya sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # Simpan perubahan ke database

    def save_parking(
        self,
        id_area,
        id_jenis_kendaraan,
        tanggal,
        hari,
        jam,
        jumlah_spd,
        jumlah_spdm,
        jumlah_mobil,
        total,
        gambar,
    ):
        try:
            self.cursor.execute(
                "INSERT INTO parking (id_area, id_jenis_kendaraan, tanggal, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil, total, gambar) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    id_area,
                    id_jenis_kendaraan,
                    tanggal,
                    hari,
                    jam,
                    jumlah_spd,
                    jumlah_spdm,
                    jumlah_mobil,
                    total,
                    gambar,
                ),
            )
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error:", str(e))
            return False

    def save_jenis_kendaraan(self, sepeda, sepeda_motor, mobil):
        try:
            # Mengonversi list deskripsi menjadi format JSON
            # jenis_kendaraan_list = [sepeda, sepeda_motor, mobil]
            # jenis_kendaraan_json = json.dumps(jenis_kendaraan_list)
            self.cursor.execute(
                "INSERT INTO jenis_kendaraan (sepeda, sepeda_motor, mobil) VALUES (?, ?, ?)",
                (sepeda, sepeda_motor, mobil),
            )
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan data kategori:", str(e))
            return False

    def save_area(self, area):
        try:
            # Mengonversi list deskripsi menjadi format JSON
            # area_list = [area]
            # area_json = json.dumps(area_list)
            self.cursor.execute("INSERT INTO area (area) VALUES (?)", (area))
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan data kategori:", str(e))
            return False

    def save_gambar(self, image_data):
        try:
            self.cursor.execute(
                "INSERT INTO gambar (image_data) VALUES (?)", (image_data,)
            )
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan data gambar:", str(e))
            return False
