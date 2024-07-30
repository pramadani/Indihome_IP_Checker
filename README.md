# Cari IP Public Otomatis dengan MicroPython

## Deskripsi

Proyek ini menggunakan MicroPython untuk mengontrol sebuah microcontroller yang dapat mereset router secara otomatis menggunakan relay jika IP publik yang diinginkan belum ditemukan. Ini sangat berguna untuk situasi di mana memerlukan IP Public untuk konektivitas internet.

## Latar Belakang
Di beberapa ISP, seperti Indihome, router sering diberikan IP privat dengan awalan 10.x.x.x, yang merupakan bagian dari rentang alamat IP privat yang digunakan dalam jaringan lokal. Dalam beberapa kasus, ISP juga dapat memberikan IP publik, namun alokasi IP publik ini bisa bersifat dinamis dan berubah-ubah. Untuk mendapatkan IP publik secara konsisten, mungkin perlu melakukan reset router berkali-kali hingga mendapatkan IP publik.

## Fitur

- **Pemantauan IP Publik:** Kode secara berkala memeriksa IP publik yang saat ini digunakan.
- **Pengendalian Relay:** Menggunakan relay untuk mereset router jika IP publik yang diinginkan tidak ditemukan.

## Persyaratan

- **Microcontroller:** Seperti ESP8266, ESP32, Raspberry Pico W, dan lainnya.
- **Relay Modul:** Untuk mengendalikan reset router.
- **Router Indihome:** Sebagai Router ISP.
- **Adaptor Daya:** Untuk menyalakan controller setelah unggah kode.
- **Steker & Stop Kontak:** Sebagai input daya router.

## Instalasi

1. **Install MicroPython** pada microcontroller Anda. Dapat mengikuti panduan resmi di [MicroPython](https://micropython.org/download/).

2. **Upload Kode:** Unggah skrip MicroPython ke microcontroller. Dapat menggunakan [ampy](https://github.com/adafruit/ampy) atau [Thonny IDE](https://thonny.org/) untuk meng-upload kode.

3. **Konfigurasi Wifi:** Buat juga file `config.py` yang berisi ssid dan password dari wifi. Contoh: 
```
ssid = ''
password = ''
```

4. **Konfigurasi Relay:** Pastikan relay terhubung dengan benar ke pin yang ditentukan di kode yaitu `GPIO Pin 2`. Kabel AC dihubungkan ke port NC dan ground pada relay.

## Penggunaan

1. **Jalankan Kode:** Unggah kode ke microcontroller dan beri daya ke microcontroller.
2. **Pemantauan:** Microcontroller akan secara otomatis memeriksa IP publik. Jika IP publik yang diinginkan tidak ditemukan dalam waktu yang ditentukan, relay akan diaktifkan untuk mereset router.