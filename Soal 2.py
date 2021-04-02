nama = input("masukkan nama Anda:")
nilai = float(input('masukkan nilai Anda :'))
if nilai >= 85:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah A")
elif 80 <= nilai < 85:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah A-")
elif 75 <= nilai < 80:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah B+")
elif 70 <= nilai < 75:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah B-")
elif 65 <= nilai < 70:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah C")
elif 60 <= nilai < 65:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah C-")
elif nilai < 60:
    print('Halo,', nama + '!', "Nilai Anda setelah dikonversi adalah E")
else:
    print(nilai,'adalah input tidak valid!')
print()