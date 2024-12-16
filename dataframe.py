import pandas as pd

data_csv = pd.read_csv('data_sampah_jabar.csv')

#1. DataFrame
kolom = ["nama_kabupaten_kota", "jumlah_produksi_sampah", "tahun"]
data_sampah = data_csv[kolom]
data_sampah = data_sampah.rename(columns={
    "nama_kabupaten_kota": "Kabupaten/Kota",
    "jumlah_produksi_sampah": "Sampah (Ton)",
    "tahun": "Tahun"
})
print(data_sampah)

#2. Hitung Total sampah di jabar tahun tertentu
sampah_2020 = 0
for i,j in data_sampah.iterrows():
    if j ["Tahun"] == 2020:
        sampah_2020 += j["Sampah (Ton)"]

print(f"\nTotal Produksi Sampah Di JABAR Tahun 2020: {sampah_2020:.2f}Ton")

#3. Sampah Setiap Tahun
total_sampah_semua_tahun = {}
for i, j in data_sampah.iterrows():
    tahun = j["Tahun"]
    sampah = j["Sampah (Ton)"]
    if tahun not in total_sampah_semua_tahun:
        total_sampah_semua_tahun[tahun] = 0
    total_sampah_semua_tahun[tahun] += sampah

print("\nJumlah Produksi Sampah Setiap Tahun:")
for tahun, total in total_sampah_semua_tahun.items():
    print(f"Tahun {tahun}: {total:.2f} ton/hari")

#4. Sampah per Kab/kota setiap tahun
sampah_kotakab_tahun = {}
for i, j in data_sampah.iterrows():
    kota = j["Kabupaten/Kota"]
    tahun = j["Tahun"]
    sampah = j["Sampah (Ton)"]
    if kota not in sampah_kotakab_tahun:
        sampah_kotakab_tahun[kota] = {}
    if tahun not in sampah_kotakab_tahun[kota]:
        sampah_kotakab_tahun[kota][tahun] = 0
    sampah_kotakab_tahun[kota][tahun] += sampah

print(f"\n===Jumlah Sampah Kabupaten/Kota Setiap Tahun===")
for kota,tahun in sampah_kotakab_tahun.items():
    print(f"\n{kota}:")
    for tahun, total in tahun.items():
        print(f"Tahun {tahun}: {total:.2f} Ton")

data_sampah.to_csv('sampahakhir.csv',index=False)
data_sampah.to_excel('sampahakhir.xlsx', index=False)