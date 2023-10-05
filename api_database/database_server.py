import mysql.connector

class DatabaseManager:
    def __init__(self):
        # Konfigurasi koneksi ke database MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Ganti dengan nama pengguna Anda
            password="",  # Ganti dengan kata sandi Anda (jika ada)
            database="parking"  # Ganti dengan nama database yang Anda gunakan
        )
        self.cursor = self.connection.cursor()

    def insert_parking_data(self, data):
        query = """
           INSERT INTO parking(id, id_area, id_jenis_kendaraan, id_gambar, tanggal, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil, total)
           VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, data)
        self.connection.commit()

    def get_parking(self):
        try:
            query = "SELECT * FROM parking"
            self.cursor.execute(query)

            parking_data = self.cursor.fetchall()
            return parking_data
        except Exception as e:
            print("Error:", e)
            return []

    def close_connection(self):
        # Menutup koneksi ke database MySQL
        self.connection.close()
