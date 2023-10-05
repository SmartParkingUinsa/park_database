CREATE DATABASE IF NOT EXISTS visualisasi;
USE visualisasi;

-- Table masuk
CREATE TABLE IF NOT EXISTS masuk (
    id_pengguna INT PRIMARY KEY AUTO_INCREMENT,
    sandi VARCHAR(20)
);

-- Table sparking
CREATE TABLE IF NOT EXISTS sparking (
    id_sparking INT PRIMARY KEY AUTO_INCREMENT,
    area VARCHAR(20),
    hari TEXT,
    jam TIMESTAMP
);

-- Table sparking
CREATE TABLE IF NOT EXISTS kendaraan (
    id_kendaraan INT PRIMARY KEY AUTO_INCREMENT,
    id_sparking INT,
    jumlah_spd INT,
    jumlah_spdm INT,
    jumlah_mobil INT,
    jumlah_kendaraan INT,
    kepadatan VARCHAR(10),
    FOREIGN KEY (id_sparking) REFERENCES sparking (id_sparking)
);
