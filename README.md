
# 📘 Sistem Absensi I/O Multiplexing (GUI)

## 🎯 Deskripsi
Sistem ini adalah aplikasi absensi sederhana menggunakan Python:
- Server dapat mendengarkan banyak klien sekaligus dengan I/O Multiplexing (`select`)
- Client dapat melakukan absen dan melihat rekap absensinya
- Tersedia GUI untuk siswa & admin (menggunakan Tkinter)

---

## 🖥️ Fitur

### Server (server_gui_absen.py)
✅ GUI real-time menampilkan daftar hadir  
✅ Mencatat waktu absen otomatis  
✅ Mencegah absen lebih dari 1x  
✅ Ekspor ke Excel  
✅ Filter absensi berdasarkan jam  
✅ Reset otomatis setiap jam 00:00  
✅ Edit data absensi langsung dari tabel

### Client (client_gui_absen.py)
✅ Input nama untuk absen  
✅ Balasan langsung dari server  
✅ Menyimpan bukti absen ke file lokal  
✅ Bisa melihat rekap absen kapan saja

---

## 📂 Struktur Folder

```
absensi_io_multiplexing/
├── server_gui_absen.py
├── client_gui_absen.py
├── daftar_absen.txt
├── absen_anda.txt
├── absensi_export.xlsx
├── README.pdf
└── requirements.txt (Buat install modul)
```

---

## 🚀 Cara Menjalankan

1. Jalankan server dulu:
```bash
python server_gui_absen.py
```

2. Jalankan client siswa:
```bash
python client_gui_absen.py
```

3. Server akan mencatat kehadiran dan tampilkan daftar secara real-time.

---

## 🛠️ Persyaratan

- Python 3.x
- Modul:
  - `tkinter` (built-in)
  - `openpyxl`
  - `socket`, `select`, `threading`

- Pastikan file requirements.txt ada 
├──python3 -m venv venv         # buat virtual environment baru
├──source venv/bin/activate     # aktifkan environment-nya
└──pip install -r requirements.txt  # install semua package yang kamu pakai

# Sistem Absensi Siswa (I/O Multiplexing)

## 📚 Fitur
- Login sebagai Guru (admin)
- Login sebagai Murid (client)
- Server mencatat absensi ke file Excel
- Client mengirim data absensi

## 🛠 Cara Menjalankan
1. Jalankan `main_login.py`
2. Pilih login:
   - Guru → Password: `admin123`
   - Guru → Load file excel
   - Murid → Langsung input nama

## 📂 Struktur Folder
- src/: Source code Python
- assets/: Gambar dan icon
- data/: Data absensi (Excel, TXT)
- dist/: Hasil bundling .exe

## 🔑 Password Admin
- admid123