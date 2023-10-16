# TODO Найдите количество книг, которое можно разместить на дискете
bytes_ = 4

pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
total_bytes = total_chars * bytes_
disket = 1.44 * 1024 * 1024   # емкость дискеты в байтах
x = int(disket / total_bytes)
print("Количество книг, помещающихся на дискету:", x)
