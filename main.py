from itertools import combinations

# Fungsi untuk merepresentasikan jadwal kelas
def buat_jadwal(nama, start, end):
    return {"nama": nama, "start": start, "end": end}

def repr_jadwal(jadwal):
    return f"{jadwal['nama']} ({jadwal['start']} - {jadwal['end']})"

# Fungsi untuk memeriksa bentrok
def is_compatible(jadwal):
    jadwal = sorted(jadwal, key=lambda x: x['start'])
    for i in range(1, len(jadwal)):
        if jadwal[i - 1]['end'] > jadwal[i]['start']:
            return False
    return True

# Algoritma Brute Force untuk optimalisasi penjadwalan ruang kelas
def brute_force(jadwal):
    n = len(jadwal)
    best_schedule = []

    # Mencoba semua kombinasi
    for i in range(1, n + 1):
        for combination in combinations(jadwal, i):
            if is_compatible(combination) and len(combination) > len(best_schedule):
                best_schedule = combination

    return best_schedule

# Algoritma Greedy untuk optimalisasi penjadwalan ruang kelas
def greedy(jadwal):
    jadwal = sorted(jadwal, key=lambda x: x['end'])  # Urutkan berdasarkan waktu selesai
    hasil = []
    waktu_sekarang = 0

    for kelas in jadwal:
        if kelas['start'] >= waktu_sekarang:
            hasil.append(kelas)
            waktu_sekarang = kelas['end']

    return hasil

# Data input jadwal kelas
jadwal = [
    buat_jadwal("Kelas A", 8, 10),
    buat_jadwal("Kelas B", 9, 11),
    buat_jadwal("Kelas C", 10, 12),
    buat_jadwal("Kelas D", 11, 13),
    buat_jadwal("Kelas E", 13, 14),
    buat_jadwal("Kelas F", 12, 15),
]
for(kelas) in jadwal:
    print(repr_jadwal(kelas))
# Eksekusi algoritma
print("\nOptimalisasi Penjadwalan Ruang Kelas\n")
print("Algoritma Greedy:")
greedy_result = greedy(jadwal)
for kelas in greedy_result:
    print(repr_jadwal(kelas))

print("\nAlgoritma Brute Force:")
brute_force_result = brute_force(jadwal)
for kelas in brute_force_result:
    print(repr_jadwal(kelas))

# Perbandingan hasil
print("\nJumlah kelas maksimal yang dijadwalkan:")
print(f"Greedy: {len(greedy_result)} kelas")
print(f"Brute Force: {len(brute_force_result)} kelas")