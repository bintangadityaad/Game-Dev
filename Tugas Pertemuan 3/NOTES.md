# 🗼 Tower of Hanoi (Python)

Berisi implementasi penyelesaian algoritma **Tower of Hanoi** menggunakan bahasa pemrograman Python. Program ini ditulis untuk mendemonstrasikan bagaimana konsep rekursi (fungsi yang memanggil dirinya sendiri) bekerja.

## 📝 Deskripsi Masalah
Tower of Hanoi adalah sebuah teka-teki logika yang terdiri dari 3 tiang (A, B, dan C) dan sejumlah cakram dengan ukuran berbeda. Tujuan utamanya adalah memindahkan seluruh tumpukan cakram dari tiang awal (A) ke tiang tujuan (C), dengan mematuhi 3 aturan berikut:
1. Hanya boleh memindahkan satu cakram dalam satu waktu.
2. Hanya cakram yang berada paling atas dari sebuah tumpukan yang boleh dipindahkan.
3. Cakram yang lebih besar tidak boleh diletakkan di atas cakram yang lebih kecil.

Program ini disimulasikan secara default untuk memindahkan **3 cakram** dari Tiang A ke Tiang C menggunakan Tiang B sebagai bantuan.

## 🧠 Penjelasan Logika Kode (Rekursi)
Untuk menyelesaikan masalah ini secara sistematis, program menggunakan pendekatan **Rekursif**. Secara logika, pemindahan `n` buah cakram dilakukan melalui 3 tahapan utama:

1. **Langkah 1:** Pindahkan `n-1` cakram yang ada di tumpukan atas dari tiang asal (A) ke tiang bantu (B). Ini mengosongkan jalan untuk cakram terbesar di paling bawah.
2. **Langkah 2:** Pindahkan cakram terbesar (cakram ke-`n`) langsung dari tiang asal (A) ke tiang tujuan (C).
3. **Langkah 3:** Pindahkan kembali tumpukan `n-1` cakram yang sedang "menunggu" di tiang bantu (B) ke atas cakram terbesar di tiang tujuan (C).

Program akan terus memecah langkah-langkah di atas (memanggil fungsinya sendiri) hingga tersisa hanya 1 cakram (Base Case), yang dapat langsung dipindahkan tanpa bantuan tiang lain.
