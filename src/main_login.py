# main_login.py (Tema Pokémon White & Black Version)
import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import os

# Password untuk login guru
PASSWORD_ADMIN = "admin123"

# Fungsi kalau klik login sebagai Guru
def login_guru():
    password = simpledialog.askstring("Login Guru", "Masukkan Password:", show='*')
    if password == PASSWORD_ADMIN:
        messagebox.showinfo("Sukses", "Login Guru berhasil!")
        jalankan_server()
    else:
        messagebox.showerror("Gagal", "Password salah!")

# Fungsi kalau klik login sebagai Murid
def login_murid():
    jalankan_client()

# Fungsi jalankan server
def jalankan_server():
    try:
        subprocess.Popen(["python", "src/server_gui_absen.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka server: {e}")

# Fungsi jalankan client
def jalankan_client():
    try:
        subprocess.Popen(["python", "src/client_gui_absen.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka client: {e}")

# Buat jendela utama
window = tk.Tk()
window.title("Login Absensi Pokémon BW")
window.geometry("400x350")
window.configure(bg="white")

# Tambahkan teks Logo (placeholder)
label_logo = tk.Label(window, text="Pokémon BW ⚡", font=("Arial", 20, "bold"), bg="white", fg="black")
label_logo.pack(pady=15)

# Label utama
label = tk.Label(window, text="Login Absensi", font=("Arial", 16), bg="white", fg="black")
label.pack(pady=10)

# Tombol login
btn_guru = tk.Button(window, text="Login sebagai Guru", width=20, bg="white", fg="black", font=("Arial", 12), relief="solid", bd=2, command=login_guru)
btn_guru.pack(pady=10)

btn_murid = tk.Button(window, text="Login sebagai Murid", width=20, bg="black", fg="white", font=("Arial", 12), relief="flat", command=login_murid)
btn_murid.pack(pady=10)

window.mainloop()