import streamlit as st

from faker import Faker
import pandas as pd
import math 
import matplotlib.pyplot as plt


fake = Faker('id_ID')

class Product():
    def __init__(self, bulan, nama, jumlah_stok_awal, pengeluaran_stok, pemasukan_stok, jumlah_stok_akhir, biaya_penyimpanan, biaya_pemesanan, harga_produk):
        self.bulan = bulan
        self.nama = nama
        self.jumlah_stok_awal = jumlah_stok_awal
        self.pengeluaran_stok = pengeluaran_stok
        self.pemasukan_stok = pemasukan_stok
        self.jumlah_stok_akhir = jumlah_stok_akhir
        self.biaya_penyimpanan = biaya_penyimpanan
        self.biaya_pemesanan = biaya_pemesanan
        self.harga_produk = harga_produk

    def __repr__(self):
      return "{}: {}".format(self.__class__.__name__, vars(self))


product_name = [('Permen Apel', 1), ('Permen Semangka', 1), ('Permen Melon', 1), ('Cokelat Susu', 2), ('Cokelat Kacang', 3)]

def create_mock_data():
    products = []
    for name in product_name:
        stock_start = fake.pyint()
        for i in range(1, 13):
            stock_in =  fake.pyint(min_value = 1000)
            stock_out = fake.pyint(max_value = stock_start - 1)
            cost_storage = fake.pyint(min_value=1, max_value=5) * 100
            cost_order = math.floor(stock_in / 1000) * 100
            stock_end = stock_start - stock_out + stock_in
            products.append(Product(i, name[0], stock_start, stock_out, stock_in, stock_end, cost_storage, cost_order, name[1]))
            stock_start = stock_end

    return products


data = create_mock_data()

df = pd.DataFrame.from_records(vars(o) for o in data)

st.title("Dashboard Data Analisis Inventori")

# Menampilkan data inventori
st.subheader('Data Inventori')
st.dataframe(df)

# Menampilkan grafik jumlah stok

produk_list = df['nama'].unique()
selected_produk = st.selectbox('Pilih Produk:', produk_list)
selected_df = df[df['nama'] == selected_produk]

st.subheader('Grafik Jumlah Stok')
fig, ax = plt.subplots()
selected_df.plot(x='bulan', y=['jumlah_stok_awal', 'pemasukan_stok', 'pengeluaran_stok', 'jumlah_stok_akhir'], kind='bar', ax=ax)
ax.set_ylabel('Jumlah')
ax.set_xlabel('Bulan')
st.pyplot(fig)

# Menampilkan tabel ringkasan biaya
st.subheader('Ringkasan Biaya')
biaya_summary = df[['biaya_penyimpanan', 'biaya_pemesanan']].sum()
st.table(biaya_summary)

# Menampilkan ringkasan harga produk
st.subheader('Ringkasan Harga Produk')
harga_summary = df['harga_produk'].describe()
st.table(harga_summary)