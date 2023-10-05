-- Buat database jika belum ada
CREATE DATABASE IF NOT EXISTS parking;
USE parking;


-- Table Area
CREATE TABLE IF NOT EXISTS area (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    area VARCHAR(20)
);

-- Table Jenis Kendaraan
CREATE TABLE IF NOT EXISTS jenis_kendaraan (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    jenis_kendaraan VARCHAR(20)
);

-- Table Gambar
CREATE TABLE IF NOT EXISTS gambar (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    image_data BLOB
);

-- Table Parking
CREATE TABLE IF NOT EXISTS parking (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_area INTEGER,
    id_jenis_kendaraan INTEGER,
    id_gambar INTEGER,
    tanggal INTEGER,
    hari TEXT,
    jam TIMESTAMP(6),
    jumlah_spd INTEGER,
    jumlah_spdm INTEGER,
    jumlah_mobil INTEGER,
    total INTEGER,
    FOREIGN KEY (id_area) REFERENCES area (id),
    FOREIGN KEY (id_jenis_kendaraan) REFERENCES jenis_kendaraan (id),
    FOREIGN KEY (id_gambar) REFERENCES gambar (id),
    UNIQUE(tanggal, jam)
);
