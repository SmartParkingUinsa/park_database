import sqlite3

class desktop:
    def __init__(self):
        self.conn = sqlite3.connect("visualisasi.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open('visualisasi.sql', 'r') as sqlfile:  # Pastikan nama file dan pathnya sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # Simpan perubahan ke database

    def save_masuk(self,id_pengguna,sandi): 
        try: 
            self.cursor.execute("INSERT INTO masuk (id_pengguna,sandi) VALUES (?, ?)", (id_pengguna,sandi))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_sparking(self,id_sparking, area, hari, jam): 
        try: 
            self.cursor.execute("INSERT INTO sparking (id_sparking, area, hari, jam) VALUES (?, ?, ?, ?)", (id_sparking, area, hari, jam))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False
    
    def save_kendaraan(self,id_kendaraan, id_sparking, jumlah_spd, jumlah_spdm, jumlah_mobil, jumlah_kendaraan, kepadatan): 
        try: 
            self.cursor.execute("INSERT INTO sparking (id_kendaraan, id_sparking, jumlah_spd, jumlah_spdm, jumlah_mobil, jumlah_kendaraan, kepadatan) VALUES (?, ?, ?, ?, ?, ?, ?)", (id_kendaraan, id_sparking, jumlah_spd, jumlah_spdm, jumlah_mobil, jumlah_kendaraan, kepadatan))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False