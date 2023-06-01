# Nama  : Grandies Silvania verdianto
# Kelas : R1
# NIM   : 210511003

try:
    user_input = input("Masukkan sesuatu: ")
    print("Input yang dimasukkan:", user_input)
except EOFError:
    print("Terjadi EOFError. Input tidak ditemukan.")
