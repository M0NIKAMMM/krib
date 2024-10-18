bytes_of_symbol = 4
symbols = 25
lines = 50
pages = 100
volume_in_disk = 1.44

volume_book_in_bytes = int(bytes_of_symbol) * int(symbols) * int(lines) * int(pages)
volume_book_in_mb = volume_book_in_bytes / (1024 * 1024)
total_book = round(volume_in_disk // volume_book_in_mb)

print("Количество книг, помещающихся на дискету:", total_book )
