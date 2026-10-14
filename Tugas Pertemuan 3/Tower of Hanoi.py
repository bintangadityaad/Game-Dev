def selesaikan_hanoi(n, tiang_asal, tiang_tujuan, tiang_bantu):
    """
    Fungsi rekursif untuk menyelesaikan puzzle Tower of Hanoi.
    :param n: Jumlah cakram
    :param tiang_asal: Tiang tempat cakram berada saat ini
    :param tiang_tujuan: Tiang target pemindahan cakram
    :param tiang_bantu: Tiang sementara untuk membantu pemindahan
    """
    # Base case: Jika hanya ada 1 cakram, langsung pindahkan ke tujuan
    if n == 1:
        print(f"Pindahkan cakram 1 dari {tiang_asal} ke {tiang_tujuan}")
        return

    # Langkah 1: Pindahkan (n-1) cakram ke tiang bantu
    selesaikan_hanoi(n - 1, tiang_asal, tiang_bantu, tiang_tujuan)

    # Langkah 2: Pindahkan cakram terbesar (cakram ke-n) ke tiang tujuan
    print(f"Pindahkan cakram {n} dari {tiang_asal} ke {tiang_tujuan}")

    # Langkah 3: Pindahkan kembali (n-1) cakram dari tiang bantu ke tiang tujuan
    selesaikan_hanoi(n - 1, tiang_bantu, tiang_tujuan, tiang_asal)

if __name__ == "__main__":
    # Menentukan jumlah cakram
    jumlah_cakram = 3 

    print(f"Langkah-langkah penyelesaian Tower of Hanoi untuk {jumlah_cakram} cakram:")
    print("-" * 55)
    
    # Menjalankan fungsi (Dari tiang A ke tiang C, dibantu tiang B)
    selesaikan_hanoi(jumlah_cakram, 'A', 'C', 'B')
