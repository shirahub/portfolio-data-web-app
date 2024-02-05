import datetime
import math
import random
from faker import Faker

fake = Faker('id_ID')

class Product():
    def __init__(self, bulan, nama, jumlah_stok_awal, pengeluaran_stok, pemasukan_stok, jumlah_stok_akhir, biaya_penyimpanan, biaya_pemesanan, harga_produk):
        self.bulan = bulan
        self.nama = nama
        self.jumlah_stok_awal = jumlah_stok_awal
        self.pengeluaran_stok = pengeluaran_stok
        self.jumlah_stok_akhir = jumlah_stok_akhir
        self.pemasukan_stok = pemasukan_stok
        self.biaya_penyimpanan = biaya_penyimpanan
        self.biaya_pemesanan = biaya_pemesanan
        self.harga_produk = harga_produk


product_name = ['Permen Apel', 'Permen Semangka', 'Permen Melon' 'Cokelat Susu', 'Cokelat Kacang']

def create_mock_data():
    products = []
    for name in product_name:
        stock_start = fake.pyint()
        stock_out = fake.pyint(max_value = stock_start - 1)
        for i in range(1, 13):
            stock_in = fake.pyint()
            stock_end = stock_start - stock_out + stock_in
            stock_start = stock_end
            cost_storage = 10 * 1000
            products.append(Product(i, name, stock_start, stock_out, stock_in, stock_end, cost_storage, fake.pyint(max_value=100) * 1000, fake.pyint(max_value=100)))
    
    return products
            