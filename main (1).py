# UTS Dasar Komputer dan Pemrograman
# Kelompok C - Instrumentasi: Monitoring Level Tangki
# Nama: M. Zaid Muzakki
# NIM: 03041182631011

data_level = [
    18, 25, 33, 41, 55,
    62, 76, 84, 91, 47,
    29, 38, 70, 82, 15,
    30, 80, 29, 81, 50
]


# Fungsi untuk menentukan status level
def status_level(level):
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    else:
        return "HIGH"


# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    return sum(data) / len(data)


# Fungsi untuk menghitung jumlah kategori
def hitung_kategori(data, kategori):
    jumlah = 0

    for level in data:
        if status_level(level) == kategori:
            jumlah += 1

    return jumlah


# Memproses seluruh data
print("=== MONITORING LEVEL TANGKI ===")

for nomor, level in enumerate(data_level, start=1):
    status = status_level(level)
    print(f"{nomor:02d}. Level = {level}% -> {status}")


# Menampilkan ringkasan
print("\n=== RINGKASAN ===")
print("Total data:", len(data_level))
print("Jumlah LOW:", hitung_kategori(data_level, "LOW"))
print("Jumlah NORMAL:", hitung_kategori(data_level, "NORMAL"))
print("Jumlah HIGH:", hitung_kategori(data_level, "HIGH"))
print("Rata-rata:", round(rata_rata(data_level), 2), "%")
print("Maksimum:", max(data_level), "%")
print("Minimum:", min(data_level), "%")