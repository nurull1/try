def electron_configuration(atom_number):
    electrons = atom_number
    config = ""
    shell = 1

    while electrons > 0:
        max_electrons = 2 * shell ** 2
        if electrons >= max_electrons:
            config += f"{max_electrons} {shell}s "
            electrons -= max_electrons
        else:
            config += f"{electrons} {shell}s "
            electrons = 0
        shell += 1

    return config.strip()

# Contoh penggunaan:
atom_number = int(input("Masukkan nomor atom: "))
print("Konfigurasi elektron:", electron_configuration(atom_number))
