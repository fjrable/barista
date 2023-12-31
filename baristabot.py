# DATA MENU KOPI
daftar_kopi = {
    1: {'nama': 'Americano', 'harga': 15000},
    2: {'nama': 'Espresso', 'harga': 18000},
    3: {'nama': 'Latte', 'harga': 22000},
    4: {'nama': 'Cappuccino', 'harga': 20000},
    5: {'nama': 'Mocha', 'harga': 25000},
    6: {'nama': 'Arabica', 'harga': 25000},
    7: {'nama': 'Torabicca', 'harga': 15000},
    8: {'nama': 'Robusta', 'harga': 20000},
    9: {'nama': 'Luwak', 'harga': 30000},
    10: {'nama': 'Brazil', 'harga': 15000},
    # Tambahkan kopi lainnya di sini
}

# MENU AWAL

def tampilkan_menu():
    print("Selamat datang di KopiShop! Berikut adalah daftar menu kopi kami: ")
    print("=============================================")

    for nomor, kopi in daftar_kopi.items():
        print(f"{nomor}. {kopi['nama']} - Harga: Rp {kopi['harga']}")

# interaksi dari konsumen
def pesan_kopi():
  nomor_pilihan = int(input("Silahkan pilih nomor kopi yang ingin Anda pesan: "))
  if nomor_pilihan in daftar_kopi:
      kopi_terpilih = daftar_kopi[nomor_pilihan]
      print(f"Anda memesan kopi {kopi_terpilih['nama']} seharga Rp {kopi_terpilih['harga']}.")
      return kopi_terpilih['harga'], True  # Mengembalikan harga kopi dan flag berhasil pesan
  else:
      print("Maaf, nomor kopi yang Anda pilih tidak tersedia.")
      return 0, False  # Mengembalikan 0 dan flag pesanan tidak berhasil

def pembayaran(total_harga):
    print(f"Total harga pesanan: Rp {total_harga}")
    pembayaran = int(input("Masukkan jumlah uang Anda: "))

    if pembayaran >= total_harga:
        kembalian = pembayaran - total_harga
        print(f"Terima kasih! Kembalian Anda: Rp {kembalian}")
    else:
        print("Maaf, uang Anda kurang.")

def main():
    tampilkan_menu()
    total_harga, pesanan_berhasil = pesan_kopi()

    if pesanan_berhasil:
        pembayaran(total_harga)
    else:
        print("Terima kasih!")

main()
