# client_gui_absen.py (versi terbaru: tidak lagi simpan ke Excel, hanya kirim ke server)
import socket
import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Fungsi absen
def kirim_absen():
    nama = entry_nama.get()
    if not nama:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 9000))
        client_socket.send(nama.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()

        # Tampilkan pesan dari server
        messagebox.showinfo("Info", response)

    except Exception as e:
        messagebox.showerror("Error", f"Gagal terhubung ke server: {e}")

    # HAPUS inputan setelah proses kirim, apapun hasilnya
    entry_nama.delete(0, tk.END)

# Rekap absen pribadi
def lihat_rekap():
    if not os.path.exists("data/daftar_absen.txt"):
        messagebox.showinfo("Info", "Belum ada absen yang tersimpan.")
        return
    with open("data/daftar_absen.txt", "r") as f:
        isi = f.read()

    rekap_win = tk.Toplevel(window)
    rekap_win.title("Rekap Absensi Saya")
    rekap_win.geometry("300x180")
    label = tk.Label(rekap_win, text=isi, justify="left")
    label.pack(padx=10, pady=10)

# GUI utama
window = tk.Tk()
window.title("Sistem Absen Siswa")
window.geometry("300x200")

label = tk.Label(window, text="Masukkan Nama:")
label.pack(pady=10)

entry_nama = tk.Entry(window, width=30)
entry_nama.pack(pady=5)

btn_absen = tk.Button(window, text="Kirim Absen", command=kirim_absen)
btn_absen.pack(pady=8)

btn_rekap = tk.Button(window, text="Lihat Rekap Saya", command=lihat_rekap)
btn_rekap.pack(pady=3)

window.mainloop()
