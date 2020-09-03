# soal no 1

Jelaskan itu pivoting dan melting data

Pivoting adalah suatu pengubahan bentuk data dengan memutar data yang terletak di baris menjadi di column, sedangkan 
Melting adalah ‘unpivoting’, melting mengubah suatu data dengan memutar dari yang tadinya berada di posisi column menjadi 
di posisi row.

# soal no 2

gambar diatas reshaping data menggunakan pivoting data, sedangkan gambar di bawah reshaping data menggunakan melting data

# soal no 3

import pandas as pd
import random

data = {
    'Tipe Ujian' : ['UTS1', 'UAS1', 'UTS2', 'UAS2']*3,
    'Mata Pelajaran' : ['Fisika']*4 + ['Matematika']*4+['Statistika']*4,
    'Rata2 Waktu Belajar (menit)' : [random.choice(range(200, 800)) for i in range(12)],
    'Rata2 Nilai Ujian' : [random.choice(range(40, 100)) for i in range(12)] 
}
df = pd.DataFrame(data)
df

df.pivot_table(values = ['Rata2 Nilai Ujian', 'Rata2 Waktu Belajar (menit)'], index = 'Tipe Ujian', columns = 'Mata Pelajaran')

# soal no 4

import pandas as pd

data = {
    'Hari' : ['Sabtu', 'Minggu'],
    'Kebun Binatang' : [271, 399],
    'Dufan' : [501, 700],
    'Disney' : [1000, 1001],
    'Bali' : [900, 803]
}
df = pd.DataFrame(data).set_index('Hari')
df.reset_index(inplace = True)

pd.melt(df, id_vars = ['Hari'], value_vars = ['Kebun Binatang', 'Dufan', 'Disney', 'Bali'], var_name = 'Tempat Hiburan', value_name = 'Pengunjung')

# soal no 5

import pandas as pd

data = {
    'Tipe Ujian' : ['UTS1', 'UAS1']*3,
    'Mata Pelajaran' :['Statistika', 'Fisika', 'Fisika', 'Statistika', 'Fisika', 'Statistika'],
    'Jumlah Peserta' : [14, 17, 12, 16, 14, 13]
}
df = pd.DataFrame(data).set_index('Tipe Ujian')
df

df.pivot_table(index = 'Tipe Ujian', columns = 'Mata Pelajaran', values = 'Jumlah Peserta', aggfunc = 'sum')