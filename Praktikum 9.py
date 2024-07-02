library = []

def add_book():
    title = input("Masukkan Judul Buku: ")
    author = input("Masukkan Nama Penulis: ")
    year = input("Masukkan Tahun Terbit: ")
    
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print(f"Buku '{title}' berhasil ditambahkan ke perpustakaan!")

def search_books(keyword, search_by):
    results = []
    for book in library:
        if search_by == "title" and keyword.lower() in book["title"].lower():
            results.append(book)
        elif search_by == "year" and keyword == book["year"]:
            results.append(book)
        elif search_by == "author" and keyword.lower() in book["author"].lower():
            results.append(book)
    return results

def display_books(books):
    if not books:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in sorted(books, key=lambda x: x["title"]):
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def display_all_books():
    if not library:
        print("Perpustakaan masih kosong.")
    else:
        print("Daftar Buku di Perpustakaan:")
        for book in sorted(library, key=lambda x: x["title"]):
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Keluar")
        choice = input("Pilih menu: (1/2/3/4): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            print("Pilih cara pencarian:")
            print("1. Berdasarkan Judul")
            print("2. Berdasarkan Tahun")
            print("3. Berdasarkan Penulis")
            search_choice = input("Pilih cara pencarian: (1/2/3): ")
            if search_choice == '1':
                keyword = input("Masukkan kata kunci judul yang ingin dicari: ")
                results = search_books(keyword, "title")
            elif search_choice == '2':
                keyword = input("Masukkan tahun yang ingin dicari: ")
                results = search_books(keyword, "year")
            elif search_choice == '3':
                keyword = input("Masukkan nama penulis yang ingin dicari: ")
                results = search_books(keyword, "author")
            else:
                print("Pilihan Tidak Valid, Silahkan Coba Lagi.")
                continue
            display_books(sorted(results, key=lambda x: int(x["year"])))
        elif choice == '3':
            display_all_books()
        elif choice == '4':
            print("Terima Kasih Telah Menggunakan Perpustakaan!")
            break
        else:
            print("Pilihan Tidak Valid, Silahkan Coba Lagi.")

if __name__ == "__main__":
    main()